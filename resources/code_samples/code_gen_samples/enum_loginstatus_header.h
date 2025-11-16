/**
 * All possible states of a local user
 *
 * @see [...]
 */
EOS_ENUM(EOS_ELoginStatus,
	/** Player has not logged in or chosen a local profile */
	EOS_LS_NotLoggedIn = 0,
	/** Player is using a local profile but is not logged in */
	EOS_LS_UsingLocalProfile = 1,
	/** Player has been validated by the platform specific authentication service */
	EOS_LS_LoggedIn = 2
);
