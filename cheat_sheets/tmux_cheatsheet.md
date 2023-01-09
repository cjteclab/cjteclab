# TMUX cheat sheet
## General informations
The tmux server manages clients, sessions, windows and panes.
- `tmux` : start tmux in terminal. This creates a new session with one window and one pane.
- `ctrl y` : personal prefix command
- keyboard shortcuts can be set at ~/.tmux.config
- `tmux a` : attach to session
- `exit` : Close tmux session

### Session
- `tcmd d` : detach from current session

### Window
- `tcmd c` : create new window
- `tcmd n` : move to next window
- `tcmd p` : move to previous window
- `tcmd 0-9` : move to window number 0-9
- `tcmd &` : kill current window
- `tcmd ,` : rename window
- `tcmd l` : move to previously selected window

### Pane
- `tcmd '` : split the window and creates a new pane (right)
- `tcmd -` : split the window and create a new pane (below)
- `tcmd o` : go to the next pane
- `tcmd ;` : go to the previoues active pane
- `tcmd q` : show pane numbers (switch pane)
- `tcmd x` : kill the current pane
- `tcmd !` : break the pane out of the window

