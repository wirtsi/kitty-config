from kitty.window import DynamicColor

def main(args):
   pass

def handle_result(args, answer, target_window_id, boss):
   tab = boss.active_tab
   w = boss.window_id_map.get(target_window_id)
   if tab is not None:
      if tab.current_layout.name == 'stack':
         w.change_colors({DynamicColor(2):'black'})
         tab.last_used_layout()
      else:
         w.change_colors({DynamicColor(2):'grey29'})
         tab.goto_layout('stack')

handle_result.no_ui = True
