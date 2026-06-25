from scenes import SCENES
from typing import TypedDict
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0.3
)
class GameState(TypedDict):
    current_scene: str
    player_input: str
    interpretation: str
    game_over: bool
class IntentMatch(BaseModel):
    action_key: str
    matched: bool
    
def render_scene(state: GameState):
    scene = SCENES[state["current_scene"]]
    print("\n" + "=" * 50)
    print(scene["description"])
    return state
    
def interpret_action(state: GameState):
    print("\nWhat do you do?\n")
    state["player_input"] = input("\n> ")
    scene = SCENES[state["current_scene"]]
    user_input = state["player_input"]
    possible_actions = list(scene["actions"].keys())
    structured = llm.with_structured_output(IntentMatch)
    while True:
        prompt = f"""
        You are an intent classifier for a text adventure game.
        Player input:
        {user_input}
        Available actions:
        {possible_actions}
        Rules:
        - If the input clearly relates to one of the available actions, set matched=True and return the best matching action_key.
        - If the input cannot reasonably map to any available action, set matched=False.
        - When matched=false, action_key should be an empty string.
        - Return JSON only.
        """
        result = structured.invoke(prompt)
        if result.matched and result.action_key in possible_actions:
            state["interpretation"] = result.action_key
            return state

        print("\nHmm, that doesn't quite fit. Try something else.")
        state["player_input"] = input("\n> ")
        user_input = state["player_input"]
        
def transition(state: GameState):
    scene = SCENES[state["current_scene"]]
    action_key = state["interpretation"]
    if action_key not in scene["actions"]:
        print("You hesitate... unsure how to do that.")
        return state
    state["current_scene"] = scene["actions"][action_key]
    return state

def check_end(state: GameState):
    scene = SCENES[state["current_scene"]]
    state["game_over"] = len(scene["actions"]) == 0
    return state

def route(state: GameState):
    if state["game_over"]:
        return "end_game"
    return "render_scene"
workflow = StateGraph(GameState)

workflow.add_node("render_scene", render_scene)
workflow.add_node("interpret_action", interpret_action)
workflow.add_node("transition", transition)
workflow.add_node("check_end", check_end)

workflow.add_edge(START, "render_scene")
workflow.add_edge("render_scene", "interpret_action")
workflow.add_edge("interpret_action", "transition")
workflow.add_edge("transition", "check_end")

workflow.add_conditional_edges(
    "check_end",
    route,
    {
        "render_scene": "render_scene",
        "end_game": END
    }
)

game = workflow.compile()

def run_game():
    state = {
        "current_scene": "wake_up",
        "player_input": "",
        "interpretation": "",
        "game_over": False
    }

    game.invoke(state)
    print("\nGame Over.")

run_game()
