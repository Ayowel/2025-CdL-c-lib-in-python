class EOS_ELoginStatus(c_int32):
    def __init__(self, value):
        # [...]
EOS_LS_NotLoggedIn = EOS_ELoginStatus(0)
EOS_LS_UsingLocalProfile = EOS_ELoginStatus(1)
EOS_LS_LoggedIn = EOS_ELoginStatus(2)
