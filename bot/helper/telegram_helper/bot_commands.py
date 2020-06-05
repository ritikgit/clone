class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'public'
        self.TarMirrorCommand = 'publictar'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'list'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'authorize'
        self.UnAuthorizeCommand = 'unauthorize'
        self.PingCommand = 'ping'
        self.RestartCommand = 'restart'
        self.StatsCommand = 'stats'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = "publicclone"
        self.WatchCommand = 'publicwatch'
        self.TarWatchCommand = 'publictarwatch'

BotCommands = _BotCommands()
