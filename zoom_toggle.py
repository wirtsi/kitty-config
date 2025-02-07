from kitty.window import DynamicColor
from kittens.tui.loop import debug
from kitty.boss import Boss
from kittens.tui.handler import result_handler


def main(args: list[str]) -> str:
    pass


@result_handler(no_ui=True)
def handle_result(
    args: list[str], answer: str, target_window_id: int, boss: Boss
) -> None:
    tab = boss.active_tab
    w = boss.window_id_map.get(target_window_id)
    debug(vars(w))

    if tab is not None:
        if tab.current_layout.name == "stack":
            tab.last_used_layout()
        else:
            tab.goto_layout("stack")
