# MTProto API Definitions

Source: Telethon generated TL schema, version `1.44.0`.

Total definitions: `2344`.
Functions: `779`.
Type constructors: `1565`.

This file lists both callable MTProto request functions and TL type constructors.

## Full List

### `function`

| Namespace | Name | Callable Path | Constructor Signature |
|---|---|---|---|
| `account` | `AcceptAuthorizationRequest` | `account.AcceptAuthorizationRequest` | `(self, bot_id: int, scope: str, public_key: str, value_hashes: List[ForwardRef('TypeSecureValueHash')], credentials: 'TypeSecureCredentialsEncrypted')` |
| `account` | `CancelPasswordEmailRequest` | `account.CancelPasswordEmailRequest` | `(self, /, *args, **kwargs)` |
| `account` | `ChangeAuthorizationSettingsRequest` | `account.ChangeAuthorizationSettingsRequest` | `(self, hash: int, confirmed: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None)` |
| `account` | `ChangePhoneRequest` | `account.ChangePhoneRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: str)` |
| `account` | `CheckUsernameRequest` | `account.CheckUsernameRequest` | `(self, username: str)` |
| `account` | `ClearRecentEmojiStatusesRequest` | `account.ClearRecentEmojiStatusesRequest` | `(self, /, *args, **kwargs)` |
| `account` | `ConfirmBotConnectionRequest` | `account.ConfirmBotConnectionRequest` | `(self, bot_id: 'TypeInputUser')` |
| `account` | `ConfirmPasswordEmailRequest` | `account.ConfirmPasswordEmailRequest` | `(self, code: str)` |
| `account` | `ConfirmPhoneRequest` | `account.ConfirmPhoneRequest` | `(self, phone_code_hash: str, phone_code: str)` |
| `account` | `CreateBusinessChatLinkRequest` | `account.CreateBusinessChatLinkRequest` | `(self, link: 'TypeInputBusinessChatLink')` |
| `account` | `CreateThemeRequest` | `account.CreateThemeRequest` | `(self, slug: str, title: str, document: Optional[ForwardRef('TypeInputDocument')] = None, settings: Optional[List[ForwardRef('TypeInputThemeSettings')]] = None)` |
| `account` | `DeclinePasswordResetRequest` | `account.DeclinePasswordResetRequest` | `(self, /, *args, **kwargs)` |
| `account` | `DeleteAccountRequest` | `account.DeleteAccountRequest` | `(self, reason: str, password: Optional[ForwardRef('TypeInputCheckPasswordSRP')] = None)` |
| `account` | `DeleteAutoSaveExceptionsRequest` | `account.DeleteAutoSaveExceptionsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `DeleteBusinessChatLinkRequest` | `account.DeleteBusinessChatLinkRequest` | `(self, slug: str)` |
| `account` | `DeletePasskeyRequest` | `account.DeletePasskeyRequest` | `(self, id: str)` |
| `account` | `DeleteSecureValueRequest` | `account.DeleteSecureValueRequest` | `(self, types: List[ForwardRef('TypeSecureValueType')])` |
| `account` | `DeleteWebBrowserSettingsExceptionsRequest` | `account.DeleteWebBrowserSettingsExceptionsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `DisablePeerConnectedBotRequest` | `account.DisablePeerConnectedBotRequest` | `(self, peer: 'TypeInputPeer')` |
| `account` | `EditBusinessChatLinkRequest` | `account.EditBusinessChatLinkRequest` | `(self, slug: str, link: 'TypeInputBusinessChatLink')` |
| `account` | `FinishTakeoutSessionRequest` | `account.FinishTakeoutSessionRequest` | `(self, success: Optional[bool] = None)` |
| `account` | `GetAccountTTLRequest` | `account.GetAccountTTLRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetAllSecureValuesRequest` | `account.GetAllSecureValuesRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetAuthorizationFormRequest` | `account.GetAuthorizationFormRequest` | `(self, bot_id: int, scope: str, public_key: str)` |
| `account` | `GetAuthorizationsRequest` | `account.GetAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetAutoDownloadSettingsRequest` | `account.GetAutoDownloadSettingsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetAutoSaveSettingsRequest` | `account.GetAutoSaveSettingsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetBotBusinessConnectionRequest` | `account.GetBotBusinessConnectionRequest` | `(self, connection_id: str)` |
| `account` | `GetBusinessChatLinksRequest` | `account.GetBusinessChatLinksRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetChannelDefaultEmojiStatusesRequest` | `account.GetChannelDefaultEmojiStatusesRequest` | `(self, hash: int)` |
| `account` | `GetChannelRestrictedStatusEmojisRequest` | `account.GetChannelRestrictedStatusEmojisRequest` | `(self, hash: int)` |
| `account` | `GetChatThemesRequest` | `account.GetChatThemesRequest` | `(self, hash: int)` |
| `account` | `GetCollectibleEmojiStatusesRequest` | `account.GetCollectibleEmojiStatusesRequest` | `(self, hash: int)` |
| `account` | `GetConnectedBotsRequest` | `account.GetConnectedBotsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetContactSignUpNotificationRequest` | `account.GetContactSignUpNotificationRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetContentSettingsRequest` | `account.GetContentSettingsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetDefaultBackgroundEmojisRequest` | `account.GetDefaultBackgroundEmojisRequest` | `(self, hash: int)` |
| `account` | `GetDefaultEmojiStatusesRequest` | `account.GetDefaultEmojiStatusesRequest` | `(self, hash: int)` |
| `account` | `GetDefaultGroupPhotoEmojisRequest` | `account.GetDefaultGroupPhotoEmojisRequest` | `(self, hash: int)` |
| `account` | `GetDefaultProfilePhotoEmojisRequest` | `account.GetDefaultProfilePhotoEmojisRequest` | `(self, hash: int)` |
| `account` | `GetGlobalPrivacySettingsRequest` | `account.GetGlobalPrivacySettingsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetMultiWallPapersRequest` | `account.GetMultiWallPapersRequest` | `(self, wallpapers: List[ForwardRef('TypeInputWallPaper')])` |
| `account` | `GetNotifyExceptionsRequest` | `account.GetNotifyExceptionsRequest` | `(self, compare_sound: Optional[bool] = None, compare_stories: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputNotifyPeer')] = None)` |
| `account` | `GetNotifySettingsRequest` | `account.GetNotifySettingsRequest` | `(self, peer: 'TypeInputNotifyPeer')` |
| `account` | `GetPaidMessagesRevenueRequest` | `account.GetPaidMessagesRevenueRequest` | `(self, user_id: 'TypeInputUser', parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `account` | `GetPasskeysRequest` | `account.GetPasskeysRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetPasswordRequest` | `account.GetPasswordRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetPasswordSettingsRequest` | `account.GetPasswordSettingsRequest` | `(self, password: 'TypeInputCheckPasswordSRP')` |
| `account` | `GetPrivacyRequest` | `account.GetPrivacyRequest` | `(self, key: 'TypeInputPrivacyKey')` |
| `account` | `GetReactionsNotifySettingsRequest` | `account.GetReactionsNotifySettingsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetRecentEmojiStatusesRequest` | `account.GetRecentEmojiStatusesRequest` | `(self, hash: int)` |
| `account` | `GetSavedMusicIdsRequest` | `account.GetSavedMusicIdsRequest` | `(self, hash: int)` |
| `account` | `GetSavedRingtonesRequest` | `account.GetSavedRingtonesRequest` | `(self, hash: int)` |
| `account` | `GetSecureValueRequest` | `account.GetSecureValueRequest` | `(self, types: List[ForwardRef('TypeSecureValueType')])` |
| `account` | `GetThemeRequest` | `account.GetThemeRequest` | `(self, format: str, theme: 'TypeInputTheme')` |
| `account` | `GetThemesRequest` | `account.GetThemesRequest` | `(self, format: str, hash: int)` |
| `account` | `GetTmpPasswordRequest` | `account.GetTmpPasswordRequest` | `(self, password: 'TypeInputCheckPasswordSRP', period: int)` |
| `account` | `GetUniqueGiftChatThemesRequest` | `account.GetUniqueGiftChatThemesRequest` | `(self, offset: str, limit: int, hash: int)` |
| `account` | `GetWallPaperRequest` | `account.GetWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper')` |
| `account` | `GetWallPapersRequest` | `account.GetWallPapersRequest` | `(self, hash: int)` |
| `account` | `GetWebAuthorizationsRequest` | `account.GetWebAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `GetWebBrowserSettingsRequest` | `account.GetWebBrowserSettingsRequest` | `(self, hash: int)` |
| `account` | `InitPasskeyRegistrationRequest` | `account.InitPasskeyRegistrationRequest` | `(self, /, *args, **kwargs)` |
| `account` | `InitTakeoutSessionRequest` | `account.InitTakeoutSessionRequest` | `(self, contacts: Optional[bool] = None, message_users: Optional[bool] = None, message_chats: Optional[bool] = None, message_megagroups: Optional[bool] = None, message_channels: Optional[bool] = None, files: Optional[bool] = None, file_max_size: Optional[int] = None)` |
| `account` | `InstallThemeRequest` | `account.InstallThemeRequest` | `(self, dark: Optional[bool] = None, theme: Optional[ForwardRef('TypeInputTheme')] = None, format: Optional[str] = None, base_theme: Optional[ForwardRef('TypeBaseTheme')] = None)` |
| `account` | `InstallWallPaperRequest` | `account.InstallWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper', settings: 'TypeWallPaperSettings')` |
| `account` | `InvalidateSignInCodesRequest` | `account.InvalidateSignInCodesRequest` | `(self, codes: List[str])` |
| `account` | `RegisterDeviceRequest` | `account.RegisterDeviceRequest` | `(self, token_type: int, token: str, app_sandbox: bool, secret: bytes, other_uids: List[int], no_muted: Optional[bool] = None)` |
| `account` | `RegisterPasskeyRequest` | `account.RegisterPasskeyRequest` | `(self, credential: 'TypeInputPasskeyCredential')` |
| `account` | `ReorderUsernamesRequest` | `account.ReorderUsernamesRequest` | `(self, order: List[str])` |
| `account` | `ReportPeerRequest` | `account.ReportPeerRequest` | `(self, peer: 'TypeInputPeer', reason: 'TypeReportReason', message: str)` |
| `account` | `ReportProfilePhotoRequest` | `account.ReportProfilePhotoRequest` | `(self, peer: 'TypeInputPeer', photo_id: 'TypeInputPhoto', reason: 'TypeReportReason', message: str)` |
| `account` | `ResendPasswordEmailRequest` | `account.ResendPasswordEmailRequest` | `(self, /, *args, **kwargs)` |
| `account` | `ResetAuthorizationRequest` | `account.ResetAuthorizationRequest` | `(self, hash: int)` |
| `account` | `ResetNotifySettingsRequest` | `account.ResetNotifySettingsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `ResetPasswordRequest` | `account.ResetPasswordRequest` | `(self, /, *args, **kwargs)` |
| `account` | `ResetWallPapersRequest` | `account.ResetWallPapersRequest` | `(self, /, *args, **kwargs)` |
| `account` | `ResetWebAuthorizationRequest` | `account.ResetWebAuthorizationRequest` | `(self, hash: int)` |
| `account` | `ResetWebAuthorizationsRequest` | `account.ResetWebAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `account` | `ResolveBusinessChatLinkRequest` | `account.ResolveBusinessChatLinkRequest` | `(self, slug: str)` |
| `account` | `SaveAutoDownloadSettingsRequest` | `account.SaveAutoDownloadSettingsRequest` | `(self, settings: 'TypeAutoDownloadSettings', low: Optional[bool] = None, high: Optional[bool] = None)` |
| `account` | `SaveAutoSaveSettingsRequest` | `account.SaveAutoSaveSettingsRequest` | `(self, settings: 'TypeAutoSaveSettings', users: Optional[bool] = None, chats: Optional[bool] = None, broadcasts: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `account` | `SaveMusicRequest` | `account.SaveMusicRequest` | `(self, id: 'TypeInputDocument', unsave: Optional[bool] = None, after_id: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `account` | `SaveRingtoneRequest` | `account.SaveRingtoneRequest` | `(self, id: 'TypeInputDocument', unsave: bool)` |
| `account` | `SaveSecureValueRequest` | `account.SaveSecureValueRequest` | `(self, value: 'TypeInputSecureValue', secure_secret_id: int)` |
| `account` | `SaveThemeRequest` | `account.SaveThemeRequest` | `(self, theme: 'TypeInputTheme', unsave: bool)` |
| `account` | `SaveWallPaperRequest` | `account.SaveWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper', unsave: bool, settings: 'TypeWallPaperSettings')` |
| `account` | `SendChangePhoneCodeRequest` | `account.SendChangePhoneCodeRequest` | `(self, phone_number: str, settings: 'TypeCodeSettings')` |
| `account` | `SendConfirmPhoneCodeRequest` | `account.SendConfirmPhoneCodeRequest` | `(self, hash: str, settings: 'TypeCodeSettings')` |
| `account` | `SendVerifyEmailCodeRequest` | `account.SendVerifyEmailCodeRequest` | `(self, purpose: 'TypeEmailVerifyPurpose', email: str)` |
| `account` | `SendVerifyPhoneCodeRequest` | `account.SendVerifyPhoneCodeRequest` | `(self, phone_number: str, settings: 'TypeCodeSettings')` |
| `account` | `SetAccountTTLRequest` | `account.SetAccountTTLRequest` | `(self, ttl: 'TypeAccountDaysTTL')` |
| `account` | `SetAuthorizationTTLRequest` | `account.SetAuthorizationTTLRequest` | `(self, authorization_ttl_days: int)` |
| `account` | `SetContactSignUpNotificationRequest` | `account.SetContactSignUpNotificationRequest` | `(self, silent: bool)` |
| `account` | `SetContentSettingsRequest` | `account.SetContentSettingsRequest` | `(self, sensitive_enabled: Optional[bool] = None)` |
| `account` | `SetGlobalPrivacySettingsRequest` | `account.SetGlobalPrivacySettingsRequest` | `(self, settings: 'TypeGlobalPrivacySettings')` |
| `account` | `SetMainProfileTabRequest` | `account.SetMainProfileTabRequest` | `(self, tab: 'TypeProfileTab')` |
| `account` | `SetPrivacyRequest` | `account.SetPrivacyRequest` | `(self, key: 'TypeInputPrivacyKey', rules: List[ForwardRef('TypeInputPrivacyRule')])` |
| `account` | `SetReactionsNotifySettingsRequest` | `account.SetReactionsNotifySettingsRequest` | `(self, settings: 'TypeReactionsNotifySettings')` |
| `account` | `ToggleConnectedBotPausedRequest` | `account.ToggleConnectedBotPausedRequest` | `(self, peer: 'TypeInputPeer', paused: bool)` |
| `account` | `ToggleNoPaidMessagesExceptionRequest` | `account.ToggleNoPaidMessagesExceptionRequest` | `(self, user_id: 'TypeInputUser', refund_charged: Optional[bool] = None, require_payment: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `account` | `ToggleSponsoredMessagesRequest` | `account.ToggleSponsoredMessagesRequest` | `(self, enabled: bool)` |
| `account` | `ToggleUsernameRequest` | `account.ToggleUsernameRequest` | `(self, username: str, active: bool)` |
| `account` | `ToggleWebBrowserSettingsExceptionRequest` | `account.ToggleWebBrowserSettingsExceptionRequest` | `(self, url: str, delete: Optional[bool] = None, open_external_browser: Optional[bool] = None)` |
| `account` | `UnregisterDeviceRequest` | `account.UnregisterDeviceRequest` | `(self, token_type: int, token: str, other_uids: List[int])` |
| `account` | `UpdateBirthdayRequest` | `account.UpdateBirthdayRequest` | `(self, birthday: Optional[ForwardRef('TypeBirthday')] = None)` |
| `account` | `UpdateBusinessAwayMessageRequest` | `account.UpdateBusinessAwayMessageRequest` | `(self, message: Optional[ForwardRef('TypeInputBusinessAwayMessage')] = None)` |
| `account` | `UpdateBusinessGreetingMessageRequest` | `account.UpdateBusinessGreetingMessageRequest` | `(self, message: Optional[ForwardRef('TypeInputBusinessGreetingMessage')] = None)` |
| `account` | `UpdateBusinessIntroRequest` | `account.UpdateBusinessIntroRequest` | `(self, intro: Optional[ForwardRef('TypeInputBusinessIntro')] = None)` |
| `account` | `UpdateBusinessLocationRequest` | `account.UpdateBusinessLocationRequest` | `(self, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None, address: Optional[str] = None)` |
| `account` | `UpdateBusinessWorkHoursRequest` | `account.UpdateBusinessWorkHoursRequest` | `(self, business_work_hours: Optional[ForwardRef('TypeBusinessWorkHours')] = None)` |
| `account` | `UpdateColorRequest` | `account.UpdateColorRequest` | `(self, for_profile: Optional[bool] = None, color: Optional[ForwardRef('TypePeerColor')] = None)` |
| `account` | `UpdateConnectedBotRequest` | `account.UpdateConnectedBotRequest` | `(self, bot: 'TypeInputUser', recipients: 'TypeInputBusinessBotRecipients', deleted: Optional[bool] = None, rights: Optional[ForwardRef('TypeBusinessBotRights')] = None)` |
| `account` | `UpdateDeviceLockedRequest` | `account.UpdateDeviceLockedRequest` | `(self, period: int)` |
| `account` | `UpdateEmojiStatusRequest` | `account.UpdateEmojiStatusRequest` | `(self, emoji_status: 'TypeEmojiStatus')` |
| `account` | `UpdateNotifySettingsRequest` | `account.UpdateNotifySettingsRequest` | `(self, peer: 'TypeInputNotifyPeer', settings: 'TypeInputPeerNotifySettings')` |
| `account` | `UpdatePasswordSettingsRequest` | `account.UpdatePasswordSettingsRequest` | `(self, password: 'TypeInputCheckPasswordSRP', new_settings: 'TypePasswordInputSettings')` |
| `account` | `UpdatePersonalChannelRequest` | `account.UpdatePersonalChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `account` | `UpdateProfileRequest` | `account.UpdateProfileRequest` | `(self, first_name: Optional[str] = None, last_name: Optional[str] = None, about: Optional[str] = None)` |
| `account` | `UpdateStatusRequest` | `account.UpdateStatusRequest` | `(self, offline: bool)` |
| `account` | `UpdateThemeRequest` | `account.UpdateThemeRequest` | `(self, format: str, theme: 'TypeInputTheme', slug: Optional[str] = None, title: Optional[str] = None, document: Optional[ForwardRef('TypeInputDocument')] = None, settings: Optional[List[ForwardRef('TypeInputThemeSettings')]] = None)` |
| `account` | `UpdateUsernameRequest` | `account.UpdateUsernameRequest` | `(self, username: str)` |
| `account` | `UpdateWebBrowserSettingsRequest` | `account.UpdateWebBrowserSettingsRequest` | `(self, open_external_browser: Optional[bool] = None, display_close_button: Optional[bool] = None)` |
| `account` | `UploadRingtoneRequest` | `account.UploadRingtoneRequest` | `(self, file: 'TypeInputFile', file_name: str, mime_type: str)` |
| `account` | `UploadThemeRequest` | `account.UploadThemeRequest` | `(self, file: 'TypeInputFile', file_name: str, mime_type: str, thumb: Optional[ForwardRef('TypeInputFile')] = None)` |
| `account` | `UploadWallPaperRequest` | `account.UploadWallPaperRequest` | `(self, file: 'TypeInputFile', mime_type: str, settings: 'TypeWallPaperSettings', for_chat: Optional[bool] = None)` |
| `account` | `VerifyEmailRequest` | `account.VerifyEmailRequest` | `(self, purpose: 'TypeEmailVerifyPurpose', verification: 'TypeEmailVerification')` |
| `account` | `VerifyPhoneRequest` | `account.VerifyPhoneRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: str)` |
| `aicompose` | `CreateToneRequest` | `aicompose.CreateToneRequest` | `(self, emoji_id: int, title: str, prompt: str, display_author: Optional[bool] = None)` |
| `aicompose` | `DeleteToneRequest` | `aicompose.DeleteToneRequest` | `(self, tone: 'TypeInputAiComposeTone')` |
| `aicompose` | `GetToneExampleRequest` | `aicompose.GetToneExampleRequest` | `(self, tone: 'TypeInputAiComposeTone', num: int)` |
| `aicompose` | `GetToneRequest` | `aicompose.GetToneRequest` | `(self, tone: 'TypeInputAiComposeTone')` |
| `aicompose` | `GetTonesRequest` | `aicompose.GetTonesRequest` | `(self, hash: int)` |
| `aicompose` | `SaveToneRequest` | `aicompose.SaveToneRequest` | `(self, tone: 'TypeInputAiComposeTone', unsave: bool)` |
| `aicompose` | `UpdateToneRequest` | `aicompose.UpdateToneRequest` | `(self, tone: 'TypeInputAiComposeTone', display_author: Optional[bool] = None, emoji_id: Optional[int] = None, title: Optional[str] = None, prompt: Optional[str] = None)` |
| `auth` | `AcceptLoginTokenRequest` | `auth.AcceptLoginTokenRequest` | `(self, token: bytes)` |
| `auth` | `BindTempAuthKeyRequest` | `auth.BindTempAuthKeyRequest` | `(self, perm_auth_key_id: int, nonce: int, expires_at: Optional[datetime.datetime], encrypted_message: bytes)` |
| `auth` | `CancelCodeRequest` | `auth.CancelCodeRequest` | `(self, phone_number: str, phone_code_hash: str)` |
| `auth` | `CheckPaidAuthRequest` | `auth.CheckPaidAuthRequest` | `(self, phone_number: str, phone_code_hash: str, form_id: int)` |
| `auth` | `CheckPasswordRequest` | `auth.CheckPasswordRequest` | `(self, password: 'TypeInputCheckPasswordSRP')` |
| `auth` | `CheckRecoveryPasswordRequest` | `auth.CheckRecoveryPasswordRequest` | `(self, code: str)` |
| `auth` | `DropTempAuthKeysRequest` | `auth.DropTempAuthKeysRequest` | `(self, except_auth_keys: List[int])` |
| `auth` | `ExportAuthorizationRequest` | `auth.ExportAuthorizationRequest` | `(self, dc_id: int)` |
| `auth` | `ExportLoginTokenRequest` | `auth.ExportLoginTokenRequest` | `(self, api_id: int, api_hash: str, except_ids: List[int])` |
| `auth` | `FinishPasskeyLoginRequest` | `auth.FinishPasskeyLoginRequest` | `(self, credential: 'TypeInputPasskeyCredential', from_dc_id: Optional[int] = None, from_auth_key_id: Optional[int] = None)` |
| `auth` | `ImportAuthorizationRequest` | `auth.ImportAuthorizationRequest` | `(self, id: int, bytes: bytes)` |
| `auth` | `ImportBotAuthorizationRequest` | `auth.ImportBotAuthorizationRequest` | `(self, flags: int, api_id: int, api_hash: str, bot_auth_token: str)` |
| `auth` | `ImportLoginTokenRequest` | `auth.ImportLoginTokenRequest` | `(self, token: bytes)` |
| `auth` | `ImportWebTokenAuthorizationRequest` | `auth.ImportWebTokenAuthorizationRequest` | `(self, api_id: int, api_hash: str, web_auth_token: str)` |
| `auth` | `InitPasskeyLoginRequest` | `auth.InitPasskeyLoginRequest` | `(self, api_id: int, api_hash: str)` |
| `auth` | `LogOutRequest` | `auth.LogOutRequest` | `(self, /, *args, **kwargs)` |
| `auth` | `RecoverPasswordRequest` | `auth.RecoverPasswordRequest` | `(self, code: str, new_settings: Optional[ForwardRef('TypePasswordInputSettings')] = None)` |
| `auth` | `ReportMissingCodeRequest` | `auth.ReportMissingCodeRequest` | `(self, phone_number: str, phone_code_hash: str, mnc: str)` |
| `auth` | `RequestFirebaseSmsRequest` | `auth.RequestFirebaseSmsRequest` | `(self, phone_number: str, phone_code_hash: str, safety_net_token: Optional[str] = None, play_integrity_token: Optional[str] = None, ios_push_secret: Optional[str] = None)` |
| `auth` | `RequestPasswordRecoveryRequest` | `auth.RequestPasswordRecoveryRequest` | `(self, /, *args, **kwargs)` |
| `auth` | `ResendCodeRequest` | `auth.ResendCodeRequest` | `(self, phone_number: str, phone_code_hash: str, reason: Optional[str] = None)` |
| `auth` | `ResetAuthorizationsRequest` | `auth.ResetAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `auth` | `ResetLoginEmailRequest` | `auth.ResetLoginEmailRequest` | `(self, phone_number: str, phone_code_hash: str)` |
| `auth` | `SendCodeRequest` | `auth.SendCodeRequest` | `(self, phone_number: str, api_id: int, api_hash: str, settings: 'TypeCodeSettings')` |
| `auth` | `SignInRequest` | `auth.SignInRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: Optional[str] = None, email_verification: Optional[ForwardRef('TypeEmailVerification')] = None)` |
| `auth` | `SignUpRequest` | `auth.SignUpRequest` | `(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str, no_joined_notifications: Optional[bool] = None)` |
| `bots` | `AddPreviewMediaRequest` | `bots.AddPreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia')` |
| `bots` | `AllowSendMessageRequest` | `bots.AllowSendMessageRequest` | `(self, bot: 'TypeInputUser')` |
| `bots` | `AnswerWebhookJSONQueryRequest` | `bots.AnswerWebhookJSONQueryRequest` | `(self, query_id: int, data: 'TypeDataJSON')` |
| `bots` | `CanSendMessageRequest` | `bots.CanSendMessageRequest` | `(self, bot: 'TypeInputUser')` |
| `bots` | `CheckDownloadFileParamsRequest` | `bots.CheckDownloadFileParamsRequest` | `(self, bot: 'TypeInputUser', file_name: str, url: str)` |
| `bots` | `CheckUsernameRequest` | `bots.CheckUsernameRequest` | `(self, username: str)` |
| `bots` | `CreateBotRequest` | `bots.CreateBotRequest` | `(self, name: str, username: str, manager_id: 'TypeInputUser', via_deeplink: Optional[bool] = None)` |
| `bots` | `DeletePreviewMediaRequest` | `bots.DeletePreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: List[ForwardRef('TypeInputMedia')])` |
| `bots` | `EditAccessSettingsRequest` | `bots.EditAccessSettingsRequest` | `(self, bot: 'TypeInputUser', restricted: Optional[bool] = None, add_users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `bots` | `EditPreviewMediaRequest` | `bots.EditPreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia', new_media: 'TypeInputMedia')` |
| `bots` | `ExportBotTokenRequest` | `bots.ExportBotTokenRequest` | `(self, bot: 'TypeInputUser', revoke: bool)` |
| `bots` | `GetAccessSettingsRequest` | `bots.GetAccessSettingsRequest` | `(self, bot: 'TypeInputUser')` |
| `bots` | `GetAdminedBotsRequest` | `bots.GetAdminedBotsRequest` | `(self, /, *args, **kwargs)` |
| `bots` | `GetBotCommandsRequest` | `bots.GetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str)` |
| `bots` | `GetBotInfoRequest` | `bots.GetBotInfoRequest` | `(self, lang_code: str, bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `bots` | `GetBotMenuButtonRequest` | `bots.GetBotMenuButtonRequest` | `(self, user_id: 'TypeInputUser')` |
| `bots` | `GetBotRecommendationsRequest` | `bots.GetBotRecommendationsRequest` | `(self, bot: 'TypeInputUser')` |
| `bots` | `GetPopularAppBotsRequest` | `bots.GetPopularAppBotsRequest` | `(self, offset: str, limit: int)` |
| `bots` | `GetPreviewInfoRequest` | `bots.GetPreviewInfoRequest` | `(self, bot: 'TypeInputUser', lang_code: str)` |
| `bots` | `GetPreviewMediasRequest` | `bots.GetPreviewMediasRequest` | `(self, bot: 'TypeInputUser')` |
| `bots` | `GetRequestedWebViewButtonRequest` | `bots.GetRequestedWebViewButtonRequest` | `(self, bot: 'TypeInputUser', webapp_req_id: str)` |
| `bots` | `InvokeWebViewCustomMethodRequest` | `bots.InvokeWebViewCustomMethodRequest` | `(self, bot: 'TypeInputUser', custom_method: str, params: 'TypeDataJSON')` |
| `bots` | `ReorderPreviewMediasRequest` | `bots.ReorderPreviewMediasRequest` | `(self, bot: 'TypeInputUser', lang_code: str, order: List[ForwardRef('TypeInputMedia')])` |
| `bots` | `ReorderUsernamesRequest` | `bots.ReorderUsernamesRequest` | `(self, bot: 'TypeInputUser', order: List[str])` |
| `bots` | `RequestWebViewButtonRequest` | `bots.RequestWebViewButtonRequest` | `(self, user_id: 'TypeInputUser', button: 'TypeKeyboardButton')` |
| `bots` | `ResetBotCommandsRequest` | `bots.ResetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str)` |
| `bots` | `SendCustomRequestRequest` | `bots.SendCustomRequestRequest` | `(self, custom_method: str, params: 'TypeDataJSON')` |
| `bots` | `SetBotBroadcastDefaultAdminRightsRequest` | `bots.SetBotBroadcastDefaultAdminRightsRequest` | `(self, admin_rights: 'TypeChatAdminRights')` |
| `bots` | `SetBotCommandsRequest` | `bots.SetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str, commands: List[ForwardRef('TypeBotCommand')])` |
| `bots` | `SetBotGroupDefaultAdminRightsRequest` | `bots.SetBotGroupDefaultAdminRightsRequest` | `(self, admin_rights: 'TypeChatAdminRights')` |
| `bots` | `SetBotInfoRequest` | `bots.SetBotInfoRequest` | `(self, lang_code: str, bot: Optional[ForwardRef('TypeInputUser')] = None, name: Optional[str] = None, about: Optional[str] = None, description: Optional[str] = None)` |
| `bots` | `SetBotMenuButtonRequest` | `bots.SetBotMenuButtonRequest` | `(self, user_id: 'TypeInputUser', button: 'TypeBotMenuButton')` |
| `bots` | `SetCustomVerificationRequest` | `bots.SetCustomVerificationRequest` | `(self, peer: 'TypeInputPeer', enabled: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None, custom_description: Optional[str] = None)` |
| `bots` | `SetJoinChatResultsRequest` | `bots.SetJoinChatResultsRequest` | `(self, query_id: int, result: 'TypeJoinChatBotResult')` |
| `bots` | `ToggleUserEmojiStatusPermissionRequest` | `bots.ToggleUserEmojiStatusPermissionRequest` | `(self, bot: 'TypeInputUser', enabled: bool)` |
| `bots` | `ToggleUsernameRequest` | `bots.ToggleUsernameRequest` | `(self, bot: 'TypeInputUser', username: str, active: bool)` |
| `bots` | `UpdateStarRefProgramRequest` | `bots.UpdateStarRefProgramRequest` | `(self, bot: 'TypeInputUser', commission_permille: int, duration_months: Optional[int] = None)` |
| `bots` | `UpdateUserEmojiStatusRequest` | `bots.UpdateUserEmojiStatusRequest` | `(self, user_id: 'TypeInputUser', emoji_status: 'TypeEmojiStatus')` |
| `channels` | `CheckSearchPostsFloodRequest` | `channels.CheckSearchPostsFloodRequest` | `(self, query: Optional[str] = None)` |
| `channels` | `CheckUsernameRequest` | `channels.CheckUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str)` |
| `channels` | `ConvertToGigagroupRequest` | `channels.ConvertToGigagroupRequest` | `(self, channel: 'TypeInputChannel')` |
| `channels` | `CreateChannelRequest` | `channels.CreateChannelRequest` | `(self, title: str, about: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, for_import: Optional[bool] = None, forum: Optional[bool] = None, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None, address: Optional[str] = None, ttl_period: Optional[int] = None)` |
| `channels` | `DeactivateAllUsernamesRequest` | `channels.DeactivateAllUsernamesRequest` | `(self, channel: 'TypeInputChannel')` |
| `channels` | `DeleteChannelRequest` | `channels.DeleteChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `channels` | `DeleteHistoryRequest` | `channels.DeleteHistoryRequest` | `(self, channel: 'TypeInputChannel', max_id: int, for_everyone: Optional[bool] = None)` |
| `channels` | `DeleteMessagesRequest` | `channels.DeleteMessagesRequest` | `(self, channel: 'TypeInputChannel', id: List[int])` |
| `channels` | `DeleteParticipantHistoryRequest` | `channels.DeleteParticipantHistoryRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer')` |
| `channels` | `EditAdminRequest` | `channels.EditAdminRequest` | `(self, channel: 'TypeInputChannel', user_id: 'TypeInputUser', admin_rights: 'TypeChatAdminRights', rank: Optional[str] = None)` |
| `channels` | `EditBannedRequest` | `channels.EditBannedRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer', banned_rights: 'TypeChatBannedRights')` |
| `channels` | `EditLocationRequest` | `channels.EditLocationRequest` | `(self, channel: 'TypeInputChannel', geo_point: 'TypeInputGeoPoint', address: str)` |
| `channels` | `EditPhotoRequest` | `channels.EditPhotoRequest` | `(self, channel: 'TypeInputChannel', photo: 'TypeInputChatPhoto')` |
| `channels` | `EditTitleRequest` | `channels.EditTitleRequest` | `(self, channel: 'TypeInputChannel', title: str)` |
| `channels` | `ExportMessageLinkRequest` | `channels.ExportMessageLinkRequest` | `(self, channel: 'TypeInputChannel', id: int, grouped: Optional[bool] = None, thread: Optional[bool] = None)` |
| `channels` | `GetAdminLogRequest` | `channels.GetAdminLogRequest` | `(self, channel: 'TypeInputChannel', q: str, max_id: int, min_id: int, limit: int, events_filter: Optional[ForwardRef('TypeChannelAdminLogEventsFilter')] = None, admins: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `channels` | `GetAdminedPublicChannelsRequest` | `channels.GetAdminedPublicChannelsRequest` | `(self, by_location: Optional[bool] = None, check_limit: Optional[bool] = None, for_personal: Optional[bool] = None)` |
| `channels` | `GetChannelRecommendationsRequest` | `channels.GetChannelRecommendationsRequest` | `(self, channel: Optional[ForwardRef('TypeInputChannel')] = None)` |
| `channels` | `GetChannelsRequest` | `channels.GetChannelsRequest` | `(self, id: List[ForwardRef('TypeInputChannel')])` |
| `channels` | `GetFullChannelRequest` | `channels.GetFullChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `channels` | `GetGroupsForDiscussionRequest` | `channels.GetGroupsForDiscussionRequest` | `(self, /, *args, **kwargs)` |
| `channels` | `GetInactiveChannelsRequest` | `channels.GetInactiveChannelsRequest` | `(self, /, *args, **kwargs)` |
| `channels` | `GetLeftChannelsRequest` | `channels.GetLeftChannelsRequest` | `(self, offset: int)` |
| `channels` | `GetMessageAuthorRequest` | `channels.GetMessageAuthorRequest` | `(self, channel: 'TypeInputChannel', id: int)` |
| `channels` | `GetMessagesRequest` | `channels.GetMessagesRequest` | `(self, channel: 'TypeInputChannel', id: List[ForwardRef('TypeInputMessage')])` |
| `channels` | `GetParticipantRequest` | `channels.GetParticipantRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer')` |
| `channels` | `GetParticipantsRequest` | `channels.GetParticipantsRequest` | `(self, channel: 'TypeInputChannel', filter: 'TypeChannelParticipantsFilter', offset: int, limit: int, hash: int)` |
| `channels` | `GetSendAsRequest` | `channels.GetSendAsRequest` | `(self, peer: 'TypeInputPeer', for_paid_reactions: Optional[bool] = None, for_live_stories: Optional[bool] = None)` |
| `channels` | `InviteToChannelRequest` | `channels.InviteToChannelRequest` | `(self, channel: 'TypeInputChannel', users: List[ForwardRef('TypeInputUser')])` |
| `channels` | `JoinChannelRequest` | `channels.JoinChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `channels` | `LeaveChannelRequest` | `channels.LeaveChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `channels` | `ReadHistoryRequest` | `channels.ReadHistoryRequest` | `(self, channel: 'TypeInputChannel', max_id: int)` |
| `channels` | `ReadMessageContentsRequest` | `channels.ReadMessageContentsRequest` | `(self, channel: 'TypeInputChannel', id: List[int])` |
| `channels` | `ReorderUsernamesRequest` | `channels.ReorderUsernamesRequest` | `(self, channel: 'TypeInputChannel', order: List[str])` |
| `channels` | `ReportAntiSpamFalsePositiveRequest` | `channels.ReportAntiSpamFalsePositiveRequest` | `(self, channel: 'TypeInputChannel', msg_id: int)` |
| `channels` | `ReportSpamRequest` | `channels.ReportSpamRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer', id: List[int])` |
| `channels` | `RestrictSponsoredMessagesRequest` | `channels.RestrictSponsoredMessagesRequest` | `(self, channel: 'TypeInputChannel', restricted: bool)` |
| `channels` | `SearchPostsRequest` | `channels.SearchPostsRequest` | `(self, offset_rate: int, offset_peer: 'TypeInputPeer', offset_id: int, limit: int, hashtag: Optional[str] = None, query: Optional[str] = None, allow_paid_stars: Optional[int] = None)` |
| `channels` | `SetBoostsToUnblockRestrictionsRequest` | `channels.SetBoostsToUnblockRestrictionsRequest` | `(self, channel: 'TypeInputChannel', boosts: int)` |
| `channels` | `SetDiscussionGroupRequest` | `channels.SetDiscussionGroupRequest` | `(self, broadcast: 'TypeInputChannel', group: 'TypeInputChannel')` |
| `channels` | `SetEmojiStickersRequest` | `channels.SetEmojiStickersRequest` | `(self, channel: 'TypeInputChannel', stickerset: 'TypeInputStickerSet')` |
| `channels` | `SetMainProfileTabRequest` | `channels.SetMainProfileTabRequest` | `(self, channel: 'TypeInputChannel', tab: 'TypeProfileTab')` |
| `channels` | `SetStickersRequest` | `channels.SetStickersRequest` | `(self, channel: 'TypeInputChannel', stickerset: 'TypeInputStickerSet')` |
| `channels` | `ToggleAntiSpamRequest` | `channels.ToggleAntiSpamRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `channels` | `ToggleAutotranslationRequest` | `channels.ToggleAutotranslationRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `channels` | `ToggleForumRequest` | `channels.ToggleForumRequest` | `(self, channel: 'TypeInputChannel', enabled: bool, tabs: bool)` |
| `channels` | `ToggleJoinRequestRequest` | `channels.ToggleJoinRequestRequest` | `(self, channel: 'TypeInputChannel', enabled: bool, apply_to_invites: Optional[bool] = None, guard_bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `channels` | `ToggleJoinToSendRequest` | `channels.ToggleJoinToSendRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `channels` | `ToggleParticipantsHiddenRequest` | `channels.ToggleParticipantsHiddenRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `channels` | `TogglePreHistoryHiddenRequest` | `channels.TogglePreHistoryHiddenRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `channels` | `ToggleSignaturesRequest` | `channels.ToggleSignaturesRequest` | `(self, channel: 'TypeInputChannel', signatures_enabled: Optional[bool] = None, profiles_enabled: Optional[bool] = None)` |
| `channels` | `ToggleSlowModeRequest` | `channels.ToggleSlowModeRequest` | `(self, channel: 'TypeInputChannel', seconds: int)` |
| `channels` | `ToggleUsernameRequest` | `channels.ToggleUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str, active: bool)` |
| `channels` | `ToggleViewForumAsMessagesRequest` | `channels.ToggleViewForumAsMessagesRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `channels` | `UpdateColorRequest` | `channels.UpdateColorRequest` | `(self, channel: 'TypeInputChannel', for_profile: Optional[bool] = None, color: Optional[int] = None, background_emoji_id: Optional[int] = None)` |
| `channels` | `UpdateEmojiStatusRequest` | `channels.UpdateEmojiStatusRequest` | `(self, channel: 'TypeInputChannel', emoji_status: 'TypeEmojiStatus')` |
| `channels` | `UpdatePaidMessagesPriceRequest` | `channels.UpdatePaidMessagesPriceRequest` | `(self, channel: 'TypeInputChannel', send_paid_messages_stars: int, broadcast_messages_allowed: Optional[bool] = None)` |
| `channels` | `UpdateUsernameRequest` | `channels.UpdateUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str)` |
| `chatlists` | `CheckChatlistInviteRequest` | `chatlists.CheckChatlistInviteRequest` | `(self, slug: str)` |
| `chatlists` | `DeleteExportedInviteRequest` | `chatlists.DeleteExportedInviteRequest` | `(self, chatlist: 'TypeInputChatlist', slug: str)` |
| `chatlists` | `EditExportedInviteRequest` | `chatlists.EditExportedInviteRequest` | `(self, chatlist: 'TypeInputChatlist', slug: str, title: Optional[str] = None, peers: Optional[List[ForwardRef('TypeInputPeer')]] = None)` |
| `chatlists` | `ExportChatlistInviteRequest` | `chatlists.ExportChatlistInviteRequest` | `(self, chatlist: 'TypeInputChatlist', title: str, peers: List[ForwardRef('TypeInputPeer')])` |
| `chatlists` | `GetChatlistUpdatesRequest` | `chatlists.GetChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `chatlists` | `GetExportedInvitesRequest` | `chatlists.GetExportedInvitesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `chatlists` | `GetLeaveChatlistSuggestionsRequest` | `chatlists.GetLeaveChatlistSuggestionsRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `chatlists` | `HideChatlistUpdatesRequest` | `chatlists.HideChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `chatlists` | `JoinChatlistInviteRequest` | `chatlists.JoinChatlistInviteRequest` | `(self, slug: str, peers: List[ForwardRef('TypeInputPeer')])` |
| `chatlists` | `JoinChatlistUpdatesRequest` | `chatlists.JoinChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist', peers: List[ForwardRef('TypeInputPeer')])` |
| `chatlists` | `LeaveChatlistRequest` | `chatlists.LeaveChatlistRequest` | `(self, chatlist: 'TypeInputChatlist', peers: List[ForwardRef('TypeInputPeer')])` |
| `contacts` | `AcceptContactRequest` | `contacts.AcceptContactRequest` | `(self, id: 'TypeInputUser')` |
| `contacts` | `AddContactRequest` | `contacts.AddContactRequest` | `(self, id: 'TypeInputUser', first_name: str, last_name: str, phone: str, add_phone_privacy_exception: Optional[bool] = None, note: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `contacts` | `BlockFromRepliesRequest` | `contacts.BlockFromRepliesRequest` | `(self, msg_id: int, delete_message: Optional[bool] = None, delete_history: Optional[bool] = None, report_spam: Optional[bool] = None)` |
| `contacts` | `BlockRequest` | `contacts.BlockRequest` | `(self, id: 'TypeInputPeer', my_stories_from: Optional[bool] = None)` |
| `contacts` | `DeleteByPhonesRequest` | `contacts.DeleteByPhonesRequest` | `(self, phones: List[str])` |
| `contacts` | `DeleteContactsRequest` | `contacts.DeleteContactsRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `contacts` | `EditCloseFriendsRequest` | `contacts.EditCloseFriendsRequest` | `(self, id: List[int])` |
| `contacts` | `ExportContactTokenRequest` | `contacts.ExportContactTokenRequest` | `(self, /, *args, **kwargs)` |
| `contacts` | `GetBirthdaysRequest` | `contacts.GetBirthdaysRequest` | `(self, /, *args, **kwargs)` |
| `contacts` | `GetBlockedRequest` | `contacts.GetBlockedRequest` | `(self, offset: int, limit: int, my_stories_from: Optional[bool] = None)` |
| `contacts` | `GetContactIDsRequest` | `contacts.GetContactIDsRequest` | `(self, hash: int)` |
| `contacts` | `GetContactsRequest` | `contacts.GetContactsRequest` | `(self, hash: int)` |
| `contacts` | `GetLocatedRequest` | `contacts.GetLocatedRequest` | `(self, geo_point: 'TypeInputGeoPoint', background: Optional[bool] = None, self_expires: Optional[int] = None)` |
| `contacts` | `GetSavedRequest` | `contacts.GetSavedRequest` | `(self, /, *args, **kwargs)` |
| `contacts` | `GetSponsoredPeersRequest` | `contacts.GetSponsoredPeersRequest` | `(self, q: str)` |
| `contacts` | `GetStatusesRequest` | `contacts.GetStatusesRequest` | `(self, /, *args, **kwargs)` |
| `contacts` | `GetTopPeersRequest` | `contacts.GetTopPeersRequest` | `(self, offset: int, limit: int, hash: int, correspondents: Optional[bool] = None, bots_pm: Optional[bool] = None, bots_inline: Optional[bool] = None, phone_calls: Optional[bool] = None, forward_users: Optional[bool] = None, forward_chats: Optional[bool] = None, groups: Optional[bool] = None, channels: Optional[bool] = None, bots_app: Optional[bool] = None, bots_guestchat: Optional[bool] = None)` |
| `contacts` | `ImportContactTokenRequest` | `contacts.ImportContactTokenRequest` | `(self, token: str)` |
| `contacts` | `ImportContactsRequest` | `contacts.ImportContactsRequest` | `(self, contacts: List[ForwardRef('TypeInputContact')])` |
| `contacts` | `ResetSavedRequest` | `contacts.ResetSavedRequest` | `(self, /, *args, **kwargs)` |
| `contacts` | `ResetTopPeerRatingRequest` | `contacts.ResetTopPeerRatingRequest` | `(self, category: 'TypeTopPeerCategory', peer: 'TypeInputPeer')` |
| `contacts` | `ResolvePhoneRequest` | `contacts.ResolvePhoneRequest` | `(self, phone: str)` |
| `contacts` | `ResolveUsernameRequest` | `contacts.ResolveUsernameRequest` | `(self, username: str, referer: Optional[str] = None)` |
| `contacts` | `SearchRequest` | `contacts.SearchRequest` | `(self, q: str, limit: int, broadcasts: Optional[bool] = None, bots: Optional[bool] = None)` |
| `contacts` | `SetBlockedRequest` | `contacts.SetBlockedRequest` | `(self, id: List[ForwardRef('TypeInputPeer')], limit: int, my_stories_from: Optional[bool] = None)` |
| `contacts` | `ToggleTopPeersRequest` | `contacts.ToggleTopPeersRequest` | `(self, enabled: bool)` |
| `contacts` | `UnblockRequest` | `contacts.UnblockRequest` | `(self, id: 'TypeInputPeer', my_stories_from: Optional[bool] = None)` |
| `contacts` | `UpdateContactNoteRequest` | `contacts.UpdateContactNoteRequest` | `(self, id: 'TypeInputUser', note: 'TypeTextWithEntities')` |
| `folders` | `EditPeerFoldersRequest` | `folders.EditPeerFoldersRequest` | `(self, folder_peers: List[ForwardRef('TypeInputFolderPeer')])` |
| `fragment` | `GetCollectibleInfoRequest` | `fragment.GetCollectibleInfoRequest` | `(self, collectible: 'TypeInputCollectible')` |
| `help` | `AcceptTermsOfServiceRequest` | `help.AcceptTermsOfServiceRequest` | `(self, id: 'TypeDataJSON')` |
| `help` | `DismissSuggestionRequest` | `help.DismissSuggestionRequest` | `(self, peer: 'TypeInputPeer', suggestion: str)` |
| `help` | `EditUserInfoRequest` | `help.EditUserInfoRequest` | `(self, user_id: 'TypeInputUser', message: str, entities: List[ForwardRef('TypeMessageEntity')])` |
| `help` | `GetAppConfigRequest` | `help.GetAppConfigRequest` | `(self, hash: int)` |
| `help` | `GetAppUpdateRequest` | `help.GetAppUpdateRequest` | `(self, source: str)` |
| `help` | `GetCdnConfigRequest` | `help.GetCdnConfigRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetConfigRequest` | `help.GetConfigRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetCountriesListRequest` | `help.GetCountriesListRequest` | `(self, lang_code: str, hash: int)` |
| `help` | `GetDeepLinkInfoRequest` | `help.GetDeepLinkInfoRequest` | `(self, path: str)` |
| `help` | `GetInviteTextRequest` | `help.GetInviteTextRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetNearestDcRequest` | `help.GetNearestDcRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetPassportConfigRequest` | `help.GetPassportConfigRequest` | `(self, hash: int)` |
| `help` | `GetPeerColorsRequest` | `help.GetPeerColorsRequest` | `(self, hash: int)` |
| `help` | `GetPeerProfileColorsRequest` | `help.GetPeerProfileColorsRequest` | `(self, hash: int)` |
| `help` | `GetPremiumPromoRequest` | `help.GetPremiumPromoRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetPromoDataRequest` | `help.GetPromoDataRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetRecentMeUrlsRequest` | `help.GetRecentMeUrlsRequest` | `(self, referer: str)` |
| `help` | `GetSupportNameRequest` | `help.GetSupportNameRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetSupportRequest` | `help.GetSupportRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetTermsOfServiceUpdateRequest` | `help.GetTermsOfServiceUpdateRequest` | `(self, /, *args, **kwargs)` |
| `help` | `GetTimezonesListRequest` | `help.GetTimezonesListRequest` | `(self, hash: int)` |
| `help` | `GetUserInfoRequest` | `help.GetUserInfoRequest` | `(self, user_id: 'TypeInputUser')` |
| `help` | `HidePromoDataRequest` | `help.HidePromoDataRequest` | `(self, peer: 'TypeInputPeer')` |
| `help` | `SaveAppLogRequest` | `help.SaveAppLogRequest` | `(self, events: List[ForwardRef('TypeInputAppEvent')])` |
| `help` | `SetBotUpdatesStatusRequest` | `help.SetBotUpdatesStatusRequest` | `(self, pending_updates_count: int, message: str)` |
| `langpack` | `GetDifferenceRequest` | `langpack.GetDifferenceRequest` | `(self, lang_pack: str, lang_code: str, from_version: int)` |
| `langpack` | `GetLangPackRequest` | `langpack.GetLangPackRequest` | `(self, lang_pack: str, lang_code: str)` |
| `langpack` | `GetLanguageRequest` | `langpack.GetLanguageRequest` | `(self, lang_pack: str, lang_code: str)` |
| `langpack` | `GetLanguagesRequest` | `langpack.GetLanguagesRequest` | `(self, lang_pack: str)` |
| `langpack` | `GetStringsRequest` | `langpack.GetStringsRequest` | `(self, lang_pack: str, lang_code: str, keys: List[str])` |
| `messages` | `AcceptEncryptionRequest` | `messages.AcceptEncryptionRequest` | `(self, peer: 'TypeInputEncryptedChat', g_b: bytes, key_fingerprint: int)` |
| `messages` | `AcceptUrlAuthRequest` | `messages.AcceptUrlAuthRequest` | `(self, write_allowed: Optional[bool] = None, share_phone_number: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None, match_code: Optional[str] = None)` |
| `messages` | `AddChatUserRequest` | `messages.AddChatUserRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', fwd_limit: int)` |
| `messages` | `AddPollAnswerRequest` | `messages.AddPollAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, answer: 'TypePollAnswer')` |
| `messages` | `AppendTodoListRequest` | `messages.AppendTodoListRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, list: List[ForwardRef('TypeTodoItem')])` |
| `messages` | `CheckChatInviteRequest` | `messages.CheckChatInviteRequest` | `(self, hash: str)` |
| `messages` | `CheckHistoryImportPeerRequest` | `messages.CheckHistoryImportPeerRequest` | `(self, peer: 'TypeInputPeer')` |
| `messages` | `CheckHistoryImportRequest` | `messages.CheckHistoryImportRequest` | `(self, import_head: str)` |
| `messages` | `CheckQuickReplyShortcutRequest` | `messages.CheckQuickReplyShortcutRequest` | `(self, shortcut: str)` |
| `messages` | `CheckUrlAuthMatchCodeRequest` | `messages.CheckUrlAuthMatchCodeRequest` | `(self, url: str, match_code: str)` |
| `messages` | `ClearAllDraftsRequest` | `messages.ClearAllDraftsRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `ClearRecentReactionsRequest` | `messages.ClearRecentReactionsRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `ClearRecentStickersRequest` | `messages.ClearRecentStickersRequest` | `(self, attached: Optional[bool] = None)` |
| `messages` | `ClickSponsoredMessageRequest` | `messages.ClickSponsoredMessageRequest` | `(self, media: Optional[bool] = None, fullscreen: Optional[bool] = None, random_id: bytes = None)` |
| `messages` | `ComposeMessageWithAIRequest` | `messages.ComposeMessageWithAIRequest` | `(self, text: 'TypeTextWithEntities', proofread: Optional[bool] = None, emojify: Optional[bool] = None, translate_to_lang: Optional[str] = None, tone: Optional[ForwardRef('TypeInputAiComposeTone')] = None)` |
| `messages` | `CreateChatRequest` | `messages.CreateChatRequest` | `(self, users: List[ForwardRef('TypeInputUser')], title: str, ttl_period: Optional[int] = None)` |
| `messages` | `CreateForumTopicRequest` | `messages.CreateForumTopicRequest` | `(self, peer: 'TypeInputPeer', title: str, title_missing: Optional[bool] = None, icon_color: Optional[int] = None, icon_emoji_id: Optional[int] = None, random_id: int = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `DeclineUrlAuthRequest` | `messages.DeclineUrlAuthRequest` | `(self, url: str)` |
| `messages` | `DeleteChatRequest` | `messages.DeleteChatRequest` | `(self, chat_id: int)` |
| `messages` | `DeleteChatUserRequest` | `messages.DeleteChatUserRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', revoke_history: Optional[bool] = None)` |
| `messages` | `DeleteExportedChatInviteRequest` | `messages.DeleteExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str)` |
| `messages` | `DeleteFactCheckRequest` | `messages.DeleteFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `messages` | `DeleteHistoryRequest` | `messages.DeleteHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int, just_clear: Optional[bool] = None, revoke: Optional[bool] = None, min_date: Optional[datetime.datetime] = None, max_date: Optional[datetime.datetime] = None)` |
| `messages` | `DeleteMessagesRequest` | `messages.DeleteMessagesRequest` | `(self, id: List[int], revoke: Optional[bool] = None)` |
| `messages` | `DeleteParticipantReactionRequest` | `messages.DeleteParticipantReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, participant: 'TypeInputPeer')` |
| `messages` | `DeleteParticipantReactionsRequest` | `messages.DeleteParticipantReactionsRequest` | `(self, peer: 'TypeInputPeer', participant: 'TypeInputPeer')` |
| `messages` | `DeletePhoneCallHistoryRequest` | `messages.DeletePhoneCallHistoryRequest` | `(self, revoke: Optional[bool] = None)` |
| `messages` | `DeletePollAnswerRequest` | `messages.DeletePollAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, option: bytes)` |
| `messages` | `DeleteQuickReplyMessagesRequest` | `messages.DeleteQuickReplyMessagesRequest` | `(self, shortcut_id: int, id: List[int])` |
| `messages` | `DeleteQuickReplyShortcutRequest` | `messages.DeleteQuickReplyShortcutRequest` | `(self, shortcut_id: int)` |
| `messages` | `DeleteRevokedExportedChatInvitesRequest` | `messages.DeleteRevokedExportedChatInvitesRequest` | `(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser')` |
| `messages` | `DeleteSavedHistoryRequest` | `messages.DeleteSavedHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None, min_date: Optional[datetime.datetime] = None, max_date: Optional[datetime.datetime] = None)` |
| `messages` | `DeleteScheduledMessagesRequest` | `messages.DeleteScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `messages` | `DeleteTopicHistoryRequest` | `messages.DeleteTopicHistoryRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: int)` |
| `messages` | `DiscardEncryptionRequest` | `messages.DiscardEncryptionRequest` | `(self, chat_id: int, delete_history: Optional[bool] = None)` |
| `messages` | `EditChatAboutRequest` | `messages.EditChatAboutRequest` | `(self, peer: 'TypeInputPeer', about: str)` |
| `messages` | `EditChatAdminRequest` | `messages.EditChatAdminRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', is_admin: bool)` |
| `messages` | `EditChatCreatorRequest` | `messages.EditChatCreatorRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser', password: 'TypeInputCheckPasswordSRP')` |
| `messages` | `EditChatDefaultBannedRightsRequest` | `messages.EditChatDefaultBannedRightsRequest` | `(self, peer: 'TypeInputPeer', banned_rights: 'TypeChatBannedRights')` |
| `messages` | `EditChatParticipantRankRequest` | `messages.EditChatParticipantRankRequest` | `(self, peer: 'TypeInputPeer', participant: 'TypeInputPeer', rank: str)` |
| `messages` | `EditChatPhotoRequest` | `messages.EditChatPhotoRequest` | `(self, chat_id: int, photo: 'TypeInputChatPhoto')` |
| `messages` | `EditChatTitleRequest` | `messages.EditChatTitleRequest` | `(self, chat_id: int, title: str)` |
| `messages` | `EditExportedChatInviteRequest` | `messages.EditExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str, revoked: Optional[bool] = None, expire_date: Optional[datetime.datetime] = None, usage_limit: Optional[int] = None, request_needed: Optional[bool] = None, title: Optional[str] = None)` |
| `messages` | `EditFactCheckRequest` | `messages.EditFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, text: 'TypeTextWithEntities')` |
| `messages` | `EditForumTopicRequest` | `messages.EditForumTopicRequest` | `(self, peer: 'TypeInputPeer', topic_id: int, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None)` |
| `messages` | `EditInlineBotMessageRequest` | `messages.EditInlineBotMessageRequest` | `(self, id: 'TypeInputBotInlineMessageID', no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `messages` | `EditMessageRequest` | `messages.EditMessageRequest` | `(self, peer: 'TypeInputPeer', id: int, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, quick_reply_shortcut_id: Optional[int] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `messages` | `EditQuickReplyShortcutRequest` | `messages.EditQuickReplyShortcutRequest` | `(self, shortcut_id: int, shortcut: str)` |
| `messages` | `ExportChatInviteRequest` | `messages.ExportChatInviteRequest` | `(self, peer: 'TypeInputPeer', legacy_revoke_permanent: Optional[bool] = None, request_needed: Optional[bool] = None, expire_date: Optional[datetime.datetime] = None, usage_limit: Optional[int] = None, title: Optional[str] = None, subscription_pricing: Optional[ForwardRef('TypeStarsSubscriptionPricing')] = None)` |
| `messages` | `FaveStickerRequest` | `messages.FaveStickerRequest` | `(self, id: 'TypeInputDocument', unfave: bool)` |
| `messages` | `ForwardMessagesRequest` | `messages.ForwardMessagesRequest` | `(self, from_peer: 'TypeInputPeer', id: List[int], to_peer: 'TypeInputPeer', silent: Optional[bool] = None, background: Optional[bool] = None, with_my_score: Optional[bool] = None, drop_author: Optional[bool] = None, drop_media_captions: Optional[bool] = None, noforwards: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, random_id: List[int] = None, top_msg_id: Optional[int] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, video_timestamp: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None)` |
| `messages` | `GetAdminsWithInvitesRequest` | `messages.GetAdminsWithInvitesRequest` | `(self, peer: 'TypeInputPeer')` |
| `messages` | `GetAllDraftsRequest` | `messages.GetAllDraftsRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetAllStickersRequest` | `messages.GetAllStickersRequest` | `(self, hash: int)` |
| `messages` | `GetArchivedStickersRequest` | `messages.GetArchivedStickersRequest` | `(self, offset_id: int, limit: int, masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `messages` | `GetAttachMenuBotRequest` | `messages.GetAttachMenuBotRequest` | `(self, bot: 'TypeInputUser')` |
| `messages` | `GetAttachMenuBotsRequest` | `messages.GetAttachMenuBotsRequest` | `(self, hash: int)` |
| `messages` | `GetAttachedStickersRequest` | `messages.GetAttachedStickersRequest` | `(self, media: 'TypeInputStickeredMedia')` |
| `messages` | `GetAvailableEffectsRequest` | `messages.GetAvailableEffectsRequest` | `(self, hash: int)` |
| `messages` | `GetAvailableReactionsRequest` | `messages.GetAvailableReactionsRequest` | `(self, hash: int)` |
| `messages` | `GetBotAppRequest` | `messages.GetBotAppRequest` | `(self, app: 'TypeInputBotApp', hash: int)` |
| `messages` | `GetBotCallbackAnswerRequest` | `messages.GetBotCallbackAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, game: Optional[bool] = None, data: Optional[bytes] = None, password: Optional[ForwardRef('TypeInputCheckPasswordSRP')] = None)` |
| `messages` | `GetChatInviteImportersRequest` | `messages.GetChatInviteImportersRequest` | `(self, peer: 'TypeInputPeer', offset_date: Optional[datetime.datetime], offset_user: 'TypeInputUser', limit: int, requested: Optional[bool] = None, subscription_expired: Optional[bool] = None, link: Optional[str] = None, q: Optional[str] = None)` |
| `messages` | `GetChatsRequest` | `messages.GetChatsRequest` | `(self, id: List[int])` |
| `messages` | `GetCommonChatsRequest` | `messages.GetCommonChatsRequest` | `(self, user_id: 'TypeInputUser', max_id: int, limit: int)` |
| `messages` | `GetCustomEmojiDocumentsRequest` | `messages.GetCustomEmojiDocumentsRequest` | `(self, document_id: List[int])` |
| `messages` | `GetDefaultHistoryTTLRequest` | `messages.GetDefaultHistoryTTLRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetDefaultTagReactionsRequest` | `messages.GetDefaultTagReactionsRequest` | `(self, hash: int)` |
| `messages` | `GetDhConfigRequest` | `messages.GetDhConfigRequest` | `(self, version: int, random_length: int)` |
| `messages` | `GetDialogFiltersRequest` | `messages.GetDialogFiltersRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetDialogUnreadMarksRequest` | `messages.GetDialogUnreadMarksRequest` | `(self, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetDialogsRequest` | `messages.GetDialogsRequest` | `(self, offset_date: Optional[datetime.datetime], offset_id: int, offset_peer: 'TypeInputPeer', limit: int, hash: int, exclude_pinned: Optional[bool] = None, folder_id: Optional[int] = None)` |
| `messages` | `GetDiscussionMessageRequest` | `messages.GetDiscussionMessageRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `messages` | `GetDocumentByHashRequest` | `messages.GetDocumentByHashRequest` | `(self, sha256: bytes, size: int, mime_type: str)` |
| `messages` | `GetEmojiGameInfoRequest` | `messages.GetEmojiGameInfoRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetEmojiGroupsRequest` | `messages.GetEmojiGroupsRequest` | `(self, hash: int)` |
| `messages` | `GetEmojiKeywordsDifferenceRequest` | `messages.GetEmojiKeywordsDifferenceRequest` | `(self, lang_code: str, from_version: int)` |
| `messages` | `GetEmojiKeywordsLanguagesRequest` | `messages.GetEmojiKeywordsLanguagesRequest` | `(self, lang_codes: List[str])` |
| `messages` | `GetEmojiKeywordsRequest` | `messages.GetEmojiKeywordsRequest` | `(self, lang_code: str)` |
| `messages` | `GetEmojiProfilePhotoGroupsRequest` | `messages.GetEmojiProfilePhotoGroupsRequest` | `(self, hash: int)` |
| `messages` | `GetEmojiStatusGroupsRequest` | `messages.GetEmojiStatusGroupsRequest` | `(self, hash: int)` |
| `messages` | `GetEmojiStickerGroupsRequest` | `messages.GetEmojiStickerGroupsRequest` | `(self, hash: int)` |
| `messages` | `GetEmojiStickersRequest` | `messages.GetEmojiStickersRequest` | `(self, hash: int)` |
| `messages` | `GetEmojiURLRequest` | `messages.GetEmojiURLRequest` | `(self, lang_code: str)` |
| `messages` | `GetExportedChatInviteRequest` | `messages.GetExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str)` |
| `messages` | `GetExportedChatInvitesRequest` | `messages.GetExportedChatInvitesRequest` | `(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser', limit: int, revoked: Optional[bool] = None, offset_date: Optional[datetime.datetime] = None, offset_link: Optional[str] = None)` |
| `messages` | `GetExtendedMediaRequest` | `messages.GetExtendedMediaRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `messages` | `GetFactCheckRequest` | `messages.GetFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: List[int])` |
| `messages` | `GetFavedStickersRequest` | `messages.GetFavedStickersRequest` | `(self, hash: int)` |
| `messages` | `GetFeaturedEmojiStickersRequest` | `messages.GetFeaturedEmojiStickersRequest` | `(self, hash: int)` |
| `messages` | `GetFeaturedStickersRequest` | `messages.GetFeaturedStickersRequest` | `(self, hash: int)` |
| `messages` | `GetForumTopicsByIDRequest` | `messages.GetForumTopicsByIDRequest` | `(self, peer: 'TypeInputPeer', topics: List[int])` |
| `messages` | `GetForumTopicsRequest` | `messages.GetForumTopicsRequest` | `(self, peer: 'TypeInputPeer', offset_date: Optional[datetime.datetime], offset_id: int, offset_topic: int, limit: int, q: Optional[str] = None)` |
| `messages` | `GetFullChatRequest` | `messages.GetFullChatRequest` | `(self, chat_id: int)` |
| `messages` | `GetFutureChatCreatorAfterLeaveRequest` | `messages.GetFutureChatCreatorAfterLeaveRequest` | `(self, peer: 'TypeInputPeer')` |
| `messages` | `GetGameHighScoresRequest` | `messages.GetGameHighScoresRequest` | `(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser')` |
| `messages` | `GetHistoryRequest` | `messages.GetHistoryRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int)` |
| `messages` | `GetInlineBotResultsRequest` | `messages.GetInlineBotResultsRequest` | `(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', query: str, offset: str, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None)` |
| `messages` | `GetInlineGameHighScoresRequest` | `messages.GetInlineGameHighScoresRequest` | `(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser')` |
| `messages` | `GetMaskStickersRequest` | `messages.GetMaskStickersRequest` | `(self, hash: int)` |
| `messages` | `GetMessageEditDataRequest` | `messages.GetMessageEditDataRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `messages` | `GetMessageReactionsListRequest` | `messages.GetMessageReactionsListRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, reaction: Optional[ForwardRef('TypeReaction')] = None, offset: Optional[str] = None)` |
| `messages` | `GetMessageReadParticipantsRequest` | `messages.GetMessageReadParticipantsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `messages` | `GetMessagesReactionsRequest` | `messages.GetMessagesReactionsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `messages` | `GetMessagesRequest` | `messages.GetMessagesRequest` | `(self, id: List[ForwardRef('TypeInputMessage')])` |
| `messages` | `GetMessagesViewsRequest` | `messages.GetMessagesViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int], increment: bool)` |
| `messages` | `GetMyStickersRequest` | `messages.GetMyStickersRequest` | `(self, offset_id: int, limit: int)` |
| `messages` | `GetOldFeaturedStickersRequest` | `messages.GetOldFeaturedStickersRequest` | `(self, offset: int, limit: int, hash: int)` |
| `messages` | `GetOnlinesRequest` | `messages.GetOnlinesRequest` | `(self, peer: 'TypeInputPeer')` |
| `messages` | `GetOutboxReadDateRequest` | `messages.GetOutboxReadDateRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `messages` | `GetPaidReactionPrivacyRequest` | `messages.GetPaidReactionPrivacyRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetPeerDialogsRequest` | `messages.GetPeerDialogsRequest` | `(self, peers: List[ForwardRef('TypeInputDialogPeer')])` |
| `messages` | `GetPeerSettingsRequest` | `messages.GetPeerSettingsRequest` | `(self, peer: 'TypeInputPeer')` |
| `messages` | `GetPersonalChannelHistoryRequest` | `messages.GetPersonalChannelHistoryRequest` | `(self, user_id: 'TypeInputUser', limit: int, max_id: int, min_id: int, hash: int)` |
| `messages` | `GetPinnedDialogsRequest` | `messages.GetPinnedDialogsRequest` | `(self, folder_id: int)` |
| `messages` | `GetPinnedSavedDialogsRequest` | `messages.GetPinnedSavedDialogsRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetPollResultsRequest` | `messages.GetPollResultsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, poll_hash: int)` |
| `messages` | `GetPollVotesRequest` | `messages.GetPollVotesRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, option: Optional[bytes] = None, offset: Optional[str] = None)` |
| `messages` | `GetPreparedInlineMessageRequest` | `messages.GetPreparedInlineMessageRequest` | `(self, bot: 'TypeInputUser', id: str)` |
| `messages` | `GetQuickRepliesRequest` | `messages.GetQuickRepliesRequest` | `(self, hash: int)` |
| `messages` | `GetQuickReplyMessagesRequest` | `messages.GetQuickReplyMessagesRequest` | `(self, shortcut_id: int, hash: int, id: Optional[List[int]] = None)` |
| `messages` | `GetRecentLocationsRequest` | `messages.GetRecentLocationsRequest` | `(self, peer: 'TypeInputPeer', limit: int, hash: int)` |
| `messages` | `GetRecentReactionsRequest` | `messages.GetRecentReactionsRequest` | `(self, limit: int, hash: int)` |
| `messages` | `GetRecentStickersRequest` | `messages.GetRecentStickersRequest` | `(self, hash: int, attached: Optional[bool] = None)` |
| `messages` | `GetRepliesRequest` | `messages.GetRepliesRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int)` |
| `messages` | `GetRichMessageRequest` | `messages.GetRichMessageRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `messages` | `GetSavedDialogsByIDRequest` | `messages.GetSavedDialogsByIDRequest` | `(self, ids: List[ForwardRef('TypeInputPeer')], parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetSavedDialogsRequest` | `messages.GetSavedDialogsRequest` | `(self, offset_date: Optional[datetime.datetime], offset_id: int, offset_peer: 'TypeInputPeer', limit: int, hash: int, exclude_pinned: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetSavedGifsRequest` | `messages.GetSavedGifsRequest` | `(self, hash: int)` |
| `messages` | `GetSavedHistoryRequest` | `messages.GetSavedHistoryRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetSavedReactionTagsRequest` | `messages.GetSavedReactionTagsRequest` | `(self, hash: int, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetScheduledHistoryRequest` | `messages.GetScheduledHistoryRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `messages` | `GetScheduledMessagesRequest` | `messages.GetScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `messages` | `GetSearchCountersRequest` | `messages.GetSearchCountersRequest` | `(self, peer: 'TypeInputPeer', filters: List[ForwardRef('TypeMessagesFilter')], saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, top_msg_id: Optional[int] = None)` |
| `messages` | `GetSearchResultsCalendarRequest` | `messages.GetSearchResultsCalendarRequest` | `(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, offset_date: Optional[datetime.datetime], saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetSearchResultsPositionsRequest` | `messages.GetSearchResultsPositionsRequest` | `(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, limit: int, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetSplitRangesRequest` | `messages.GetSplitRangesRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetSponsoredMessagesRequest` | `messages.GetSponsoredMessagesRequest` | `(self, peer: 'TypeInputPeer', msg_id: Optional[int] = None)` |
| `messages` | `GetStickerSetRequest` | `messages.GetStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', hash: int)` |
| `messages` | `GetStickersRequest` | `messages.GetStickersRequest` | `(self, emoticon: str, hash: int)` |
| `messages` | `GetSuggestedDialogFiltersRequest` | `messages.GetSuggestedDialogFiltersRequest` | `(self, /, *args, **kwargs)` |
| `messages` | `GetTopReactionsRequest` | `messages.GetTopReactionsRequest` | `(self, limit: int, hash: int)` |
| `messages` | `GetUnreadMentionsRequest` | `messages.GetUnreadMentionsRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None)` |
| `messages` | `GetUnreadPollVotesRequest` | `messages.GetUnreadPollVotesRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None)` |
| `messages` | `GetUnreadReactionsRequest` | `messages.GetUnreadReactionsRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `GetWebPagePreviewRequest` | `messages.GetWebPagePreviewRequest` | `(self, message: str, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None)` |
| `messages` | `GetWebPageRequest` | `messages.GetWebPageRequest` | `(self, url: str, hash: int)` |
| `messages` | `HideAllChatJoinRequestsRequest` | `messages.HideAllChatJoinRequestsRequest` | `(self, peer: 'TypeInputPeer', approved: Optional[bool] = None, link: Optional[str] = None)` |
| `messages` | `HideChatJoinRequestRequest` | `messages.HideChatJoinRequestRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser', approved: Optional[bool] = None)` |
| `messages` | `HidePeerSettingsBarRequest` | `messages.HidePeerSettingsBarRequest` | `(self, peer: 'TypeInputPeer')` |
| `messages` | `ImportChatInviteRequest` | `messages.ImportChatInviteRequest` | `(self, hash: str)` |
| `messages` | `InitHistoryImportRequest` | `messages.InitHistoryImportRequest` | `(self, peer: 'TypeInputPeer', file: 'TypeInputFile', media_count: int)` |
| `messages` | `InstallStickerSetRequest` | `messages.InstallStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', archived: bool)` |
| `messages` | `MarkDialogUnreadRequest` | `messages.MarkDialogUnreadRequest` | `(self, peer: 'TypeInputDialogPeer', unread: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `MigrateChatRequest` | `messages.MigrateChatRequest` | `(self, chat_id: int)` |
| `messages` | `ProlongWebViewRequest` | `messages.ProlongWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', query_id: int, silent: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `RateTranscribedAudioRequest` | `messages.RateTranscribedAudioRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, transcription_id: int, good: bool)` |
| `messages` | `ReadDiscussionRequest` | `messages.ReadDiscussionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, read_max_id: int)` |
| `messages` | `ReadEncryptedHistoryRequest` | `messages.ReadEncryptedHistoryRequest` | `(self, peer: 'TypeInputEncryptedChat', max_date: Optional[datetime.datetime])` |
| `messages` | `ReadFeaturedStickersRequest` | `messages.ReadFeaturedStickersRequest` | `(self, id: List[int])` |
| `messages` | `ReadHistoryRequest` | `messages.ReadHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int)` |
| `messages` | `ReadMentionsRequest` | `messages.ReadMentionsRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None)` |
| `messages` | `ReadMessageContentsRequest` | `messages.ReadMessageContentsRequest` | `(self, id: List[int])` |
| `messages` | `ReadPollVotesRequest` | `messages.ReadPollVotesRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None)` |
| `messages` | `ReadReactionsRequest` | `messages.ReadReactionsRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `ReadSavedHistoryRequest` | `messages.ReadSavedHistoryRequest` | `(self, parent_peer: 'TypeInputPeer', peer: 'TypeInputPeer', max_id: int)` |
| `messages` | `ReceivedMessagesRequest` | `messages.ReceivedMessagesRequest` | `(self, max_id: int)` |
| `messages` | `ReceivedQueueRequest` | `messages.ReceivedQueueRequest` | `(self, max_qts: int)` |
| `messages` | `ReorderPinnedDialogsRequest` | `messages.ReorderPinnedDialogsRequest` | `(self, folder_id: int, order: List[ForwardRef('TypeInputDialogPeer')], force: Optional[bool] = None)` |
| `messages` | `ReorderPinnedForumTopicsRequest` | `messages.ReorderPinnedForumTopicsRequest` | `(self, peer: 'TypeInputPeer', order: List[int], force: Optional[bool] = None)` |
| `messages` | `ReorderPinnedSavedDialogsRequest` | `messages.ReorderPinnedSavedDialogsRequest` | `(self, order: List[ForwardRef('TypeInputDialogPeer')], force: Optional[bool] = None)` |
| `messages` | `ReorderQuickRepliesRequest` | `messages.ReorderQuickRepliesRequest` | `(self, order: List[int])` |
| `messages` | `ReorderStickerSetsRequest` | `messages.ReorderStickerSetsRequest` | `(self, order: List[int], masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `messages` | `ReportEncryptedSpamRequest` | `messages.ReportEncryptedSpamRequest` | `(self, peer: 'TypeInputEncryptedChat')` |
| `messages` | `ReportMessagesDeliveryRequest` | `messages.ReportMessagesDeliveryRequest` | `(self, peer: 'TypeInputPeer', id: List[int], push: Optional[bool] = None)` |
| `messages` | `ReportMusicListenRequest` | `messages.ReportMusicListenRequest` | `(self, id: 'TypeInputDocument', listened_duration: int)` |
| `messages` | `ReportReactionRequest` | `messages.ReportReactionRequest` | `(self, peer: 'TypeInputPeer', id: int, reaction_peer: 'TypeInputPeer')` |
| `messages` | `ReportReadMetricsRequest` | `messages.ReportReadMetricsRequest` | `(self, peer: 'TypeInputPeer', metrics: List[ForwardRef('TypeInputMessageReadMetric')])` |
| `messages` | `ReportRequest` | `messages.ReportRequest` | `(self, peer: 'TypeInputPeer', id: List[int], option: bytes, message: str)` |
| `messages` | `ReportSpamRequest` | `messages.ReportSpamRequest` | `(self, peer: 'TypeInputPeer')` |
| `messages` | `ReportSponsoredMessageRequest` | `messages.ReportSponsoredMessageRequest` | `(self, option: bytes, random_id: bytes = None)` |
| `messages` | `RequestAppWebViewRequest` | `messages.RequestAppWebViewRequest` | `(self, peer: 'TypeInputPeer', app: 'TypeInputBotApp', platform: str, write_allowed: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `messages` | `RequestEncryptionRequest` | `messages.RequestEncryptionRequest` | `(self, user_id: 'TypeInputUser', g_a: bytes, random_id: int = None)` |
| `messages` | `RequestMainWebViewRequest` | `messages.RequestMainWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', platform: str, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `messages` | `RequestSimpleWebViewRequest` | `messages.RequestSimpleWebViewRequest` | `(self, bot: 'TypeInputUser', platform: str, from_switch_webview: Optional[bool] = None, from_side_menu: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `messages` | `RequestUrlAuthRequest` | `messages.RequestUrlAuthRequest` | `(self, peer: Optional[ForwardRef('TypeInputPeer')] = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None, in_app_origin: Optional[str] = None)` |
| `messages` | `RequestWebViewRequest` | `messages.RequestWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', platform: str, from_bot_menu: Optional[bool] = None, silent: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `SaveDefaultSendAsRequest` | `messages.SaveDefaultSendAsRequest` | `(self, peer: 'TypeInputPeer', send_as: 'TypeInputPeer')` |
| `messages` | `SaveDraftRequest` | `messages.SaveDraftRequest` | `(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, effect: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `messages` | `SaveGifRequest` | `messages.SaveGifRequest` | `(self, id: 'TypeInputDocument', unsave: bool)` |
| `messages` | `SavePreparedInlineMessageRequest` | `messages.SavePreparedInlineMessageRequest` | `(self, result: 'TypeInputBotInlineResult', user_id: 'TypeInputUser', peer_types: Optional[List[ForwardRef('TypeInlineQueryPeerType')]] = None)` |
| `messages` | `SaveRecentStickerRequest` | `messages.SaveRecentStickerRequest` | `(self, id: 'TypeInputDocument', unsave: bool, attached: Optional[bool] = None)` |
| `messages` | `SearchCustomEmojiRequest` | `messages.SearchCustomEmojiRequest` | `(self, emoticon: str, hash: int)` |
| `messages` | `SearchEmojiStickerSetsRequest` | `messages.SearchEmojiStickerSetsRequest` | `(self, q: str, hash: int, exclude_featured: Optional[bool] = None)` |
| `messages` | `SearchGlobalRequest` | `messages.SearchGlobalRequest` | `(self, q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime], offset_rate: int, offset_peer: 'TypeInputPeer', offset_id: int, limit: int, broadcasts_only: Optional[bool] = None, groups_only: Optional[bool] = None, users_only: Optional[bool] = None, folder_id: Optional[int] = None)` |
| `messages` | `SearchRequest` | `messages.SearchRequest` | `(self, peer: 'TypeInputPeer', q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime], offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, from_id: Optional[ForwardRef('TypeInputPeer')] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, saved_reaction: Optional[List[ForwardRef('TypeReaction')]] = None, top_msg_id: Optional[int] = None)` |
| `messages` | `SearchSentMediaRequest` | `messages.SearchSentMediaRequest` | `(self, q: str, filter: 'TypeMessagesFilter', limit: int)` |
| `messages` | `SearchStickerSetsRequest` | `messages.SearchStickerSetsRequest` | `(self, q: str, hash: int, exclude_featured: Optional[bool] = None)` |
| `messages` | `SearchStickersRequest` | `messages.SearchStickersRequest` | `(self, q: str, emoticon: str, lang_code: List[str], offset: int, limit: int, hash: int, emojis: Optional[bool] = None)` |
| `messages` | `SendBotRequestedPeerRequest` | `messages.SendBotRequestedPeerRequest` | `(self, peer: 'TypeInputPeer', button_id: int, requested_peers: List[ForwardRef('TypeInputPeer')], msg_id: Optional[int] = None, webapp_req_id: Optional[str] = None)` |
| `messages` | `SendEncryptedFileRequest` | `messages.SendEncryptedFileRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, file: 'TypeInputEncryptedFile', silent: Optional[bool] = None, random_id: int = None)` |
| `messages` | `SendEncryptedRequest` | `messages.SendEncryptedRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, silent: Optional[bool] = None, random_id: int = None)` |
| `messages` | `SendEncryptedServiceRequest` | `messages.SendEncryptedServiceRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, random_id: int = None)` |
| `messages` | `SendInlineBotResultRequest` | `messages.SendInlineBotResultRequest` | `(self, peer: 'TypeInputPeer', query_id: int, id: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, hide_via: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, schedule_date: Optional[datetime.datetime] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, allow_paid_stars: Optional[int] = None)` |
| `messages` | `SendMediaRequest` | `messages.SendMediaRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', message: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None)` |
| `messages` | `SendMessageRequest` | `messages.SendMessageRequest` | `(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool] = None, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `messages` | `SendMultiMediaRequest` | `messages.SendMultiMediaRequest` | `(self, peer: 'TypeInputPeer', multi_media: List[ForwardRef('TypeInputSingleMedia')], silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, schedule_date: Optional[datetime.datetime] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None)` |
| `messages` | `SendPaidReactionRequest` | `messages.SendPaidReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, count: int, random_id: int = None, private: Optional[ForwardRef('TypePaidReactionPrivacy')] = None)` |
| `messages` | `SendQuickReplyMessagesRequest` | `messages.SendQuickReplyMessagesRequest` | `(self, peer: 'TypeInputPeer', shortcut_id: int, id: List[int], random_id: List[int] = None)` |
| `messages` | `SendReactionRequest` | `messages.SendReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, big: Optional[bool] = None, add_to_recent: Optional[bool] = None, reaction: Optional[List[ForwardRef('TypeReaction')]] = None)` |
| `messages` | `SendScheduledMessagesRequest` | `messages.SendScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `messages` | `SendScreenshotNotificationRequest` | `messages.SendScreenshotNotificationRequest` | `(self, peer: 'TypeInputPeer', reply_to: 'TypeInputReplyTo', random_id: int = None)` |
| `messages` | `SendVoteRequest` | `messages.SendVoteRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, options: List[bytes])` |
| `messages` | `SendWebViewDataRequest` | `messages.SendWebViewDataRequest` | `(self, bot: 'TypeInputUser', button_text: str, data: str, random_id: int = None)` |
| `messages` | `SendWebViewResultMessageRequest` | `messages.SendWebViewResultMessageRequest` | `(self, bot_query_id: str, result: 'TypeInputBotInlineResult')` |
| `messages` | `SetBotCallbackAnswerRequest` | `messages.SetBotCallbackAnswerRequest` | `(self, query_id: int, cache_time: int, alert: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None)` |
| `messages` | `SetBotGuestChatResultRequest` | `messages.SetBotGuestChatResultRequest` | `(self, query_id: int, result: 'TypeInputBotInlineResult')` |
| `messages` | `SetBotPrecheckoutResultsRequest` | `messages.SetBotPrecheckoutResultsRequest` | `(self, query_id: int, success: Optional[bool] = None, error: Optional[str] = None)` |
| `messages` | `SetBotShippingResultsRequest` | `messages.SetBotShippingResultsRequest` | `(self, query_id: int, error: Optional[str] = None, shipping_options: Optional[List[ForwardRef('TypeShippingOption')]] = None)` |
| `messages` | `SetChatAvailableReactionsRequest` | `messages.SetChatAvailableReactionsRequest` | `(self, peer: 'TypeInputPeer', available_reactions: 'TypeChatReactions', reactions_limit: Optional[int] = None, paid_enabled: Optional[bool] = None)` |
| `messages` | `SetChatThemeRequest` | `messages.SetChatThemeRequest` | `(self, peer: 'TypeInputPeer', theme: 'TypeInputChatTheme')` |
| `messages` | `SetChatWallPaperRequest` | `messages.SetChatWallPaperRequest` | `(self, peer: 'TypeInputPeer', for_both: Optional[bool] = None, revert: Optional[bool] = None, wallpaper: Optional[ForwardRef('TypeInputWallPaper')] = None, settings: Optional[ForwardRef('TypeWallPaperSettings')] = None, id: Optional[int] = None)` |
| `messages` | `SetDefaultHistoryTTLRequest` | `messages.SetDefaultHistoryTTLRequest` | `(self, period: int)` |
| `messages` | `SetDefaultReactionRequest` | `messages.SetDefaultReactionRequest` | `(self, reaction: 'TypeReaction')` |
| `messages` | `SetEncryptedTypingRequest` | `messages.SetEncryptedTypingRequest` | `(self, peer: 'TypeInputEncryptedChat', typing: bool)` |
| `messages` | `SetGameScoreRequest` | `messages.SetGameScoreRequest` | `(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser', score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None)` |
| `messages` | `SetHistoryTTLRequest` | `messages.SetHistoryTTLRequest` | `(self, peer: 'TypeInputPeer', period: int)` |
| `messages` | `SetInlineBotResultsRequest` | `messages.SetInlineBotResultsRequest` | `(self, query_id: int, results: List[ForwardRef('TypeInputBotInlineResult')], cache_time: int, gallery: Optional[bool] = None, private: Optional[bool] = None, next_offset: Optional[str] = None, switch_pm: Optional[ForwardRef('TypeInlineBotSwitchPM')] = None, switch_webview: Optional[ForwardRef('TypeInlineBotWebView')] = None)` |
| `messages` | `SetInlineGameScoreRequest` | `messages.SetInlineGameScoreRequest` | `(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser', score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None)` |
| `messages` | `SetTypingRequest` | `messages.SetTypingRequest` | `(self, peer: 'TypeInputPeer', action: 'TypeSendMessageAction', top_msg_id: Optional[int] = None)` |
| `messages` | `StartBotRequest` | `messages.StartBotRequest` | `(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', start_param: str, random_id: int = None)` |
| `messages` | `StartHistoryImportRequest` | `messages.StartHistoryImportRequest` | `(self, peer: 'TypeInputPeer', import_id: int)` |
| `messages` | `SummarizeTextRequest` | `messages.SummarizeTextRequest` | `(self, peer: 'TypeInputPeer', id: int, to_lang: Optional[str] = None, tone: Optional[str] = None)` |
| `messages` | `ToggleBotInAttachMenuRequest` | `messages.ToggleBotInAttachMenuRequest` | `(self, bot: 'TypeInputUser', enabled: bool, write_allowed: Optional[bool] = None)` |
| `messages` | `ToggleDialogFilterTagsRequest` | `messages.ToggleDialogFilterTagsRequest` | `(self, enabled: bool)` |
| `messages` | `ToggleDialogPinRequest` | `messages.ToggleDialogPinRequest` | `(self, peer: 'TypeInputDialogPeer', pinned: Optional[bool] = None)` |
| `messages` | `ToggleNoForwardsRequest` | `messages.ToggleNoForwardsRequest` | `(self, peer: 'TypeInputPeer', enabled: bool, request_msg_id: Optional[int] = None)` |
| `messages` | `TogglePaidReactionPrivacyRequest` | `messages.TogglePaidReactionPrivacyRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, private: 'TypePaidReactionPrivacy')` |
| `messages` | `TogglePeerTranslationsRequest` | `messages.TogglePeerTranslationsRequest` | `(self, peer: 'TypeInputPeer', disabled: Optional[bool] = None)` |
| `messages` | `ToggleSavedDialogPinRequest` | `messages.ToggleSavedDialogPinRequest` | `(self, peer: 'TypeInputDialogPeer', pinned: Optional[bool] = None)` |
| `messages` | `ToggleStickerSetsRequest` | `messages.ToggleStickerSetsRequest` | `(self, stickersets: List[ForwardRef('TypeInputStickerSet')], uninstall: Optional[bool] = None, archive: Optional[bool] = None, unarchive: Optional[bool] = None)` |
| `messages` | `ToggleSuggestedPostApprovalRequest` | `messages.ToggleSuggestedPostApprovalRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, reject: Optional[bool] = None, schedule_date: Optional[datetime.datetime] = None, reject_comment: Optional[str] = None)` |
| `messages` | `ToggleTodoCompletedRequest` | `messages.ToggleTodoCompletedRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, completed: List[int], incompleted: List[int])` |
| `messages` | `TranscribeAudioRequest` | `messages.TranscribeAudioRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `messages` | `TranslateTextRequest` | `messages.TranslateTextRequest` | `(self, to_lang: str, peer: Optional[ForwardRef('TypeInputPeer')] = None, id: Optional[List[int]] = None, text: Optional[List[ForwardRef('TypeTextWithEntities')]] = None, tone: Optional[str] = None)` |
| `messages` | `UninstallStickerSetRequest` | `messages.UninstallStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet')` |
| `messages` | `UnpinAllMessagesRequest` | `messages.UnpinAllMessagesRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `messages` | `UpdateDialogFilterRequest` | `messages.UpdateDialogFilterRequest` | `(self, id: int, filter: Optional[ForwardRef('TypeDialogFilter')] = None)` |
| `messages` | `UpdateDialogFiltersOrderRequest` | `messages.UpdateDialogFiltersOrderRequest` | `(self, order: List[int])` |
| `messages` | `UpdatePinnedForumTopicRequest` | `messages.UpdatePinnedForumTopicRequest` | `(self, peer: 'TypeInputPeer', topic_id: int, pinned: bool)` |
| `messages` | `UpdatePinnedMessageRequest` | `messages.UpdatePinnedMessageRequest` | `(self, peer: 'TypeInputPeer', id: int, silent: Optional[bool] = None, unpin: Optional[bool] = None, pm_oneside: Optional[bool] = None)` |
| `messages` | `UpdateSavedReactionTagRequest` | `messages.UpdateSavedReactionTagRequest` | `(self, reaction: 'TypeReaction', title: Optional[str] = None)` |
| `messages` | `UploadEncryptedFileRequest` | `messages.UploadEncryptedFileRequest` | `(self, peer: 'TypeInputEncryptedChat', file: 'TypeInputEncryptedFile')` |
| `messages` | `UploadImportedMediaRequest` | `messages.UploadImportedMediaRequest` | `(self, peer: 'TypeInputPeer', import_id: int, file_name: str, media: 'TypeInputMedia')` |
| `messages` | `UploadMediaRequest` | `messages.UploadMediaRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', business_connection_id: Optional[str] = None)` |
| `messages` | `ViewSponsoredMessageRequest` | `messages.ViewSponsoredMessageRequest` | `(self, random_id: bytes = None)` |
| `payments` | `ApplyGiftCodeRequest` | `payments.ApplyGiftCodeRequest` | `(self, slug: str)` |
| `payments` | `AssignAppStoreTransactionRequest` | `payments.AssignAppStoreTransactionRequest` | `(self, receipt: bytes, purpose: 'TypeInputStorePaymentPurpose')` |
| `payments` | `AssignPlayMarketTransactionRequest` | `payments.AssignPlayMarketTransactionRequest` | `(self, receipt: 'TypeDataJSON', purpose: 'TypeInputStorePaymentPurpose')` |
| `payments` | `BotCancelStarsSubscriptionRequest` | `payments.BotCancelStarsSubscriptionRequest` | `(self, user_id: 'TypeInputUser', charge_id: str, restore: Optional[bool] = None)` |
| `payments` | `CanPurchaseStoreRequest` | `payments.CanPurchaseStoreRequest` | `(self, purpose: 'TypeInputStorePaymentPurpose')` |
| `payments` | `ChangeStarsSubscriptionRequest` | `payments.ChangeStarsSubscriptionRequest` | `(self, peer: 'TypeInputPeer', subscription_id: str, canceled: Optional[bool] = None)` |
| `payments` | `CheckCanSendGiftRequest` | `payments.CheckCanSendGiftRequest` | `(self, gift_id: int)` |
| `payments` | `CheckGiftCodeRequest` | `payments.CheckGiftCodeRequest` | `(self, slug: str)` |
| `payments` | `ClearSavedInfoRequest` | `payments.ClearSavedInfoRequest` | `(self, credentials: Optional[bool] = None, info: Optional[bool] = None)` |
| `payments` | `ConnectStarRefBotRequest` | `payments.ConnectStarRefBotRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser')` |
| `payments` | `ConvertStarGiftRequest` | `payments.ConvertStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift')` |
| `payments` | `CraftStarGiftRequest` | `payments.CraftStarGiftRequest` | `(self, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `payments` | `CreateStarGiftCollectionRequest` | `payments.CreateStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', title: str, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `payments` | `DeleteStarGiftCollectionRequest` | `payments.DeleteStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', collection_id: int)` |
| `payments` | `EditConnectedStarRefBotRequest` | `payments.EditConnectedStarRefBotRequest` | `(self, peer: 'TypeInputPeer', link: str, revoked: Optional[bool] = None)` |
| `payments` | `ExportInvoiceRequest` | `payments.ExportInvoiceRequest` | `(self, invoice_media: 'TypeInputMedia')` |
| `payments` | `FulfillStarsSubscriptionRequest` | `payments.FulfillStarsSubscriptionRequest` | `(self, peer: 'TypeInputPeer', subscription_id: str)` |
| `payments` | `GetBankCardDataRequest` | `payments.GetBankCardDataRequest` | `(self, number: str)` |
| `payments` | `GetConnectedStarRefBotRequest` | `payments.GetConnectedStarRefBotRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser')` |
| `payments` | `GetConnectedStarRefBotsRequest` | `payments.GetConnectedStarRefBotsRequest` | `(self, peer: 'TypeInputPeer', limit: int, offset_date: Optional[datetime.datetime] = None, offset_link: Optional[str] = None)` |
| `payments` | `GetCraftStarGiftsRequest` | `payments.GetCraftStarGiftsRequest` | `(self, gift_id: int, offset: str, limit: int)` |
| `payments` | `GetGiveawayInfoRequest` | `payments.GetGiveawayInfoRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `payments` | `GetPaymentFormRequest` | `payments.GetPaymentFormRequest` | `(self, invoice: 'TypeInputInvoice', theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `payments` | `GetPaymentReceiptRequest` | `payments.GetPaymentReceiptRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `payments` | `GetPremiumGiftCodeOptionsRequest` | `payments.GetPremiumGiftCodeOptionsRequest` | `(self, boost_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `payments` | `GetResaleStarGiftsRequest` | `payments.GetResaleStarGiftsRequest` | `(self, gift_id: int, offset: str, limit: int, sort_by_price: Optional[bool] = None, sort_by_num: Optional[bool] = None, for_craft: Optional[bool] = None, stars_only: Optional[bool] = None, attributes_hash: Optional[int] = None, attributes: Optional[List[ForwardRef('TypeStarGiftAttributeId')]] = None)` |
| `payments` | `GetSavedInfoRequest` | `payments.GetSavedInfoRequest` | `(self, /, *args, **kwargs)` |
| `payments` | `GetSavedStarGiftRequest` | `payments.GetSavedStarGiftRequest` | `(self, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `payments` | `GetSavedStarGiftsRequest` | `payments.GetSavedStarGiftsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, exclude_unsaved: Optional[bool] = None, exclude_saved: Optional[bool] = None, exclude_unlimited: Optional[bool] = None, exclude_unique: Optional[bool] = None, sort_by_value: Optional[bool] = None, exclude_upgradable: Optional[bool] = None, exclude_unupgradable: Optional[bool] = None, peer_color_available: Optional[bool] = None, exclude_hosted: Optional[bool] = None, collection_id: Optional[int] = None)` |
| `payments` | `GetStarGiftActiveAuctionsRequest` | `payments.GetStarGiftActiveAuctionsRequest` | `(self, hash: int)` |
| `payments` | `GetStarGiftAuctionAcquiredGiftsRequest` | `payments.GetStarGiftAuctionAcquiredGiftsRequest` | `(self, gift_id: int)` |
| `payments` | `GetStarGiftAuctionStateRequest` | `payments.GetStarGiftAuctionStateRequest` | `(self, auction: 'TypeInputStarGiftAuction', version: int)` |
| `payments` | `GetStarGiftCollectionsRequest` | `payments.GetStarGiftCollectionsRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `payments` | `GetStarGiftUpgradeAttributesRequest` | `payments.GetStarGiftUpgradeAttributesRequest` | `(self, gift_id: int)` |
| `payments` | `GetStarGiftUpgradePreviewRequest` | `payments.GetStarGiftUpgradePreviewRequest` | `(self, gift_id: int)` |
| `payments` | `GetStarGiftWithdrawalUrlRequest` | `payments.GetStarGiftWithdrawalUrlRequest` | `(self, stargift: 'TypeInputSavedStarGift', password: 'TypeInputCheckPasswordSRP')` |
| `payments` | `GetStarGiftsRequest` | `payments.GetStarGiftsRequest` | `(self, hash: int)` |
| `payments` | `GetStarsGiftOptionsRequest` | `payments.GetStarsGiftOptionsRequest` | `(self, user_id: Optional[ForwardRef('TypeInputUser')] = None)` |
| `payments` | `GetStarsGiveawayOptionsRequest` | `payments.GetStarsGiveawayOptionsRequest` | `(self, /, *args, **kwargs)` |
| `payments` | `GetStarsRevenueAdsAccountUrlRequest` | `payments.GetStarsRevenueAdsAccountUrlRequest` | `(self, peer: 'TypeInputPeer')` |
| `payments` | `GetStarsRevenueStatsRequest` | `payments.GetStarsRevenueStatsRequest` | `(self, peer: 'TypeInputPeer', dark: Optional[bool] = None, ton: Optional[bool] = None)` |
| `payments` | `GetStarsRevenueWithdrawalUrlRequest` | `payments.GetStarsRevenueWithdrawalUrlRequest` | `(self, peer: 'TypeInputPeer', password: 'TypeInputCheckPasswordSRP', ton: Optional[bool] = None, amount: Optional[int] = None)` |
| `payments` | `GetStarsStatusRequest` | `payments.GetStarsStatusRequest` | `(self, peer: 'TypeInputPeer', ton: Optional[bool] = None)` |
| `payments` | `GetStarsSubscriptionsRequest` | `payments.GetStarsSubscriptionsRequest` | `(self, peer: 'TypeInputPeer', offset: str, missing_balance: Optional[bool] = None)` |
| `payments` | `GetStarsTopupOptionsRequest` | `payments.GetStarsTopupOptionsRequest` | `(self, /, *args, **kwargs)` |
| `payments` | `GetStarsTransactionsByIDRequest` | `payments.GetStarsTransactionsByIDRequest` | `(self, peer: 'TypeInputPeer', id: List[ForwardRef('TypeInputStarsTransaction')], ton: Optional[bool] = None)` |
| `payments` | `GetStarsTransactionsRequest` | `payments.GetStarsTransactionsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, inbound: Optional[bool] = None, outbound: Optional[bool] = None, ascending: Optional[bool] = None, ton: Optional[bool] = None, subscription_id: Optional[str] = None)` |
| `payments` | `GetSuggestedStarRefBotsRequest` | `payments.GetSuggestedStarRefBotsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, order_by_revenue: Optional[bool] = None, order_by_date: Optional[bool] = None)` |
| `payments` | `GetUniqueStarGiftRequest` | `payments.GetUniqueStarGiftRequest` | `(self, slug: str)` |
| `payments` | `GetUniqueStarGiftValueInfoRequest` | `payments.GetUniqueStarGiftValueInfoRequest` | `(self, slug: str)` |
| `payments` | `LaunchPrepaidGiveawayRequest` | `payments.LaunchPrepaidGiveawayRequest` | `(self, peer: 'TypeInputPeer', giveaway_id: int, purpose: 'TypeInputStorePaymentPurpose')` |
| `payments` | `RefundStarsChargeRequest` | `payments.RefundStarsChargeRequest` | `(self, user_id: 'TypeInputUser', charge_id: str)` |
| `payments` | `ReorderStarGiftCollectionsRequest` | `payments.ReorderStarGiftCollectionsRequest` | `(self, peer: 'TypeInputPeer', order: List[int])` |
| `payments` | `ResolveStarGiftOfferRequest` | `payments.ResolveStarGiftOfferRequest` | `(self, offer_msg_id: int, decline: Optional[bool] = None)` |
| `payments` | `SaveStarGiftRequest` | `payments.SaveStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', unsave: Optional[bool] = None)` |
| `payments` | `SendPaymentFormRequest` | `payments.SendPaymentFormRequest` | `(self, form_id: int, invoice: 'TypeInputInvoice', credentials: 'TypeInputPaymentCredentials', requested_info_id: Optional[str] = None, shipping_option_id: Optional[str] = None, tip_amount: Optional[int] = None)` |
| `payments` | `SendStarGiftOfferRequest` | `payments.SendStarGiftOfferRequest` | `(self, peer: 'TypeInputPeer', slug: str, price: 'TypeStarsAmount', duration: int, random_id: int = None, allow_paid_stars: Optional[int] = None)` |
| `payments` | `SendStarsFormRequest` | `payments.SendStarsFormRequest` | `(self, form_id: int, invoice: 'TypeInputInvoice')` |
| `payments` | `ToggleChatStarGiftNotificationsRequest` | `payments.ToggleChatStarGiftNotificationsRequest` | `(self, peer: 'TypeInputPeer', enabled: Optional[bool] = None)` |
| `payments` | `ToggleStarGiftsPinnedToTopRequest` | `payments.ToggleStarGiftsPinnedToTopRequest` | `(self, peer: 'TypeInputPeer', stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `payments` | `TransferStarGiftRequest` | `payments.TransferStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', to_id: 'TypeInputPeer')` |
| `payments` | `UpdateStarGiftCollectionRequest` | `payments.UpdateStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', collection_id: int, title: Optional[str] = None, delete_stargift: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None, add_stargift: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None, order: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None)` |
| `payments` | `UpdateStarGiftPriceRequest` | `payments.UpdateStarGiftPriceRequest` | `(self, stargift: 'TypeInputSavedStarGift', resell_amount: 'TypeStarsAmount')` |
| `payments` | `UpgradeStarGiftRequest` | `payments.UpgradeStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', keep_original_details: Optional[bool] = None)` |
| `payments` | `ValidateRequestedInfoRequest` | `payments.ValidateRequestedInfoRequest` | `(self, invoice: 'TypeInputInvoice', info: 'TypePaymentRequestedInfo', save: Optional[bool] = None)` |
| `phone` | `AcceptCallRequest` | `phone.AcceptCallRequest` | `(self, peer: 'TypeInputPhoneCall', g_b: bytes, protocol: 'TypePhoneCallProtocol')` |
| `phone` | `CheckGroupCallRequest` | `phone.CheckGroupCallRequest` | `(self, call: 'TypeInputGroupCall', sources: List[int])` |
| `phone` | `ConfirmCallRequest` | `phone.ConfirmCallRequest` | `(self, peer: 'TypeInputPhoneCall', g_a: bytes, key_fingerprint: int, protocol: 'TypePhoneCallProtocol')` |
| `phone` | `CreateConferenceCallRequest` | `phone.CreateConferenceCallRequest` | `(self, muted: Optional[bool] = None, video_stopped: Optional[bool] = None, join: Optional[bool] = None, random_id: int = None, public_key: Optional[int] = None, block: Optional[bytes] = None, params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `phone` | `CreateGroupCallRequest` | `phone.CreateGroupCallRequest` | `(self, peer: 'TypeInputPeer', rtmp_stream: Optional[bool] = None, random_id: int = None, title: Optional[str] = None, schedule_date: Optional[datetime.datetime] = None)` |
| `phone` | `DeclineConferenceCallInviteRequest` | `phone.DeclineConferenceCallInviteRequest` | `(self, msg_id: int)` |
| `phone` | `DeleteConferenceCallParticipantsRequest` | `phone.DeleteConferenceCallParticipantsRequest` | `(self, call: 'TypeInputGroupCall', ids: List[int], block: bytes, only_left: Optional[bool] = None, kick: Optional[bool] = None)` |
| `phone` | `DeleteGroupCallMessagesRequest` | `phone.DeleteGroupCallMessagesRequest` | `(self, call: 'TypeInputGroupCall', messages: List[int], report_spam: Optional[bool] = None)` |
| `phone` | `DeleteGroupCallParticipantMessagesRequest` | `phone.DeleteGroupCallParticipantMessagesRequest` | `(self, call: 'TypeInputGroupCall', participant: 'TypeInputPeer', report_spam: Optional[bool] = None)` |
| `phone` | `DiscardCallRequest` | `phone.DiscardCallRequest` | `(self, peer: 'TypeInputPhoneCall', duration: int, reason: 'TypePhoneCallDiscardReason', connection_id: int, video: Optional[bool] = None)` |
| `phone` | `DiscardGroupCallRequest` | `phone.DiscardGroupCallRequest` | `(self, call: 'TypeInputGroupCall')` |
| `phone` | `EditGroupCallParticipantRequest` | `phone.EditGroupCallParticipantRequest` | `(self, call: 'TypeInputGroupCall', participant: 'TypeInputPeer', muted: Optional[bool] = None, volume: Optional[int] = None, raise_hand: Optional[bool] = None, video_stopped: Optional[bool] = None, video_paused: Optional[bool] = None, presentation_paused: Optional[bool] = None)` |
| `phone` | `EditGroupCallTitleRequest` | `phone.EditGroupCallTitleRequest` | `(self, call: 'TypeInputGroupCall', title: str)` |
| `phone` | `ExportGroupCallInviteRequest` | `phone.ExportGroupCallInviteRequest` | `(self, call: 'TypeInputGroupCall', can_self_unmute: Optional[bool] = None)` |
| `phone` | `GetCallConfigRequest` | `phone.GetCallConfigRequest` | `(self, /, *args, **kwargs)` |
| `phone` | `GetGroupCallChainBlocksRequest` | `phone.GetGroupCallChainBlocksRequest` | `(self, call: 'TypeInputGroupCall', sub_chain_id: int, offset: int, limit: int)` |
| `phone` | `GetGroupCallJoinAsRequest` | `phone.GetGroupCallJoinAsRequest` | `(self, peer: 'TypeInputPeer')` |
| `phone` | `GetGroupCallRequest` | `phone.GetGroupCallRequest` | `(self, call: 'TypeInputGroupCall', limit: int)` |
| `phone` | `GetGroupCallStarsRequest` | `phone.GetGroupCallStarsRequest` | `(self, call: 'TypeInputGroupCall')` |
| `phone` | `GetGroupCallStreamChannelsRequest` | `phone.GetGroupCallStreamChannelsRequest` | `(self, call: 'TypeInputGroupCall')` |
| `phone` | `GetGroupCallStreamRtmpUrlRequest` | `phone.GetGroupCallStreamRtmpUrlRequest` | `(self, peer: 'TypeInputPeer', revoke: bool, live_story: Optional[bool] = None)` |
| `phone` | `GetGroupParticipantsRequest` | `phone.GetGroupParticipantsRequest` | `(self, call: 'TypeInputGroupCall', ids: List[ForwardRef('TypeInputPeer')], sources: List[int], offset: str, limit: int)` |
| `phone` | `InviteConferenceCallParticipantRequest` | `phone.InviteConferenceCallParticipantRequest` | `(self, call: 'TypeInputGroupCall', user_id: 'TypeInputUser', video: Optional[bool] = None)` |
| `phone` | `InviteToGroupCallRequest` | `phone.InviteToGroupCallRequest` | `(self, call: 'TypeInputGroupCall', users: List[ForwardRef('TypeInputUser')])` |
| `phone` | `JoinGroupCallPresentationRequest` | `phone.JoinGroupCallPresentationRequest` | `(self, call: 'TypeInputGroupCall', params: 'TypeDataJSON')` |
| `phone` | `JoinGroupCallRequest` | `phone.JoinGroupCallRequest` | `(self, call: 'TypeInputGroupCall', join_as: 'TypeInputPeer', params: 'TypeDataJSON', muted: Optional[bool] = None, video_stopped: Optional[bool] = None, invite_hash: Optional[str] = None, public_key: Optional[int] = None, block: Optional[bytes] = None)` |
| `phone` | `LeaveGroupCallPresentationRequest` | `phone.LeaveGroupCallPresentationRequest` | `(self, call: 'TypeInputGroupCall')` |
| `phone` | `LeaveGroupCallRequest` | `phone.LeaveGroupCallRequest` | `(self, call: 'TypeInputGroupCall', source: int)` |
| `phone` | `ReceivedCallRequest` | `phone.ReceivedCallRequest` | `(self, peer: 'TypeInputPhoneCall')` |
| `phone` | `RequestCallRequest` | `phone.RequestCallRequest` | `(self, user_id: 'TypeInputUser', g_a_hash: bytes, protocol: 'TypePhoneCallProtocol', video: Optional[bool] = None, random_id: int = None)` |
| `phone` | `SaveCallDebugRequest` | `phone.SaveCallDebugRequest` | `(self, peer: 'TypeInputPhoneCall', debug: 'TypeDataJSON')` |
| `phone` | `SaveCallLogRequest` | `phone.SaveCallLogRequest` | `(self, peer: 'TypeInputPhoneCall', file: 'TypeInputFile')` |
| `phone` | `SaveDefaultGroupCallJoinAsRequest` | `phone.SaveDefaultGroupCallJoinAsRequest` | `(self, peer: 'TypeInputPeer', join_as: 'TypeInputPeer')` |
| `phone` | `SaveDefaultSendAsRequest` | `phone.SaveDefaultSendAsRequest` | `(self, call: 'TypeInputGroupCall', send_as: 'TypeInputPeer')` |
| `phone` | `SendConferenceCallBroadcastRequest` | `phone.SendConferenceCallBroadcastRequest` | `(self, call: 'TypeInputGroupCall', block: bytes)` |
| `phone` | `SendGroupCallEncryptedMessageRequest` | `phone.SendGroupCallEncryptedMessageRequest` | `(self, call: 'TypeInputGroupCall', encrypted_message: bytes)` |
| `phone` | `SendGroupCallMessageRequest` | `phone.SendGroupCallMessageRequest` | `(self, call: 'TypeInputGroupCall', message: 'TypeTextWithEntities', random_id: int = None, allow_paid_stars: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `phone` | `SendSignalingDataRequest` | `phone.SendSignalingDataRequest` | `(self, peer: 'TypeInputPhoneCall', data: bytes)` |
| `phone` | `SetCallRatingRequest` | `phone.SetCallRatingRequest` | `(self, peer: 'TypeInputPhoneCall', rating: int, comment: str, user_initiative: Optional[bool] = None)` |
| `phone` | `StartScheduledGroupCallRequest` | `phone.StartScheduledGroupCallRequest` | `(self, call: 'TypeInputGroupCall')` |
| `phone` | `ToggleGroupCallRecordRequest` | `phone.ToggleGroupCallRecordRequest` | `(self, call: 'TypeInputGroupCall', start: Optional[bool] = None, video: Optional[bool] = None, title: Optional[str] = None, video_portrait: Optional[bool] = None)` |
| `phone` | `ToggleGroupCallSettingsRequest` | `phone.ToggleGroupCallSettingsRequest` | `(self, call: 'TypeInputGroupCall', reset_invite_hash: Optional[bool] = None, join_muted: Optional[bool] = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None)` |
| `phone` | `ToggleGroupCallStartSubscriptionRequest` | `phone.ToggleGroupCallStartSubscriptionRequest` | `(self, call: 'TypeInputGroupCall', subscribed: bool)` |
| `photos` | `DeletePhotosRequest` | `photos.DeletePhotosRequest` | `(self, id: List[ForwardRef('TypeInputPhoto')])` |
| `photos` | `GetUserPhotosRequest` | `photos.GetUserPhotosRequest` | `(self, user_id: 'TypeInputUser', offset: int, max_id: int, limit: int)` |
| `photos` | `UpdateProfilePhotoRequest` | `photos.UpdateProfilePhotoRequest` | `(self, id: 'TypeInputPhoto', fallback: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `photos` | `UploadContactProfilePhotoRequest` | `photos.UploadContactProfilePhotoRequest` | `(self, user_id: 'TypeInputUser', suggest: Optional[bool] = None, save: Optional[bool] = None, file: Optional[ForwardRef('TypeInputFile')] = None, video: Optional[ForwardRef('TypeInputFile')] = None, video_start_ts: Optional[float] = None, video_emoji_markup: Optional[ForwardRef('TypeVideoSize')] = None)` |
| `photos` | `UploadProfilePhotoRequest` | `photos.UploadProfilePhotoRequest` | `(self, fallback: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None, file: Optional[ForwardRef('TypeInputFile')] = None, video: Optional[ForwardRef('TypeInputFile')] = None, video_start_ts: Optional[float] = None, video_emoji_markup: Optional[ForwardRef('TypeVideoSize')] = None)` |
| `premium` | `ApplyBoostRequest` | `premium.ApplyBoostRequest` | `(self, peer: 'TypeInputPeer', slots: Optional[List[int]] = None)` |
| `premium` | `GetBoostsListRequest` | `premium.GetBoostsListRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, gifts: Optional[bool] = None)` |
| `premium` | `GetBoostsStatusRequest` | `premium.GetBoostsStatusRequest` | `(self, peer: 'TypeInputPeer')` |
| `premium` | `GetMyBoostsRequest` | `premium.GetMyBoostsRequest` | `(self, /, *args, **kwargs)` |
| `premium` | `GetUserBoostsRequest` | `premium.GetUserBoostsRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser')` |
| `smsjobs` | `FinishJobRequest` | `smsjobs.FinishJobRequest` | `(self, job_id: str, error: Optional[str] = None)` |
| `smsjobs` | `GetSmsJobRequest` | `smsjobs.GetSmsJobRequest` | `(self, job_id: str)` |
| `smsjobs` | `GetStatusRequest` | `smsjobs.GetStatusRequest` | `(self, /, *args, **kwargs)` |
| `smsjobs` | `IsEligibleToJoinRequest` | `smsjobs.IsEligibleToJoinRequest` | `(self, /, *args, **kwargs)` |
| `smsjobs` | `JoinRequest` | `smsjobs.JoinRequest` | `(self, /, *args, **kwargs)` |
| `smsjobs` | `LeaveRequest` | `smsjobs.LeaveRequest` | `(self, /, *args, **kwargs)` |
| `smsjobs` | `UpdateSettingsRequest` | `smsjobs.UpdateSettingsRequest` | `(self, allow_international: Optional[bool] = None)` |
| `stats` | `GetBroadcastStatsRequest` | `stats.GetBroadcastStatsRequest` | `(self, channel: 'TypeInputChannel', dark: Optional[bool] = None)` |
| `stats` | `GetMegagroupStatsRequest` | `stats.GetMegagroupStatsRequest` | `(self, channel: 'TypeInputChannel', dark: Optional[bool] = None)` |
| `stats` | `GetMessagePublicForwardsRequest` | `stats.GetMessagePublicForwardsRequest` | `(self, channel: 'TypeInputChannel', msg_id: int, offset: str, limit: int)` |
| `stats` | `GetMessageStatsRequest` | `stats.GetMessageStatsRequest` | `(self, channel: 'TypeInputChannel', msg_id: int, dark: Optional[bool] = None)` |
| `stats` | `GetPollStatsRequest` | `stats.GetPollStatsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, dark: Optional[bool] = None)` |
| `stats` | `GetStoryPublicForwardsRequest` | `stats.GetStoryPublicForwardsRequest` | `(self, peer: 'TypeInputPeer', id: int, offset: str, limit: int)` |
| `stats` | `GetStoryStatsRequest` | `stats.GetStoryStatsRequest` | `(self, peer: 'TypeInputPeer', id: int, dark: Optional[bool] = None)` |
| `stats` | `LoadAsyncGraphRequest` | `stats.LoadAsyncGraphRequest` | `(self, token: str, x: Optional[int] = None)` |
| `stickers` | `AddStickerToSetRequest` | `stickers.AddStickerToSetRequest` | `(self, stickerset: 'TypeInputStickerSet', sticker: 'TypeInputStickerSetItem')` |
| `stickers` | `ChangeStickerPositionRequest` | `stickers.ChangeStickerPositionRequest` | `(self, sticker: 'TypeInputDocument', position: int)` |
| `stickers` | `ChangeStickerRequest` | `stickers.ChangeStickerRequest` | `(self, sticker: 'TypeInputDocument', emoji: Optional[str] = None, mask_coords: Optional[ForwardRef('TypeMaskCoords')] = None, keywords: Optional[str] = None)` |
| `stickers` | `CheckShortNameRequest` | `stickers.CheckShortNameRequest` | `(self, short_name: str)` |
| `stickers` | `CreateStickerSetRequest` | `stickers.CreateStickerSetRequest` | `(self, user_id: 'TypeInputUser', title: str, short_name: str, stickers: List[ForwardRef('TypeInputStickerSetItem')], masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, thumb: Optional[ForwardRef('TypeInputDocument')] = None, software: Optional[str] = None)` |
| `stickers` | `DeleteStickerSetRequest` | `stickers.DeleteStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet')` |
| `stickers` | `RemoveStickerFromSetRequest` | `stickers.RemoveStickerFromSetRequest` | `(self, sticker: 'TypeInputDocument')` |
| `stickers` | `RenameStickerSetRequest` | `stickers.RenameStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', title: str)` |
| `stickers` | `ReplaceStickerRequest` | `stickers.ReplaceStickerRequest` | `(self, sticker: 'TypeInputDocument', new_sticker: 'TypeInputStickerSetItem')` |
| `stickers` | `SetStickerSetThumbRequest` | `stickers.SetStickerSetThumbRequest` | `(self, stickerset: 'TypeInputStickerSet', thumb: Optional[ForwardRef('TypeInputDocument')] = None, thumb_document_id: Optional[int] = None)` |
| `stickers` | `SuggestShortNameRequest` | `stickers.SuggestShortNameRequest` | `(self, title: str)` |
| `stories` | `ActivateStealthModeRequest` | `stories.ActivateStealthModeRequest` | `(self, past: Optional[bool] = None, future: Optional[bool] = None)` |
| `stories` | `CanSendStoryRequest` | `stories.CanSendStoryRequest` | `(self, peer: 'TypeInputPeer')` |
| `stories` | `CreateAlbumRequest` | `stories.CreateAlbumRequest` | `(self, peer: 'TypeInputPeer', title: str, stories: List[int])` |
| `stories` | `DeleteAlbumRequest` | `stories.DeleteAlbumRequest` | `(self, peer: 'TypeInputPeer', album_id: int)` |
| `stories` | `DeleteStoriesRequest` | `stories.DeleteStoriesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `stories` | `EditStoryRequest` | `stories.EditStoryRequest` | `(self, peer: 'TypeInputPeer', id: int, media: Optional[ForwardRef('TypeInputMedia')] = None, media_areas: Optional[List[ForwardRef('TypeMediaArea')]] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, privacy_rules: Optional[List[ForwardRef('TypeInputPrivacyRule')]] = None, music: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `stories` | `ExportStoryLinkRequest` | `stories.ExportStoryLinkRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `stories` | `GetAlbumStoriesRequest` | `stories.GetAlbumStoriesRequest` | `(self, peer: 'TypeInputPeer', album_id: int, offset: int, limit: int)` |
| `stories` | `GetAlbumsRequest` | `stories.GetAlbumsRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `stories` | `GetAllReadPeerStoriesRequest` | `stories.GetAllReadPeerStoriesRequest` | `(self, /, *args, **kwargs)` |
| `stories` | `GetAllStoriesRequest` | `stories.GetAllStoriesRequest` | `(self, next: Optional[bool] = None, hidden: Optional[bool] = None, state: Optional[str] = None)` |
| `stories` | `GetChatsToSendRequest` | `stories.GetChatsToSendRequest` | `(self, /, *args, **kwargs)` |
| `stories` | `GetPeerMaxIDsRequest` | `stories.GetPeerMaxIDsRequest` | `(self, id: List[ForwardRef('TypeInputPeer')])` |
| `stories` | `GetPeerStoriesRequest` | `stories.GetPeerStoriesRequest` | `(self, peer: 'TypeInputPeer')` |
| `stories` | `GetPinnedStoriesRequest` | `stories.GetPinnedStoriesRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, limit: int)` |
| `stories` | `GetStoriesArchiveRequest` | `stories.GetStoriesArchiveRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, limit: int)` |
| `stories` | `GetStoriesByIDRequest` | `stories.GetStoriesByIDRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `stories` | `GetStoriesViewsRequest` | `stories.GetStoriesViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `stories` | `GetStoryReactionsListRequest` | `stories.GetStoryReactionsListRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, forwards_first: Optional[bool] = None, reaction: Optional[ForwardRef('TypeReaction')] = None, offset: Optional[str] = None)` |
| `stories` | `GetStoryViewsListRequest` | `stories.GetStoryViewsListRequest` | `(self, peer: 'TypeInputPeer', id: int, offset: str, limit: int, just_contacts: Optional[bool] = None, reactions_first: Optional[bool] = None, forwards_first: Optional[bool] = None, q: Optional[str] = None)` |
| `stories` | `IncrementStoryViewsRequest` | `stories.IncrementStoryViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `stories` | `ReadStoriesRequest` | `stories.ReadStoriesRequest` | `(self, peer: 'TypeInputPeer', max_id: int)` |
| `stories` | `ReorderAlbumsRequest` | `stories.ReorderAlbumsRequest` | `(self, peer: 'TypeInputPeer', order: List[int])` |
| `stories` | `ReportRequest` | `stories.ReportRequest` | `(self, peer: 'TypeInputPeer', id: List[int], option: bytes, message: str)` |
| `stories` | `SearchPostsRequest` | `stories.SearchPostsRequest` | `(self, offset: str, limit: int, hashtag: Optional[str] = None, area: Optional[ForwardRef('TypeMediaArea')] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `stories` | `SendReactionRequest` | `stories.SendReactionRequest` | `(self, peer: 'TypeInputPeer', story_id: int, reaction: 'TypeReaction', add_to_recent: Optional[bool] = None)` |
| `stories` | `SendStoryRequest` | `stories.SendStoryRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', privacy_rules: List[ForwardRef('TypeInputPrivacyRule')], pinned: Optional[bool] = None, noforwards: Optional[bool] = None, fwd_modified: Optional[bool] = None, media_areas: Optional[List[ForwardRef('TypeMediaArea')]] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, random_id: int = None, period: Optional[int] = None, fwd_from_id: Optional[ForwardRef('TypeInputPeer')] = None, fwd_from_story: Optional[int] = None, albums: Optional[List[int]] = None, music: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `stories` | `StartLiveRequest` | `stories.StartLiveRequest` | `(self, peer: 'TypeInputPeer', privacy_rules: List[ForwardRef('TypeInputPrivacyRule')], pinned: Optional[bool] = None, noforwards: Optional[bool] = None, rtmp_stream: Optional[bool] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, random_id: int = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None)` |
| `stories` | `ToggleAllStoriesHiddenRequest` | `stories.ToggleAllStoriesHiddenRequest` | `(self, hidden: bool)` |
| `stories` | `TogglePeerStoriesHiddenRequest` | `stories.TogglePeerStoriesHiddenRequest` | `(self, peer: 'TypeInputPeer', hidden: bool)` |
| `stories` | `TogglePinnedRequest` | `stories.TogglePinnedRequest` | `(self, peer: 'TypeInputPeer', id: List[int], pinned: bool)` |
| `stories` | `TogglePinnedToTopRequest` | `stories.TogglePinnedToTopRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `stories` | `UpdateAlbumRequest` | `stories.UpdateAlbumRequest` | `(self, peer: 'TypeInputPeer', album_id: int, title: Optional[str] = None, delete_stories: Optional[List[int]] = None, add_stories: Optional[List[int]] = None, order: Optional[List[int]] = None)` |
| `updates` | `GetChannelDifferenceRequest` | `updates.GetChannelDifferenceRequest` | `(self, channel: 'TypeInputChannel', filter: 'TypeChannelMessagesFilter', pts: int, limit: int, force: Optional[bool] = None)` |
| `updates` | `GetDifferenceRequest` | `updates.GetDifferenceRequest` | `(self, pts: int, date: Optional[datetime.datetime], qts: int, pts_limit: Optional[int] = None, pts_total_limit: Optional[int] = None, qts_limit: Optional[int] = None)` |
| `updates` | `GetStateRequest` | `updates.GetStateRequest` | `(self, /, *args, **kwargs)` |
| `upload` | `GetCdnFileHashesRequest` | `upload.GetCdnFileHashesRequest` | `(self, file_token: bytes, offset: int)` |
| `upload` | `GetCdnFileRequest` | `upload.GetCdnFileRequest` | `(self, file_token: bytes, offset: int, limit: int)` |
| `upload` | `GetFileHashesRequest` | `upload.GetFileHashesRequest` | `(self, location: 'TypeInputFileLocation', offset: int)` |
| `upload` | `GetFileRequest` | `upload.GetFileRequest` | `(self, location: 'TypeInputFileLocation', offset: int, limit: int, precise: Optional[bool] = None, cdn_supported: Optional[bool] = None)` |
| `upload` | `GetWebFileRequest` | `upload.GetWebFileRequest` | `(self, location: 'TypeInputWebFileLocation', offset: int, limit: int)` |
| `upload` | `ReuploadCdnFileRequest` | `upload.ReuploadCdnFileRequest` | `(self, file_token: bytes, request_token: bytes)` |
| `upload` | `SaveBigFilePartRequest` | `upload.SaveBigFilePartRequest` | `(self, file_id: int, file_part: int, file_total_parts: int, bytes: bytes)` |
| `upload` | `SaveFilePartRequest` | `upload.SaveFilePartRequest` | `(self, file_id: int, file_part: int, bytes: bytes)` |
| `users` | `GetFullUserRequest` | `users.GetFullUserRequest` | `(self, id: 'TypeInputUser')` |
| `users` | `GetRequirementsToContactRequest` | `users.GetRequirementsToContactRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `users` | `GetSavedMusicByIDRequest` | `users.GetSavedMusicByIDRequest` | `(self, id: 'TypeInputUser', documents: List[ForwardRef('TypeInputDocument')])` |
| `users` | `GetSavedMusicRequest` | `users.GetSavedMusicRequest` | `(self, id: 'TypeInputUser', offset: int, limit: int, hash: int)` |
| `users` | `GetUsersRequest` | `users.GetUsersRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `users` | `SetSecureValueErrorsRequest` | `users.SetSecureValueErrorsRequest` | `(self, id: 'TypeInputUser', errors: List[ForwardRef('TypeSecureValueError')])` |
| `users` | `SuggestBirthdayRequest` | `users.SuggestBirthdayRequest` | `(self, id: 'TypeInputUser', birthday: 'TypeBirthday')` |

### `type_constructor`

| Namespace | Name | Callable Path | Constructor Signature |
|---|---|---|---|
| `types` | `AccessPointRule` | `AccessPointRule` | `(self, phone_prefix_rules: str, dc_id: int, ips: List[ForwardRef('TypeIpPort')])` |
| `types` | `AccountDaysTTL` | `AccountDaysTTL` | `(self, days: int)` |
| `types` | `AiComposeTone` | `AiComposeTone` | `(self, id: int, access_hash: int, slug: str, title: str, creator: Optional[bool] = None, emoji_id: Optional[int] = None, prompt: Optional[str] = None, installs_count: Optional[int] = None, author_id: Optional[int] = None, example_english: Optional[ForwardRef('TypeAiComposeToneExample')] = None)` |
| `types` | `AiComposeToneDefault` | `AiComposeToneDefault` | `(self, tone: str, emoji_id: int, title: str)` |
| `types` | `AiComposeToneExample` | `AiComposeToneExample` | `(self, from_: 'TypeTextWithEntities', to: 'TypeTextWithEntities')` |
| `types` | `AttachMenuBot` | `AttachMenuBot` | `(self, bot_id: int, short_name: str, icons: List[ForwardRef('TypeAttachMenuBotIcon')], inactive: Optional[bool] = None, has_settings: Optional[bool] = None, request_write_access: Optional[bool] = None, show_in_attach_menu: Optional[bool] = None, show_in_side_menu: Optional[bool] = None, side_menu_disclaimer_needed: Optional[bool] = None, peer_types: Optional[List[ForwardRef('TypeAttachMenuPeerType')]] = None)` |
| `types` | `AttachMenuBotIcon` | `AttachMenuBotIcon` | `(self, name: str, icon: 'TypeDocument', colors: Optional[List[ForwardRef('TypeAttachMenuBotIconColor')]] = None)` |
| `types` | `AttachMenuBotIconColor` | `AttachMenuBotIconColor` | `(self, name: str, color: int)` |
| `types` | `AttachMenuBots` | `AttachMenuBots` | `(self, hash: int, bots: List[ForwardRef('TypeAttachMenuBot')], users: List[ForwardRef('TypeUser')])` |
| `types` | `AttachMenuBotsBot` | `AttachMenuBotsBot` | `(self, bot: 'TypeAttachMenuBot', users: List[ForwardRef('TypeUser')])` |
| `types` | `AttachMenuBotsNotModified` | `AttachMenuBotsNotModified` | `(self, /, *args, **kwargs)` |
| `types` | `AttachMenuPeerTypeBotPM` | `AttachMenuPeerTypeBotPM` | `(self, /, *args, **kwargs)` |
| `types` | `AttachMenuPeerTypeBroadcast` | `AttachMenuPeerTypeBroadcast` | `(self, /, *args, **kwargs)` |
| `types` | `AttachMenuPeerTypeChat` | `AttachMenuPeerTypeChat` | `(self, /, *args, **kwargs)` |
| `types` | `AttachMenuPeerTypePM` | `AttachMenuPeerTypePM` | `(self, /, *args, **kwargs)` |
| `types` | `AttachMenuPeerTypeSameBotPM` | `AttachMenuPeerTypeSameBotPM` | `(self, /, *args, **kwargs)` |
| `types` | `AuctionBidLevel` | `AuctionBidLevel` | `(self, pos: int, amount: int, date: Optional[datetime.datetime])` |
| `types` | `Authorization` | `Authorization` | `(self, hash: int, device_model: str, platform: str, system_version: str, api_id: int, app_name: str, app_version: str, date_created: Optional[datetime.datetime], date_active: Optional[datetime.datetime], ip: str, country: str, region: str, current: Optional[bool] = None, official_app: Optional[bool] = None, password_pending: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None, unconfirmed: Optional[bool] = None)` |
| `types` | `AutoDownloadSettings` | `AutoDownloadSettings` | `(self, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int, small_queue_active_operations_max: int, large_queue_active_operations_max: int, disabled: Optional[bool] = None, video_preload_large: Optional[bool] = None, audio_preload_next: Optional[bool] = None, phonecalls_less_data: Optional[bool] = None, stories_preload: Optional[bool] = None)` |
| `types` | `AutoSaveException` | `AutoSaveException` | `(self, peer: 'TypePeer', settings: 'TypeAutoSaveSettings')` |
| `types` | `AutoSaveSettings` | `AutoSaveSettings` | `(self, photos: Optional[bool] = None, videos: Optional[bool] = None, video_max_size: Optional[int] = None)` |
| `types` | `AvailableEffect` | `AvailableEffect` | `(self, id: int, emoticon: str, effect_sticker_id: int, premium_required: Optional[bool] = None, static_icon_id: Optional[int] = None, effect_animation_id: Optional[int] = None)` |
| `types` | `AvailableReaction` | `AvailableReaction` | `(self, reaction: str, title: str, static_icon: 'TypeDocument', appear_animation: 'TypeDocument', select_animation: 'TypeDocument', activate_animation: 'TypeDocument', effect_animation: 'TypeDocument', inactive: Optional[bool] = None, premium: Optional[bool] = None, around_animation: Optional[ForwardRef('TypeDocument')] = None, center_icon: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `BadMsgNotification` | `BadMsgNotification` | `(self, bad_msg_id: int, bad_msg_seqno: int, error_code: int)` |
| `types` | `BadServerSalt` | `BadServerSalt` | `(self, bad_msg_id: int, bad_msg_seqno: int, error_code: int, new_server_salt: int)` |
| `types` | `BankCardOpenUrl` | `BankCardOpenUrl` | `(self, url: str, name: str)` |
| `types` | `BaseThemeArctic` | `BaseThemeArctic` | `(self, /, *args, **kwargs)` |
| `types` | `BaseThemeClassic` | `BaseThemeClassic` | `(self, /, *args, **kwargs)` |
| `types` | `BaseThemeDay` | `BaseThemeDay` | `(self, /, *args, **kwargs)` |
| `types` | `BaseThemeNight` | `BaseThemeNight` | `(self, /, *args, **kwargs)` |
| `types` | `BaseThemeTinted` | `BaseThemeTinted` | `(self, /, *args, **kwargs)` |
| `types` | `BindAuthKeyInner` | `BindAuthKeyInner` | `(self, nonce: int, temp_auth_key_id: int, perm_auth_key_id: int, temp_session_id: int, expires_at: Optional[datetime.datetime])` |
| `types` | `Birthday` | `Birthday` | `(self, day: int, month: int, year: Optional[int] = None)` |
| `types` | `Boost` | `Boost` | `(self, id: str, date: Optional[datetime.datetime], expires: Optional[datetime.datetime], gift: Optional[bool] = None, giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, user_id: Optional[int] = None, giveaway_msg_id: Optional[int] = None, used_gift_slug: Optional[str] = None, multiplier: Optional[int] = None, stars: Optional[int] = None)` |
| `types` | `BotApp` | `BotApp` | `(self, id: int, access_hash: int, short_name: str, title: str, description: str, photo: 'TypePhoto', hash: int, document: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `BotAppNotModified` | `BotAppNotModified` | `(self, /, *args, **kwargs)` |
| `types` | `BotAppSettings` | `BotAppSettings` | `(self, placeholder_path: Optional[bytes] = None, background_color: Optional[int] = None, background_dark_color: Optional[int] = None, header_color: Optional[int] = None, header_dark_color: Optional[int] = None)` |
| `types` | `BotBusinessConnection` | `BotBusinessConnection` | `(self, connection_id: str, user_id: int, dc_id: int, date: Optional[datetime.datetime], disabled: Optional[bool] = None, rights: Optional[ForwardRef('TypeBusinessBotRights')] = None)` |
| `types` | `BotCommand` | `BotCommand` | `(self, command: str, description: str)` |
| `types` | `BotCommandScopeChatAdmins` | `BotCommandScopeChatAdmins` | `(self, /, *args, **kwargs)` |
| `types` | `BotCommandScopeChats` | `BotCommandScopeChats` | `(self, /, *args, **kwargs)` |
| `types` | `BotCommandScopeDefault` | `BotCommandScopeDefault` | `(self, /, *args, **kwargs)` |
| `types` | `BotCommandScopePeer` | `BotCommandScopePeer` | `(self, peer: 'TypeInputPeer')` |
| `types` | `BotCommandScopePeerAdmins` | `BotCommandScopePeerAdmins` | `(self, peer: 'TypeInputPeer')` |
| `types` | `BotCommandScopePeerUser` | `BotCommandScopePeerUser` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser')` |
| `types` | `BotCommandScopeUsers` | `BotCommandScopeUsers` | `(self, /, *args, **kwargs)` |
| `types` | `BotInfo` | `BotInfo` | `(self, has_preview_medias: Optional[bool] = None, user_id: Optional[int] = None, description: Optional[str] = None, description_photo: Optional[ForwardRef('TypePhoto')] = None, description_document: Optional[ForwardRef('TypeDocument')] = None, commands: Optional[List[ForwardRef('TypeBotCommand')]] = None, menu_button: Optional[ForwardRef('TypeBotMenuButton')] = None, privacy_policy_url: Optional[str] = None, app_settings: Optional[ForwardRef('TypeBotAppSettings')] = None, verifier_settings: Optional[ForwardRef('TypeBotVerifierSettings')] = None)` |
| `types` | `BotInlineMediaResult` | `BotInlineMediaResult` | `(self, id: str, type: str, send_message: 'TypeBotInlineMessage', photo: Optional[ForwardRef('TypePhoto')] = None, document: Optional[ForwardRef('TypeDocument')] = None, title: Optional[str] = None, description: Optional[str] = None)` |
| `types` | `BotInlineMessageMediaAuto` | `BotInlineMessageMediaAuto` | `(self, message: str, invert_media: Optional[bool] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineMessageMediaContact` | `BotInlineMessageMediaContact` | `(self, phone_number: str, first_name: str, last_name: str, vcard: str, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineMessageMediaGeo` | `BotInlineMessageMediaGeo` | `(self, geo: 'TypeGeoPoint', heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineMessageMediaInvoice` | `BotInlineMessageMediaInvoice` | `(self, title: str, description: str, currency: str, total_amount: int, shipping_address_requested: Optional[bool] = None, test: Optional[bool] = None, photo: Optional[ForwardRef('TypeWebDocument')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineMessageMediaVenue` | `BotInlineMessageMediaVenue` | `(self, geo: 'TypeGeoPoint', title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineMessageMediaWebPage` | `BotInlineMessageMediaWebPage` | `(self, message: str, url: str, invert_media: Optional[bool] = None, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, manual: Optional[bool] = None, safe: Optional[bool] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineMessageRichMessage` | `BotInlineMessageRichMessage` | `(self, rich_message: 'TypeRichMessage', reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineMessageText` | `BotInlineMessageText` | `(self, message: str, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `BotInlineResult` | `BotInlineResult` | `(self, id: str, type: str, send_message: 'TypeBotInlineMessage', title: Optional[str] = None, description: Optional[str] = None, url: Optional[str] = None, thumb: Optional[ForwardRef('TypeWebDocument')] = None, content: Optional[ForwardRef('TypeWebDocument')] = None)` |
| `types` | `BotMenuButton` | `BotMenuButton` | `(self, text: str, url: str)` |
| `types` | `BotMenuButtonCommands` | `BotMenuButtonCommands` | `(self, /, *args, **kwargs)` |
| `types` | `BotMenuButtonDefault` | `BotMenuButtonDefault` | `(self, /, *args, **kwargs)` |
| `types` | `BotPreviewMedia` | `BotPreviewMedia` | `(self, date: Optional[datetime.datetime], media: 'TypeMessageMedia')` |
| `types` | `BotVerification` | `BotVerification` | `(self, bot_id: int, icon: int, description: str)` |
| `types` | `BotVerifierSettings` | `BotVerifierSettings` | `(self, icon: int, company: str, can_modify_custom_description: Optional[bool] = None, custom_description: Optional[str] = None)` |
| `types` | `BusinessAwayMessage` | `BusinessAwayMessage` | `(self, shortcut_id: int, schedule: 'TypeBusinessAwayMessageSchedule', recipients: 'TypeBusinessRecipients', offline_only: Optional[bool] = None)` |
| `types` | `BusinessAwayMessageScheduleAlways` | `BusinessAwayMessageScheduleAlways` | `(self, /, *args, **kwargs)` |
| `types` | `BusinessAwayMessageScheduleCustom` | `BusinessAwayMessageScheduleCustom` | `(self, start_date: Optional[datetime.datetime], end_date: Optional[datetime.datetime])` |
| `types` | `BusinessAwayMessageScheduleOutsideWorkHours` | `BusinessAwayMessageScheduleOutsideWorkHours` | `(self, /, *args, **kwargs)` |
| `types` | `BusinessBotRecipients` | `BusinessBotRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[int]] = None, exclude_users: Optional[List[int]] = None)` |
| `types` | `BusinessBotRights` | `BusinessBotRights` | `(self, reply: Optional[bool] = None, read_messages: Optional[bool] = None, delete_sent_messages: Optional[bool] = None, delete_received_messages: Optional[bool] = None, edit_name: Optional[bool] = None, edit_bio: Optional[bool] = None, edit_profile_photo: Optional[bool] = None, edit_username: Optional[bool] = None, view_gifts: Optional[bool] = None, sell_gifts: Optional[bool] = None, change_gift_settings: Optional[bool] = None, transfer_and_upgrade_gifts: Optional[bool] = None, transfer_stars: Optional[bool] = None, manage_stories: Optional[bool] = None)` |
| `types` | `BusinessChatLink` | `BusinessChatLink` | `(self, link: str, message: str, views: int, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, title: Optional[str] = None)` |
| `types` | `BusinessGreetingMessage` | `BusinessGreetingMessage` | `(self, shortcut_id: int, recipients: 'TypeBusinessRecipients', no_activity_days: int)` |
| `types` | `BusinessIntro` | `BusinessIntro` | `(self, title: str, description: str, sticker: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `BusinessLocation` | `BusinessLocation` | `(self, address: str, geo_point: Optional[ForwardRef('TypeGeoPoint')] = None)` |
| `types` | `BusinessRecipients` | `BusinessRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[int]] = None)` |
| `types` | `BusinessWeeklyOpen` | `BusinessWeeklyOpen` | `(self, start_minute: int, end_minute: int)` |
| `types` | `BusinessWorkHours` | `BusinessWorkHours` | `(self, timezone_id: str, weekly_open: List[ForwardRef('TypeBusinessWeeklyOpen')], open_now: Optional[bool] = None)` |
| `types` | `CdnConfig` | `CdnConfig` | `(self, public_keys: List[ForwardRef('TypeCdnPublicKey')])` |
| `types` | `CdnPublicKey` | `CdnPublicKey` | `(self, dc_id: int, public_key: str)` |
| `types` | `Channel` | `Channel` | `(self, id: int, title: str, photo: 'TypeChatPhoto', date: Optional[datetime.datetime], creator: Optional[bool] = None, left: Optional[bool] = None, broadcast: Optional[bool] = None, verified: Optional[bool] = None, megagroup: Optional[bool] = None, restricted: Optional[bool] = None, signatures: Optional[bool] = None, min: Optional[bool] = None, scam: Optional[bool] = None, has_link: Optional[bool] = None, has_geo: Optional[bool] = None, slowmode_enabled: Optional[bool] = None, call_active: Optional[bool] = None, call_not_empty: Optional[bool] = None, fake: Optional[bool] = None, gigagroup: Optional[bool] = None, noforwards: Optional[bool] = None, join_to_send: Optional[bool] = None, join_request: Optional[bool] = None, forum: Optional[bool] = None, stories_hidden: Optional[bool] = None, stories_hidden_min: Optional[bool] = None, stories_unavailable: Optional[bool] = None, signature_profiles: Optional[bool] = None, autotranslation: Optional[bool] = None, broadcast_messages_allowed: Optional[bool] = None, monoforum: Optional[bool] = None, forum_tabs: Optional[bool] = None, access_hash: Optional[int] = None, username: Optional[str] = None, restriction_reason: Optional[List[ForwardRef('TypeRestrictionReason')]] = None, admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, banned_rights: Optional[ForwardRef('TypeChatBannedRights')] = None, default_banned_rights: Optional[ForwardRef('TypeChatBannedRights')] = None, participants_count: Optional[int] = None, usernames: Optional[List[ForwardRef('TypeUsername')]] = None, stories_max_id: Optional[ForwardRef('TypeRecentStory')] = None, color: Optional[ForwardRef('TypePeerColor')] = None, profile_color: Optional[ForwardRef('TypePeerColor')] = None, emoji_status: Optional[ForwardRef('TypeEmojiStatus')] = None, level: Optional[int] = None, subscription_until_date: Optional[datetime.datetime] = None, bot_verification_icon: Optional[int] = None, send_paid_messages_stars: Optional[int] = None, linked_monoforum_id: Optional[int] = None)` |
| `types` | `ChannelAdminLogEvent` | `ChannelAdminLogEvent` | `(self, id: int, date: Optional[datetime.datetime], user_id: int, action: 'TypeChannelAdminLogEventAction')` |
| `types` | `ChannelAdminLogEventActionChangeAbout` | `ChannelAdminLogEventActionChangeAbout` | `(self, prev_value: str, new_value: str)` |
| `types` | `ChannelAdminLogEventActionChangeAvailableReactions` | `ChannelAdminLogEventActionChangeAvailableReactions` | `(self, prev_value: 'TypeChatReactions', new_value: 'TypeChatReactions')` |
| `types` | `ChannelAdminLogEventActionChangeEmojiStatus` | `ChannelAdminLogEventActionChangeEmojiStatus` | `(self, prev_value: 'TypeEmojiStatus', new_value: 'TypeEmojiStatus')` |
| `types` | `ChannelAdminLogEventActionChangeEmojiStickerSet` | `ChannelAdminLogEventActionChangeEmojiStickerSet` | `(self, prev_stickerset: 'TypeInputStickerSet', new_stickerset: 'TypeInputStickerSet')` |
| `types` | `ChannelAdminLogEventActionChangeHistoryTTL` | `ChannelAdminLogEventActionChangeHistoryTTL` | `(self, prev_value: int, new_value: int)` |
| `types` | `ChannelAdminLogEventActionChangeLinkedChat` | `ChannelAdminLogEventActionChangeLinkedChat` | `(self, prev_value: int, new_value: int)` |
| `types` | `ChannelAdminLogEventActionChangeLocation` | `ChannelAdminLogEventActionChangeLocation` | `(self, prev_value: 'TypeChannelLocation', new_value: 'TypeChannelLocation')` |
| `types` | `ChannelAdminLogEventActionChangePeerColor` | `ChannelAdminLogEventActionChangePeerColor` | `(self, prev_value: 'TypePeerColor', new_value: 'TypePeerColor')` |
| `types` | `ChannelAdminLogEventActionChangePhoto` | `ChannelAdminLogEventActionChangePhoto` | `(self, prev_photo: 'TypePhoto', new_photo: 'TypePhoto')` |
| `types` | `ChannelAdminLogEventActionChangeProfilePeerColor` | `ChannelAdminLogEventActionChangeProfilePeerColor` | `(self, prev_value: 'TypePeerColor', new_value: 'TypePeerColor')` |
| `types` | `ChannelAdminLogEventActionChangeStickerSet` | `ChannelAdminLogEventActionChangeStickerSet` | `(self, prev_stickerset: 'TypeInputStickerSet', new_stickerset: 'TypeInputStickerSet')` |
| `types` | `ChannelAdminLogEventActionChangeTitle` | `ChannelAdminLogEventActionChangeTitle` | `(self, prev_value: str, new_value: str)` |
| `types` | `ChannelAdminLogEventActionChangeUsername` | `ChannelAdminLogEventActionChangeUsername` | `(self, prev_value: str, new_value: str)` |
| `types` | `ChannelAdminLogEventActionChangeUsernames` | `ChannelAdminLogEventActionChangeUsernames` | `(self, prev_value: List[str], new_value: List[str])` |
| `types` | `ChannelAdminLogEventActionChangeWallpaper` | `ChannelAdminLogEventActionChangeWallpaper` | `(self, prev_value: 'TypeWallPaper', new_value: 'TypeWallPaper')` |
| `types` | `ChannelAdminLogEventActionCreateTopic` | `ChannelAdminLogEventActionCreateTopic` | `(self, topic: 'TypeForumTopic')` |
| `types` | `ChannelAdminLogEventActionDefaultBannedRights` | `ChannelAdminLogEventActionDefaultBannedRights` | `(self, prev_banned_rights: 'TypeChatBannedRights', new_banned_rights: 'TypeChatBannedRights')` |
| `types` | `ChannelAdminLogEventActionDeleteMessage` | `ChannelAdminLogEventActionDeleteMessage` | `(self, message: 'TypeMessage')` |
| `types` | `ChannelAdminLogEventActionDeleteTopic` | `ChannelAdminLogEventActionDeleteTopic` | `(self, topic: 'TypeForumTopic')` |
| `types` | `ChannelAdminLogEventActionDiscardGroupCall` | `ChannelAdminLogEventActionDiscardGroupCall` | `(self, call: 'TypeInputGroupCall')` |
| `types` | `ChannelAdminLogEventActionEditMessage` | `ChannelAdminLogEventActionEditMessage` | `(self, prev_message: 'TypeMessage', new_message: 'TypeMessage')` |
| `types` | `ChannelAdminLogEventActionEditTopic` | `ChannelAdminLogEventActionEditTopic` | `(self, prev_topic: 'TypeForumTopic', new_topic: 'TypeForumTopic')` |
| `types` | `ChannelAdminLogEventActionExportedInviteDelete` | `ChannelAdminLogEventActionExportedInviteDelete` | `(self, invite: 'TypeExportedChatInvite')` |
| `types` | `ChannelAdminLogEventActionExportedInviteEdit` | `ChannelAdminLogEventActionExportedInviteEdit` | `(self, prev_invite: 'TypeExportedChatInvite', new_invite: 'TypeExportedChatInvite')` |
| `types` | `ChannelAdminLogEventActionExportedInviteRevoke` | `ChannelAdminLogEventActionExportedInviteRevoke` | `(self, invite: 'TypeExportedChatInvite')` |
| `types` | `ChannelAdminLogEventActionParticipantEditRank` | `ChannelAdminLogEventActionParticipantEditRank` | `(self, user_id: int, prev_rank: str, new_rank: str)` |
| `types` | `ChannelAdminLogEventActionParticipantInvite` | `ChannelAdminLogEventActionParticipantInvite` | `(self, participant: 'TypeChannelParticipant')` |
| `types` | `ChannelAdminLogEventActionParticipantJoin` | `ChannelAdminLogEventActionParticipantJoin` | `(self, /, *args, **kwargs)` |
| `types` | `ChannelAdminLogEventActionParticipantJoinByInvite` | `ChannelAdminLogEventActionParticipantJoinByInvite` | `(self, invite: 'TypeExportedChatInvite', via_chatlist: Optional[bool] = None)` |
| `types` | `ChannelAdminLogEventActionParticipantJoinByRequest` | `ChannelAdminLogEventActionParticipantJoinByRequest` | `(self, invite: 'TypeExportedChatInvite', approved_by: int)` |
| `types` | `ChannelAdminLogEventActionParticipantLeave` | `ChannelAdminLogEventActionParticipantLeave` | `(self, /, *args, **kwargs)` |
| `types` | `ChannelAdminLogEventActionParticipantMute` | `ChannelAdminLogEventActionParticipantMute` | `(self, participant: 'TypeGroupCallParticipant')` |
| `types` | `ChannelAdminLogEventActionParticipantSubExtend` | `ChannelAdminLogEventActionParticipantSubExtend` | `(self, prev_participant: 'TypeChannelParticipant', new_participant: 'TypeChannelParticipant')` |
| `types` | `ChannelAdminLogEventActionParticipantToggleAdmin` | `ChannelAdminLogEventActionParticipantToggleAdmin` | `(self, prev_participant: 'TypeChannelParticipant', new_participant: 'TypeChannelParticipant')` |
| `types` | `ChannelAdminLogEventActionParticipantToggleBan` | `ChannelAdminLogEventActionParticipantToggleBan` | `(self, prev_participant: 'TypeChannelParticipant', new_participant: 'TypeChannelParticipant')` |
| `types` | `ChannelAdminLogEventActionParticipantUnmute` | `ChannelAdminLogEventActionParticipantUnmute` | `(self, participant: 'TypeGroupCallParticipant')` |
| `types` | `ChannelAdminLogEventActionParticipantVolume` | `ChannelAdminLogEventActionParticipantVolume` | `(self, participant: 'TypeGroupCallParticipant')` |
| `types` | `ChannelAdminLogEventActionPinTopic` | `ChannelAdminLogEventActionPinTopic` | `(self, prev_topic: Optional[ForwardRef('TypeForumTopic')] = None, new_topic: Optional[ForwardRef('TypeForumTopic')] = None)` |
| `types` | `ChannelAdminLogEventActionSendMessage` | `ChannelAdminLogEventActionSendMessage` | `(self, message: 'TypeMessage')` |
| `types` | `ChannelAdminLogEventActionStartGroupCall` | `ChannelAdminLogEventActionStartGroupCall` | `(self, call: 'TypeInputGroupCall')` |
| `types` | `ChannelAdminLogEventActionStopPoll` | `ChannelAdminLogEventActionStopPoll` | `(self, message: 'TypeMessage')` |
| `types` | `ChannelAdminLogEventActionToggleAntiSpam` | `ChannelAdminLogEventActionToggleAntiSpam` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionToggleAutotranslation` | `ChannelAdminLogEventActionToggleAutotranslation` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionToggleForum` | `ChannelAdminLogEventActionToggleForum` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionToggleGroupCallSetting` | `ChannelAdminLogEventActionToggleGroupCallSetting` | `(self, join_muted: bool)` |
| `types` | `ChannelAdminLogEventActionToggleInvites` | `ChannelAdminLogEventActionToggleInvites` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionToggleNoForwards` | `ChannelAdminLogEventActionToggleNoForwards` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionTogglePreHistoryHidden` | `ChannelAdminLogEventActionTogglePreHistoryHidden` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionToggleSignatureProfiles` | `ChannelAdminLogEventActionToggleSignatureProfiles` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionToggleSignatures` | `ChannelAdminLogEventActionToggleSignatures` | `(self, new_value: bool)` |
| `types` | `ChannelAdminLogEventActionToggleSlowMode` | `ChannelAdminLogEventActionToggleSlowMode` | `(self, prev_value: int, new_value: int)` |
| `types` | `ChannelAdminLogEventActionUpdatePinned` | `ChannelAdminLogEventActionUpdatePinned` | `(self, message: 'TypeMessage')` |
| `types` | `ChannelAdminLogEventsFilter` | `ChannelAdminLogEventsFilter` | `(self, join: Optional[bool] = None, leave: Optional[bool] = None, invite: Optional[bool] = None, ban: Optional[bool] = None, unban: Optional[bool] = None, kick: Optional[bool] = None, unkick: Optional[bool] = None, promote: Optional[bool] = None, demote: Optional[bool] = None, info: Optional[bool] = None, settings: Optional[bool] = None, pinned: Optional[bool] = None, edit: Optional[bool] = None, delete: Optional[bool] = None, group_call: Optional[bool] = None, invites: Optional[bool] = None, send: Optional[bool] = None, forums: Optional[bool] = None, sub_extend: Optional[bool] = None, edit_rank: Optional[bool] = None)` |
| `types` | `ChannelForbidden` | `ChannelForbidden` | `(self, id: int, access_hash: int, title: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, monoforum: Optional[bool] = None, until_date: Optional[datetime.datetime] = None)` |
| `types` | `ChannelFull` | `ChannelFull` | `(self, id: int, about: str, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, chat_photo: 'TypePhoto', notify_settings: 'TypePeerNotifySettings', bot_info: List[ForwardRef('TypeBotInfo')], pts: int, can_view_participants: Optional[bool] = None, can_set_username: Optional[bool] = None, can_set_stickers: Optional[bool] = None, hidden_prehistory: Optional[bool] = None, can_set_location: Optional[bool] = None, has_scheduled: Optional[bool] = None, can_view_stats: Optional[bool] = None, blocked: Optional[bool] = None, can_delete_channel: Optional[bool] = None, antispam: Optional[bool] = None, participants_hidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, view_forum_as_messages: Optional[bool] = None, restricted_sponsored: Optional[bool] = None, can_view_revenue: Optional[bool] = None, paid_media_allowed: Optional[bool] = None, can_view_stars_revenue: Optional[bool] = None, paid_reactions_available: Optional[bool] = None, stargifts_available: Optional[bool] = None, paid_messages_available: Optional[bool] = None, participants_count: Optional[int] = None, admins_count: Optional[int] = None, kicked_count: Optional[int] = None, banned_count: Optional[int] = None, online_count: Optional[int] = None, exported_invite: Optional[ForwardRef('TypeExportedChatInvite')] = None, migrated_from_chat_id: Optional[int] = None, migrated_from_max_id: Optional[int] = None, pinned_msg_id: Optional[int] = None, stickerset: Optional[ForwardRef('TypeStickerSet')] = None, available_min_id: Optional[int] = None, folder_id: Optional[int] = None, linked_chat_id: Optional[int] = None, location: Optional[ForwardRef('TypeChannelLocation')] = None, slowmode_seconds: Optional[int] = None, slowmode_next_send_date: Optional[datetime.datetime] = None, stats_dc: Optional[int] = None, call: Optional[ForwardRef('TypeInputGroupCall')] = None, ttl_period: Optional[int] = None, pending_suggestions: Optional[List[str]] = None, groupcall_default_join_as: Optional[ForwardRef('TypePeer')] = None, theme_emoticon: Optional[str] = None, requests_pending: Optional[int] = None, recent_requesters: Optional[List[int]] = None, default_send_as: Optional[ForwardRef('TypePeer')] = None, available_reactions: Optional[ForwardRef('TypeChatReactions')] = None, reactions_limit: Optional[int] = None, stories: Optional[ForwardRef('TypePeerStories')] = None, wallpaper: Optional[ForwardRef('TypeWallPaper')] = None, boosts_applied: Optional[int] = None, boosts_unrestrict: Optional[int] = None, emojiset: Optional[ForwardRef('TypeStickerSet')] = None, bot_verification: Optional[ForwardRef('TypeBotVerification')] = None, stargifts_count: Optional[int] = None, send_paid_messages_stars: Optional[int] = None, main_tab: Optional[ForwardRef('TypeProfileTab')] = None, guard_bot_id: Optional[int] = None)` |
| `types` | `ChannelLocation` | `ChannelLocation` | `(self, geo_point: 'TypeGeoPoint', address: str)` |
| `types` | `ChannelLocationEmpty` | `ChannelLocationEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `ChannelMessagesFilter` | `ChannelMessagesFilter` | `(self, ranges: List[ForwardRef('TypeMessageRange')], exclude_new_messages: Optional[bool] = None)` |
| `types` | `ChannelMessagesFilterEmpty` | `ChannelMessagesFilterEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `ChannelParticipant` | `ChannelParticipant` | `(self, user_id: int, date: Optional[datetime.datetime], subscription_until_date: Optional[datetime.datetime] = None, rank: Optional[str] = None)` |
| `types` | `ChannelParticipantAdmin` | `ChannelParticipantAdmin` | `(self, user_id: int, promoted_by: int, date: Optional[datetime.datetime], admin_rights: 'TypeChatAdminRights', can_edit: Optional[bool] = None, is_self: Optional[bool] = None, inviter_id: Optional[int] = None, rank: Optional[str] = None)` |
| `types` | `ChannelParticipantBanned` | `ChannelParticipantBanned` | `(self, peer: 'TypePeer', kicked_by: int, date: Optional[datetime.datetime], banned_rights: 'TypeChatBannedRights', left: Optional[bool] = None, rank: Optional[str] = None)` |
| `types` | `ChannelParticipantCreator` | `ChannelParticipantCreator` | `(self, user_id: int, admin_rights: 'TypeChatAdminRights', rank: Optional[str] = None)` |
| `types` | `ChannelParticipantLeft` | `ChannelParticipantLeft` | `(self, peer: 'TypePeer')` |
| `types` | `ChannelParticipantSelf` | `ChannelParticipantSelf` | `(self, user_id: int, inviter_id: int, date: Optional[datetime.datetime], via_request: Optional[bool] = None, subscription_until_date: Optional[datetime.datetime] = None, rank: Optional[str] = None)` |
| `types` | `ChannelParticipantsAdmins` | `ChannelParticipantsAdmins` | `(self, /, *args, **kwargs)` |
| `types` | `ChannelParticipantsBanned` | `ChannelParticipantsBanned` | `(self, q: str)` |
| `types` | `ChannelParticipantsBots` | `ChannelParticipantsBots` | `(self, /, *args, **kwargs)` |
| `types` | `ChannelParticipantsContacts` | `ChannelParticipantsContacts` | `(self, q: str)` |
| `types` | `ChannelParticipantsKicked` | `ChannelParticipantsKicked` | `(self, q: str)` |
| `types` | `ChannelParticipantsMentions` | `ChannelParticipantsMentions` | `(self, q: Optional[str] = None, top_msg_id: Optional[int] = None)` |
| `types` | `ChannelParticipantsRecent` | `ChannelParticipantsRecent` | `(self, /, *args, **kwargs)` |
| `types` | `ChannelParticipantsSearch` | `ChannelParticipantsSearch` | `(self, q: str)` |
| `types` | `Chat` | `Chat` | `(self, id: int, title: str, photo: 'TypeChatPhoto', participants_count: int, date: Optional[datetime.datetime], version: int, creator: Optional[bool] = None, left: Optional[bool] = None, deactivated: Optional[bool] = None, call_active: Optional[bool] = None, call_not_empty: Optional[bool] = None, noforwards: Optional[bool] = None, migrated_to: Optional[ForwardRef('TypeInputChannel')] = None, admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, default_banned_rights: Optional[ForwardRef('TypeChatBannedRights')] = None)` |
| `types` | `ChatAdminRights` | `ChatAdminRights` | `(self, change_info: Optional[bool] = None, post_messages: Optional[bool] = None, edit_messages: Optional[bool] = None, delete_messages: Optional[bool] = None, ban_users: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, add_admins: Optional[bool] = None, anonymous: Optional[bool] = None, manage_call: Optional[bool] = None, other: Optional[bool] = None, manage_topics: Optional[bool] = None, post_stories: Optional[bool] = None, edit_stories: Optional[bool] = None, delete_stories: Optional[bool] = None, manage_direct_messages: Optional[bool] = None, manage_ranks: Optional[bool] = None)` |
| `types` | `ChatAdminWithInvites` | `ChatAdminWithInvites` | `(self, admin_id: int, invites_count: int, revoked_invites_count: int)` |
| `types` | `ChatBannedRights` | `ChatBannedRights` | `(self, until_date: Optional[datetime.datetime], view_messages: Optional[bool] = None, send_messages: Optional[bool] = None, send_media: Optional[bool] = None, send_stickers: Optional[bool] = None, send_gifs: Optional[bool] = None, send_games: Optional[bool] = None, send_inline: Optional[bool] = None, embed_links: Optional[bool] = None, send_polls: Optional[bool] = None, change_info: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, manage_topics: Optional[bool] = None, send_photos: Optional[bool] = None, send_videos: Optional[bool] = None, send_roundvideos: Optional[bool] = None, send_audios: Optional[bool] = None, send_voices: Optional[bool] = None, send_docs: Optional[bool] = None, send_plain: Optional[bool] = None, edit_rank: Optional[bool] = None, send_reactions: Optional[bool] = None)` |
| `types` | `ChatEmpty` | `ChatEmpty` | `(self, id: int)` |
| `types` | `ChatForbidden` | `ChatForbidden` | `(self, id: int, title: str)` |
| `types` | `ChatFull` | `ChatFull` | `(self, id: int, about: str, participants: 'TypeChatParticipants', notify_settings: 'TypePeerNotifySettings', can_set_username: Optional[bool] = None, has_scheduled: Optional[bool] = None, translations_disabled: Optional[bool] = None, chat_photo: Optional[ForwardRef('TypePhoto')] = None, exported_invite: Optional[ForwardRef('TypeExportedChatInvite')] = None, bot_info: Optional[List[ForwardRef('TypeBotInfo')]] = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, call: Optional[ForwardRef('TypeInputGroupCall')] = None, ttl_period: Optional[int] = None, groupcall_default_join_as: Optional[ForwardRef('TypePeer')] = None, theme_emoticon: Optional[str] = None, requests_pending: Optional[int] = None, recent_requesters: Optional[List[int]] = None, available_reactions: Optional[ForwardRef('TypeChatReactions')] = None, reactions_limit: Optional[int] = None)` |
| `types` | `ChatInvite` | `ChatInvite` | `(self, title: str, photo: 'TypePhoto', participants_count: int, color: int, channel: Optional[bool] = None, broadcast: Optional[bool] = None, public: Optional[bool] = None, megagroup: Optional[bool] = None, request_needed: Optional[bool] = None, verified: Optional[bool] = None, scam: Optional[bool] = None, fake: Optional[bool] = None, can_refulfill_subscription: Optional[bool] = None, about: Optional[str] = None, participants: Optional[List[ForwardRef('TypeUser')]] = None, subscription_pricing: Optional[ForwardRef('TypeStarsSubscriptionPricing')] = None, subscription_form_id: Optional[int] = None, bot_verification: Optional[ForwardRef('TypeBotVerification')] = None)` |
| `types` | `ChatInviteAlready` | `ChatInviteAlready` | `(self, chat: 'TypeChat')` |
| `types` | `ChatInviteExported` | `ChatInviteExported` | `(self, link: str, admin_id: int, date: Optional[datetime.datetime], revoked: Optional[bool] = None, permanent: Optional[bool] = None, request_needed: Optional[bool] = None, start_date: Optional[datetime.datetime] = None, expire_date: Optional[datetime.datetime] = None, usage_limit: Optional[int] = None, usage: Optional[int] = None, requested: Optional[int] = None, subscription_expired: Optional[int] = None, title: Optional[str] = None, subscription_pricing: Optional[ForwardRef('TypeStarsSubscriptionPricing')] = None)` |
| `types` | `ChatInviteImporter` | `ChatInviteImporter` | `(self, user_id: int, date: Optional[datetime.datetime], requested: Optional[bool] = None, via_chatlist: Optional[bool] = None, about: Optional[str] = None, approved_by: Optional[int] = None)` |
| `types` | `ChatInvitePeek` | `ChatInvitePeek` | `(self, chat: 'TypeChat', expires: Optional[datetime.datetime])` |
| `types` | `ChatInvitePublicJoinRequests` | `ChatInvitePublicJoinRequests` | `(self, /, *args, **kwargs)` |
| `types` | `ChatOnlines` | `ChatOnlines` | `(self, onlines: int)` |
| `types` | `ChatParticipant` | `ChatParticipant` | `(self, user_id: int, inviter_id: int, date: Optional[datetime.datetime], rank: Optional[str] = None)` |
| `types` | `ChatParticipantAdmin` | `ChatParticipantAdmin` | `(self, user_id: int, inviter_id: int, date: Optional[datetime.datetime], rank: Optional[str] = None)` |
| `types` | `ChatParticipantCreator` | `ChatParticipantCreator` | `(self, user_id: int, rank: Optional[str] = None)` |
| `types` | `ChatParticipants` | `ChatParticipants` | `(self, chat_id: int, participants: List[ForwardRef('TypeChatParticipant')], version: int)` |
| `types` | `ChatParticipantsForbidden` | `ChatParticipantsForbidden` | `(self, chat_id: int, self_participant: Optional[ForwardRef('TypeChatParticipant')] = None)` |
| `types` | `ChatPhoto` | `ChatPhoto` | `(self, photo_id: int, dc_id: int, has_video: Optional[bool] = None, stripped_thumb: Optional[bytes] = None)` |
| `types` | `ChatPhotoEmpty` | `ChatPhotoEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `ChatReactionsAll` | `ChatReactionsAll` | `(self, allow_custom: Optional[bool] = None)` |
| `types` | `ChatReactionsNone` | `ChatReactionsNone` | `(self, /, *args, **kwargs)` |
| `types` | `ChatReactionsSome` | `ChatReactionsSome` | `(self, reactions: List[ForwardRef('TypeReaction')])` |
| `types` | `ChatTheme` | `ChatTheme` | `(self, emoticon: str)` |
| `types` | `ChatThemeUniqueGift` | `ChatThemeUniqueGift` | `(self, gift: 'TypeStarGift', theme_settings: List[ForwardRef('TypeThemeSettings')])` |
| `types` | `ClientDHInnerData` | `ClientDHInnerData` | `(self, nonce: int, server_nonce: int, retry_id: int, g_b: bytes)` |
| `types` | `CodeSettings` | `CodeSettings` | `(self, allow_flashcall: Optional[bool] = None, current_number: Optional[bool] = None, allow_app_hash: Optional[bool] = None, allow_missed_call: Optional[bool] = None, allow_firebase: Optional[bool] = None, unknown_number: Optional[bool] = None, logout_tokens: Optional[List[bytes]] = None, token: Optional[str] = None, app_sandbox: Optional[bool] = None)` |
| `types` | `Config` | `Config` | `(self, date: Optional[datetime.datetime], expires: Optional[datetime.datetime], test_mode: bool, this_dc: int, dc_options: List[ForwardRef('TypeDcOption')], dc_txt_domain_name: str, chat_size_max: int, megagroup_size_max: int, forwarded_count_max: int, online_update_period_ms: int, offline_blur_timeout_ms: int, offline_idle_timeout_ms: int, online_cloud_timeout_ms: int, notify_cloud_delay_ms: int, notify_default_delay_ms: int, push_chat_period_ms: int, push_chat_limit: int, edit_time_limit: int, revoke_time_limit: int, revoke_pm_time_limit: int, rating_e_decay: int, stickers_recent_limit: int, channels_read_media_period: int, call_receive_timeout_ms: int, call_ring_timeout_ms: int, call_connect_timeout_ms: int, call_packet_timeout_ms: int, me_url_prefix: str, caption_length_max: int, message_length_max: int, webfile_dc_id: int, default_p2p_contacts: Optional[bool] = None, preload_featured_stickers: Optional[bool] = None, revoke_pm_inbox: Optional[bool] = None, blocked_mode: Optional[bool] = None, force_try_ipv6: Optional[bool] = None, tmp_sessions: Optional[int] = None, autoupdate_url_prefix: Optional[str] = None, gif_search_username: Optional[str] = None, venue_search_username: Optional[str] = None, img_search_username: Optional[str] = None, static_maps_provider: Optional[str] = None, suggested_lang_code: Optional[str] = None, lang_pack_version: Optional[int] = None, base_lang_pack_version: Optional[int] = None, reactions_default: Optional[ForwardRef('TypeReaction')] = None, autologin_token: Optional[str] = None)` |
| `types` | `ConnectedBot` | `ConnectedBot` | `(self, bot_id: int, recipients: 'TypeBusinessBotRecipients', rights: 'TypeBusinessBotRights', device: Optional[str] = None, date: Optional[datetime.datetime] = None, location: Optional[str] = None)` |
| `types` | `ConnectedBotStarRef` | `ConnectedBotStarRef` | `(self, url: str, date: Optional[datetime.datetime], bot_id: int, commission_permille: int, participants: int, revenue: int, revoked: Optional[bool] = None, duration_months: Optional[int] = None)` |
| `types` | `Contact` | `Contact` | `(self, user_id: int, mutual: bool)` |
| `types` | `ContactBirthday` | `ContactBirthday` | `(self, contact_id: int, birthday: 'TypeBirthday')` |
| `types` | `ContactStatus` | `ContactStatus` | `(self, user_id: int, status: 'TypeUserStatus')` |
| `types` | `DataJSON` | `DataJSON` | `(self, data: str)` |
| `types` | `DcOption` | `DcOption` | `(self, id: int, ip_address: str, port: int, ipv6: Optional[bool] = None, media_only: Optional[bool] = None, tcpo_only: Optional[bool] = None, cdn: Optional[bool] = None, static: Optional[bool] = None, this_port_only: Optional[bool] = None, secret: Optional[bytes] = None)` |
| `types` | `DefaultHistoryTTL` | `DefaultHistoryTTL` | `(self, period: int)` |
| `types` | `DestroyAuthKeyFail` | `DestroyAuthKeyFail` | `(self, /, *args, **kwargs)` |
| `types` | `DestroyAuthKeyNone` | `DestroyAuthKeyNone` | `(self, /, *args, **kwargs)` |
| `types` | `DestroyAuthKeyOk` | `DestroyAuthKeyOk` | `(self, /, *args, **kwargs)` |
| `types` | `DestroySessionNone` | `DestroySessionNone` | `(self, session_id: int)` |
| `types` | `DestroySessionOk` | `DestroySessionOk` | `(self, session_id: int)` |
| `types` | `DhGenFail` | `DhGenFail` | `(self, nonce: int, server_nonce: int, new_nonce_hash3: int)` |
| `types` | `DhGenOk` | `DhGenOk` | `(self, nonce: int, server_nonce: int, new_nonce_hash1: int)` |
| `types` | `DhGenRetry` | `DhGenRetry` | `(self, nonce: int, server_nonce: int, new_nonce_hash2: int)` |
| `types` | `Dialog` | `Dialog` | `(self, peer: 'TypePeer', top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, unread_poll_votes_count: int, notify_settings: 'TypePeerNotifySettings', pinned: Optional[bool] = None, unread_mark: Optional[bool] = None, view_forum_as_messages: Optional[bool] = None, pts: Optional[int] = None, draft: Optional[ForwardRef('TypeDraftMessage')] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None)` |
| `types` | `DialogFilter` | `DialogFilter` | `(self, id: int, title: 'TypeTextWithEntities', pinned_peers: List[ForwardRef('TypeInputPeer')], include_peers: List[ForwardRef('TypeInputPeer')], exclude_peers: List[ForwardRef('TypeInputPeer')], contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, groups: Optional[bool] = None, broadcasts: Optional[bool] = None, bots: Optional[bool] = None, exclude_muted: Optional[bool] = None, exclude_read: Optional[bool] = None, exclude_archived: Optional[bool] = None, title_noanimate: Optional[bool] = None, emoticon: Optional[str] = None, color: Optional[int] = None)` |
| `types` | `DialogFilterChatlist` | `DialogFilterChatlist` | `(self, id: int, title: 'TypeTextWithEntities', pinned_peers: List[ForwardRef('TypeInputPeer')], include_peers: List[ForwardRef('TypeInputPeer')], has_my_invites: Optional[bool] = None, title_noanimate: Optional[bool] = None, emoticon: Optional[str] = None, color: Optional[int] = None)` |
| `types` | `DialogFilterDefault` | `DialogFilterDefault` | `(self, /, *args, **kwargs)` |
| `types` | `DialogFilterSuggested` | `DialogFilterSuggested` | `(self, filter: 'TypeDialogFilter', description: str)` |
| `types` | `DialogFolder` | `DialogFolder` | `(self, folder: 'TypeFolder', peer: 'TypePeer', top_message: int, unread_muted_peers_count: int, unread_unmuted_peers_count: int, unread_muted_messages_count: int, unread_unmuted_messages_count: int, pinned: Optional[bool] = None)` |
| `types` | `DialogPeer` | `DialogPeer` | `(self, peer: 'TypePeer')` |
| `types` | `DialogPeerFolder` | `DialogPeerFolder` | `(self, folder_id: int)` |
| `types` | `DisallowedGiftsSettings` | `DisallowedGiftsSettings` | `(self, disallow_unlimited_stargifts: Optional[bool] = None, disallow_limited_stargifts: Optional[bool] = None, disallow_unique_stargifts: Optional[bool] = None, disallow_premium_gifts: Optional[bool] = None, disallow_stargifts_from_channels: Optional[bool] = None)` |
| `types` | `Document` | `Document` | `(self, id: int, access_hash: int, file_reference: bytes, date: Optional[datetime.datetime], mime_type: str, size: int, dc_id: int, attributes: List[ForwardRef('TypeDocumentAttribute')], thumbs: Optional[List[ForwardRef('TypePhotoSize')]] = None, video_thumbs: Optional[List[ForwardRef('TypeVideoSize')]] = None)` |
| `types` | `DocumentAttributeAnimated` | `DocumentAttributeAnimated` | `(self, /, *args, **kwargs)` |
| `types` | `DocumentAttributeAudio` | `DocumentAttributeAudio` | `(self, duration: int, voice: Optional[bool] = None, title: Optional[str] = None, performer: Optional[str] = None, waveform: Optional[bytes] = None)` |
| `types` | `DocumentAttributeCustomEmoji` | `DocumentAttributeCustomEmoji` | `(self, alt: str, stickerset: 'TypeInputStickerSet', free: Optional[bool] = None, text_color: Optional[bool] = None)` |
| `types` | `DocumentAttributeFilename` | `DocumentAttributeFilename` | `(self, file_name: str)` |
| `types` | `DocumentAttributeHasStickers` | `DocumentAttributeHasStickers` | `(self, /, *args, **kwargs)` |
| `types` | `DocumentAttributeImageSize` | `DocumentAttributeImageSize` | `(self, w: int, h: int)` |
| `types` | `DocumentAttributeSticker` | `DocumentAttributeSticker` | `(self, alt: str, stickerset: 'TypeInputStickerSet', mask: Optional[bool] = None, mask_coords: Optional[ForwardRef('TypeMaskCoords')] = None)` |
| `types` | `DocumentAttributeVideo` | `DocumentAttributeVideo` | `(self, duration: float, w: int, h: int, round_message: Optional[bool] = None, supports_streaming: Optional[bool] = None, nosound: Optional[bool] = None, preload_prefix_size: Optional[int] = None, video_start_ts: Optional[float] = None, video_codec: Optional[str] = None)` |
| `types` | `DocumentEmpty` | `DocumentEmpty` | `(self, id: int)` |
| `types` | `DraftMessage` | `DraftMessage` | `(self, message: str, date: Optional[datetime.datetime], no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, effect: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None, rich_message: Optional[ForwardRef('TypeRichMessage')] = None)` |
| `types` | `DraftMessageEmpty` | `DraftMessageEmpty` | `(self, date: Optional[datetime.datetime] = None)` |
| `types` | `EmailVerificationApple` | `EmailVerificationApple` | `(self, token: str)` |
| `types` | `EmailVerificationCode` | `EmailVerificationCode` | `(self, code: str)` |
| `types` | `EmailVerificationGoogle` | `EmailVerificationGoogle` | `(self, token: str)` |
| `types` | `EmailVerifyPurposeLoginChange` | `EmailVerifyPurposeLoginChange` | `(self, /, *args, **kwargs)` |
| `types` | `EmailVerifyPurposeLoginSetup` | `EmailVerifyPurposeLoginSetup` | `(self, phone_number: str, phone_code_hash: str)` |
| `types` | `EmailVerifyPurposePassport` | `EmailVerifyPurposePassport` | `(self, /, *args, **kwargs)` |
| `types` | `EmojiGroup` | `EmojiGroup` | `(self, title: str, icon_emoji_id: int, emoticons: List[str])` |
| `types` | `EmojiGroupGreeting` | `EmojiGroupGreeting` | `(self, title: str, icon_emoji_id: int, emoticons: List[str])` |
| `types` | `EmojiGroupPremium` | `EmojiGroupPremium` | `(self, title: str, icon_emoji_id: int)` |
| `types` | `EmojiKeyword` | `EmojiKeyword` | `(self, keyword: str, emoticons: List[str])` |
| `types` | `EmojiKeywordDeleted` | `EmojiKeywordDeleted` | `(self, keyword: str, emoticons: List[str])` |
| `types` | `EmojiKeywordsDifference` | `EmojiKeywordsDifference` | `(self, lang_code: str, from_version: int, version: int, keywords: List[ForwardRef('TypeEmojiKeyword')])` |
| `types` | `EmojiLanguage` | `EmojiLanguage` | `(self, lang_code: str)` |
| `types` | `EmojiList` | `EmojiList` | `(self, hash: int, document_id: List[int])` |
| `types` | `EmojiListNotModified` | `EmojiListNotModified` | `(self, /, *args, **kwargs)` |
| `types` | `EmojiStatus` | `EmojiStatus` | `(self, document_id: int, until: Optional[datetime.datetime] = None)` |
| `types` | `EmojiStatusCollectible` | `EmojiStatusCollectible` | `(self, collectible_id: int, document_id: int, title: str, slug: str, pattern_document_id: int, center_color: int, edge_color: int, pattern_color: int, text_color: int, until: Optional[datetime.datetime] = None)` |
| `types` | `EmojiStatusEmpty` | `EmojiStatusEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `EmojiURL` | `EmojiURL` | `(self, url: str)` |
| `types` | `EncryptedChat` | `EncryptedChat` | `(self, id: int, access_hash: int, date: Optional[datetime.datetime], admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int)` |
| `types` | `EncryptedChatDiscarded` | `EncryptedChatDiscarded` | `(self, id: int, history_deleted: Optional[bool] = None)` |
| `types` | `EncryptedChatEmpty` | `EncryptedChatEmpty` | `(self, id: int)` |
| `types` | `EncryptedChatRequested` | `EncryptedChatRequested` | `(self, id: int, access_hash: int, date: Optional[datetime.datetime], admin_id: int, participant_id: int, g_a: bytes, folder_id: Optional[int] = None)` |
| `types` | `EncryptedChatWaiting` | `EncryptedChatWaiting` | `(self, id: int, access_hash: int, date: Optional[datetime.datetime], admin_id: int, participant_id: int)` |
| `types` | `EncryptedFile` | `EncryptedFile` | `(self, id: int, access_hash: int, size: int, dc_id: int, key_fingerprint: int)` |
| `types` | `EncryptedFileEmpty` | `EncryptedFileEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `EncryptedMessage` | `EncryptedMessage` | `(self, chat_id: int, date: Optional[datetime.datetime], bytes: bytes, file: 'TypeEncryptedFile', random_id: int = None)` |
| `types` | `EncryptedMessageService` | `EncryptedMessageService` | `(self, chat_id: int, date: Optional[datetime.datetime], bytes: bytes, random_id: int = None)` |
| `types` | `ExportedChatlistInvite` | `ExportedChatlistInvite` | `(self, title: str, url: str, peers: List[ForwardRef('TypePeer')])` |
| `types` | `ExportedContactToken` | `ExportedContactToken` | `(self, url: str, expires: Optional[datetime.datetime])` |
| `types` | `ExportedMessageLink` | `ExportedMessageLink` | `(self, link: str, html: str)` |
| `types` | `ExportedStoryLink` | `ExportedStoryLink` | `(self, link: str)` |
| `types` | `FactCheck` | `FactCheck` | `(self, hash: int, need_check: Optional[bool] = None, country: Optional[str] = None, text: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `FileHash` | `FileHash` | `(self, offset: int, limit: int, hash: bytes)` |
| `types` | `Folder` | `Folder` | `(self, id: int, title: str, autofill_new_broadcasts: Optional[bool] = None, autofill_public_groups: Optional[bool] = None, autofill_new_correspondents: Optional[bool] = None, photo: Optional[ForwardRef('TypeChatPhoto')] = None)` |
| `types` | `FolderPeer` | `FolderPeer` | `(self, peer: 'TypePeer', folder_id: int)` |
| `types` | `ForumTopic` | `ForumTopic` | `(self, id: int, date: Optional[datetime.datetime], peer: 'TypePeer', title: str, icon_color: int, top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, unread_poll_votes_count: int, from_id: 'TypePeer', notify_settings: 'TypePeerNotifySettings', my: Optional[bool] = None, closed: Optional[bool] = None, pinned: Optional[bool] = None, short: Optional[bool] = None, hidden: Optional[bool] = None, title_missing: Optional[bool] = None, icon_emoji_id: Optional[int] = None, draft: Optional[ForwardRef('TypeDraftMessage')] = None)` |
| `types` | `ForumTopicDeleted` | `ForumTopicDeleted` | `(self, id: int)` |
| `types` | `FoundStory` | `FoundStory` | `(self, peer: 'TypePeer', story: 'TypeStoryItem')` |
| `types` | `FutureSalt` | `FutureSalt` | `(self, valid_since: Optional[datetime.datetime], valid_until: Optional[datetime.datetime], salt: int)` |
| `types` | `FutureSalts` | `FutureSalts` | `(self, req_msg_id: int, now: int, salts: List[ForwardRef('Typefuture_salt')])` |
| `types` | `Game` | `Game` | `(self, id: int, access_hash: int, short_name: str, title: str, description: str, photo: 'TypePhoto', document: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `GeoPoint` | `GeoPoint` | `(self, long: float, lat: float, access_hash: int, accuracy_radius: Optional[int] = None)` |
| `types` | `GeoPointAddress` | `GeoPointAddress` | `(self, country_iso2: str, state: Optional[str] = None, city: Optional[str] = None, street: Optional[str] = None)` |
| `types` | `GeoPointEmpty` | `GeoPointEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `GlobalPrivacySettings` | `GlobalPrivacySettings` | `(self, archive_and_mute_new_noncontact_peers: Optional[bool] = None, keep_archived_unmuted: Optional[bool] = None, keep_archived_folders: Optional[bool] = None, hide_read_marks: Optional[bool] = None, new_noncontact_peers_require_premium: Optional[bool] = None, display_gifts_button: Optional[bool] = None, noncontact_peers_paid_stars: Optional[int] = None, disallowed_gifts: Optional[ForwardRef('TypeDisallowedGiftsSettings')] = None)` |
| `types` | `GroupCall` | `GroupCall` | `(self, id: int, access_hash: int, participants_count: int, unmuted_video_limit: int, version: int, join_muted: Optional[bool] = None, can_change_join_muted: Optional[bool] = None, join_date_asc: Optional[bool] = None, schedule_start_subscribed: Optional[bool] = None, can_start_video: Optional[bool] = None, record_video_active: Optional[bool] = None, rtmp_stream: Optional[bool] = None, listeners_hidden: Optional[bool] = None, conference: Optional[bool] = None, creator: Optional[bool] = None, messages_enabled: Optional[bool] = None, can_change_messages_enabled: Optional[bool] = None, min: Optional[bool] = None, title: Optional[str] = None, stream_dc_id: Optional[int] = None, record_start_date: Optional[datetime.datetime] = None, schedule_date: Optional[datetime.datetime] = None, unmuted_video_count: Optional[int] = None, invite_link: Optional[str] = None, send_paid_messages_stars: Optional[int] = None, default_send_as: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `GroupCallDiscarded` | `GroupCallDiscarded` | `(self, id: int, access_hash: int, duration: int)` |
| `types` | `GroupCallDonor` | `GroupCallDonor` | `(self, stars: int, top: Optional[bool] = None, my: Optional[bool] = None, peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `GroupCallMessage` | `GroupCallMessage` | `(self, id: int, from_id: 'TypePeer', date: Optional[datetime.datetime], message: 'TypeTextWithEntities', from_admin: Optional[bool] = None, paid_message_stars: Optional[int] = None)` |
| `types` | `GroupCallParticipant` | `GroupCallParticipant` | `(self, peer: 'TypePeer', date: Optional[datetime.datetime], source: int, muted: Optional[bool] = None, left: Optional[bool] = None, can_self_unmute: Optional[bool] = None, just_joined: Optional[bool] = None, versioned: Optional[bool] = None, min: Optional[bool] = None, muted_by_you: Optional[bool] = None, volume_by_admin: Optional[bool] = None, is_self: Optional[bool] = None, video_joined: Optional[bool] = None, active_date: Optional[datetime.datetime] = None, volume: Optional[int] = None, about: Optional[str] = None, raise_hand_rating: Optional[int] = None, video: Optional[ForwardRef('TypeGroupCallParticipantVideo')] = None, presentation: Optional[ForwardRef('TypeGroupCallParticipantVideo')] = None, paid_stars_total: Optional[int] = None)` |
| `types` | `GroupCallParticipantVideo` | `GroupCallParticipantVideo` | `(self, endpoint: str, source_groups: List[ForwardRef('TypeGroupCallParticipantVideoSourceGroup')], paused: Optional[bool] = None, audio_source: Optional[int] = None)` |
| `types` | `GroupCallParticipantVideoSourceGroup` | `GroupCallParticipantVideoSourceGroup` | `(self, semantics: str, sources: List[int])` |
| `types` | `GroupCallStreamChannel` | `GroupCallStreamChannel` | `(self, channel: int, scale: int, last_timestamp_ms: int)` |
| `types` | `HighScore` | `HighScore` | `(self, pos: int, user_id: int, score: int)` |
| `types` | `HttpWait` | `HttpWait` | `(self, max_delay: int, wait_after: int, max_wait: int)` |
| `types` | `ImportedContact` | `ImportedContact` | `(self, user_id: int, client_id: int)` |
| `types` | `InlineBotSwitchPM` | `InlineBotSwitchPM` | `(self, text: str, start_param: str)` |
| `types` | `InlineBotWebView` | `InlineBotWebView` | `(self, text: str, url: str)` |
| `types` | `InlineQueryPeerTypeBotPM` | `InlineQueryPeerTypeBotPM` | `(self, /, *args, **kwargs)` |
| `types` | `InlineQueryPeerTypeBroadcast` | `InlineQueryPeerTypeBroadcast` | `(self, /, *args, **kwargs)` |
| `types` | `InlineQueryPeerTypeChat` | `InlineQueryPeerTypeChat` | `(self, /, *args, **kwargs)` |
| `types` | `InlineQueryPeerTypeMegagroup` | `InlineQueryPeerTypeMegagroup` | `(self, /, *args, **kwargs)` |
| `types` | `InlineQueryPeerTypePM` | `InlineQueryPeerTypePM` | `(self, /, *args, **kwargs)` |
| `types` | `InlineQueryPeerTypeSameBotPM` | `InlineQueryPeerTypeSameBotPM` | `(self, /, *args, **kwargs)` |
| `types` | `InputAiComposeToneDefault` | `InputAiComposeToneDefault` | `(self, tone: str)` |
| `types` | `InputAiComposeToneID` | `InputAiComposeToneID` | `(self, id: int, access_hash: int)` |
| `types` | `InputAiComposeToneSlug` | `InputAiComposeToneSlug` | `(self, slug: str)` |
| `types` | `InputAppEvent` | `InputAppEvent` | `(self, time: float, type: str, peer: int, data: 'TypeJSONValue')` |
| `types` | `InputBotAppID` | `InputBotAppID` | `(self, id: int, access_hash: int)` |
| `types` | `InputBotAppShortName` | `InputBotAppShortName` | `(self, bot_id: 'TypeInputUser', short_name: str)` |
| `types` | `InputBotInlineMessageGame` | `InputBotInlineMessageGame` | `(self, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageID` | `InputBotInlineMessageID` | `(self, dc_id: int, id: int, access_hash: int)` |
| `types` | `InputBotInlineMessageID64` | `InputBotInlineMessageID64` | `(self, dc_id: int, owner_id: int, id: int, access_hash: int)` |
| `types` | `InputBotInlineMessageMediaAuto` | `InputBotInlineMessageMediaAuto` | `(self, message: str, invert_media: Optional[bool] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageMediaContact` | `InputBotInlineMessageMediaContact` | `(self, phone_number: str, first_name: str, last_name: str, vcard: str, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageMediaGeo` | `InputBotInlineMessageMediaGeo` | `(self, geo_point: 'TypeInputGeoPoint', heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageMediaInvoice` | `InputBotInlineMessageMediaInvoice` | `(self, title: str, description: str, invoice: 'TypeInvoice', payload: bytes, provider: str, provider_data: 'TypeDataJSON', photo: Optional[ForwardRef('TypeInputWebDocument')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageMediaVenue` | `InputBotInlineMessageMediaVenue` | `(self, geo_point: 'TypeInputGeoPoint', title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageMediaWebPage` | `InputBotInlineMessageMediaWebPage` | `(self, message: str, url: str, invert_media: Optional[bool] = None, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageRichMessage` | `InputBotInlineMessageRichMessage` | `(self, rich_message: 'TypeInputRichMessage', reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineMessageText` | `InputBotInlineMessageText` | `(self, message: str, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None)` |
| `types` | `InputBotInlineResult` | `InputBotInlineResult` | `(self, id: str, type: str, send_message: 'TypeInputBotInlineMessage', title: Optional[str] = None, description: Optional[str] = None, url: Optional[str] = None, thumb: Optional[ForwardRef('TypeInputWebDocument')] = None, content: Optional[ForwardRef('TypeInputWebDocument')] = None)` |
| `types` | `InputBotInlineResultDocument` | `InputBotInlineResultDocument` | `(self, id: str, type: str, document: 'TypeInputDocument', send_message: 'TypeInputBotInlineMessage', title: Optional[str] = None, description: Optional[str] = None)` |
| `types` | `InputBotInlineResultGame` | `InputBotInlineResultGame` | `(self, id: str, short_name: str, send_message: 'TypeInputBotInlineMessage')` |
| `types` | `InputBotInlineResultPhoto` | `InputBotInlineResultPhoto` | `(self, id: str, type: str, photo: 'TypeInputPhoto', send_message: 'TypeInputBotInlineMessage')` |
| `types` | `InputBusinessAwayMessage` | `InputBusinessAwayMessage` | `(self, shortcut_id: int, schedule: 'TypeBusinessAwayMessageSchedule', recipients: 'TypeInputBusinessRecipients', offline_only: Optional[bool] = None)` |
| `types` | `InputBusinessBotRecipients` | `InputBusinessBotRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[ForwardRef('TypeInputUser')]] = None, exclude_users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `types` | `InputBusinessChatLink` | `InputBusinessChatLink` | `(self, message: str, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, title: Optional[str] = None)` |
| `types` | `InputBusinessGreetingMessage` | `InputBusinessGreetingMessage` | `(self, shortcut_id: int, recipients: 'TypeInputBusinessRecipients', no_activity_days: int)` |
| `types` | `InputBusinessIntro` | `InputBusinessIntro` | `(self, title: str, description: str, sticker: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `types` | `InputBusinessRecipients` | `InputBusinessRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `types` | `InputChannel` | `InputChannel` | `(self, channel_id: int, access_hash: int)` |
| `types` | `InputChannelEmpty` | `InputChannelEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputChannelFromMessage` | `InputChannelFromMessage` | `(self, peer: 'TypeInputPeer', msg_id: int, channel_id: int)` |
| `types` | `InputChatPhoto` | `InputChatPhoto` | `(self, id: 'TypeInputPhoto')` |
| `types` | `InputChatPhotoEmpty` | `InputChatPhotoEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputChatTheme` | `InputChatTheme` | `(self, emoticon: str)` |
| `types` | `InputChatThemeEmpty` | `InputChatThemeEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputChatThemeUniqueGift` | `InputChatThemeUniqueGift` | `(self, slug: str)` |
| `types` | `InputChatUploadedPhoto` | `InputChatUploadedPhoto` | `(self, file: Optional[ForwardRef('TypeInputFile')] = None, video: Optional[ForwardRef('TypeInputFile')] = None, video_start_ts: Optional[float] = None, video_emoji_markup: Optional[ForwardRef('TypeVideoSize')] = None)` |
| `types` | `InputChatlistDialogFilter` | `InputChatlistDialogFilter` | `(self, filter_id: int)` |
| `types` | `InputCheckPasswordEmpty` | `InputCheckPasswordEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputCheckPasswordSRP` | `InputCheckPasswordSRP` | `(self, srp_id: int, A: bytes, M1: bytes)` |
| `types` | `InputClientProxy` | `InputClientProxy` | `(self, address: str, port: int)` |
| `types` | `InputCollectiblePhone` | `InputCollectiblePhone` | `(self, phone: str)` |
| `types` | `InputCollectibleUsername` | `InputCollectibleUsername` | `(self, username: str)` |
| `types` | `InputDialogPeer` | `InputDialogPeer` | `(self, peer: 'TypeInputPeer')` |
| `types` | `InputDialogPeerFolder` | `InputDialogPeerFolder` | `(self, folder_id: int)` |
| `types` | `InputDocument` | `InputDocument` | `(self, id: int, access_hash: int, file_reference: bytes)` |
| `types` | `InputDocumentEmpty` | `InputDocumentEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputDocumentFileLocation` | `InputDocumentFileLocation` | `(self, id: int, access_hash: int, file_reference: bytes, thumb_size: str)` |
| `types` | `InputEmojiStatusCollectible` | `InputEmojiStatusCollectible` | `(self, collectible_id: int, until: Optional[datetime.datetime] = None)` |
| `types` | `InputEncryptedChat` | `InputEncryptedChat` | `(self, chat_id: int, access_hash: int)` |
| `types` | `InputEncryptedFile` | `InputEncryptedFile` | `(self, id: int, access_hash: int)` |
| `types` | `InputEncryptedFileBigUploaded` | `InputEncryptedFileBigUploaded` | `(self, id: int, parts: int, key_fingerprint: int)` |
| `types` | `InputEncryptedFileEmpty` | `InputEncryptedFileEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputEncryptedFileLocation` | `InputEncryptedFileLocation` | `(self, id: int, access_hash: int)` |
| `types` | `InputEncryptedFileUploaded` | `InputEncryptedFileUploaded` | `(self, id: int, parts: int, md5_checksum: str, key_fingerprint: int)` |
| `types` | `InputFile` | `InputFile` | `(self, id: int, parts: int, name: str, md5_checksum: str)` |
| `types` | `InputFileBig` | `InputFileBig` | `(self, id: int, parts: int, name: str)` |
| `types` | `InputFileLocation` | `InputFileLocation` | `(self, volume_id: int, local_id: int, secret: int, file_reference: bytes)` |
| `types` | `InputFileStoryDocument` | `InputFileStoryDocument` | `(self, id: 'TypeInputDocument')` |
| `types` | `InputFolderPeer` | `InputFolderPeer` | `(self, peer: 'TypeInputPeer', folder_id: int)` |
| `types` | `InputGameID` | `InputGameID` | `(self, id: int, access_hash: int)` |
| `types` | `InputGameShortName` | `InputGameShortName` | `(self, bot_id: 'TypeInputUser', short_name: str)` |
| `types` | `InputGeoPoint` | `InputGeoPoint` | `(self, lat: float, long: float, accuracy_radius: Optional[int] = None)` |
| `types` | `InputGeoPointEmpty` | `InputGeoPointEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputGroupCall` | `InputGroupCall` | `(self, id: int, access_hash: int)` |
| `types` | `InputGroupCallInviteMessage` | `InputGroupCallInviteMessage` | `(self, msg_id: int)` |
| `types` | `InputGroupCallSlug` | `InputGroupCallSlug` | `(self, slug: str)` |
| `types` | `InputGroupCallStream` | `InputGroupCallStream` | `(self, call: 'TypeInputGroupCall', time_ms: int, scale: int, video_channel: Optional[int] = None, video_quality: Optional[int] = None)` |
| `types` | `InputInvoiceBusinessBotTransferStars` | `InputInvoiceBusinessBotTransferStars` | `(self, bot: 'TypeInputUser', stars: int)` |
| `types` | `InputInvoiceChatInviteSubscription` | `InputInvoiceChatInviteSubscription` | `(self, hash: str)` |
| `types` | `InputInvoiceMessage` | `InputInvoiceMessage` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `types` | `InputInvoicePremiumAuthCode` | `InputInvoicePremiumAuthCode` | `(self, purpose: 'TypeInputStorePaymentPurpose')` |
| `types` | `InputInvoicePremiumGiftCode` | `InputInvoicePremiumGiftCode` | `(self, purpose: 'TypeInputStorePaymentPurpose', option: 'TypePremiumGiftCodeOption')` |
| `types` | `InputInvoicePremiumGiftStars` | `InputInvoicePremiumGiftStars` | `(self, user_id: 'TypeInputUser', months: int, message: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `InputInvoiceSlug` | `InputInvoiceSlug` | `(self, slug: str)` |
| `types` | `InputInvoiceStarGift` | `InputInvoiceStarGift` | `(self, peer: 'TypeInputPeer', gift_id: int, hide_name: Optional[bool] = None, include_upgrade: Optional[bool] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `InputInvoiceStarGiftAuctionBid` | `InputInvoiceStarGiftAuctionBid` | `(self, gift_id: int, bid_amount: int, hide_name: Optional[bool] = None, update_bid: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `InputInvoiceStarGiftDropOriginalDetails` | `InputInvoiceStarGiftDropOriginalDetails` | `(self, stargift: 'TypeInputSavedStarGift')` |
| `types` | `InputInvoiceStarGiftPrepaidUpgrade` | `InputInvoiceStarGiftPrepaidUpgrade` | `(self, peer: 'TypeInputPeer', hash: str)` |
| `types` | `InputInvoiceStarGiftResale` | `InputInvoiceStarGiftResale` | `(self, slug: str, to_id: 'TypeInputPeer', ton: Optional[bool] = None)` |
| `types` | `InputInvoiceStarGiftTransfer` | `InputInvoiceStarGiftTransfer` | `(self, stargift: 'TypeInputSavedStarGift', to_id: 'TypeInputPeer')` |
| `types` | `InputInvoiceStarGiftUpgrade` | `InputInvoiceStarGiftUpgrade` | `(self, stargift: 'TypeInputSavedStarGift', keep_original_details: Optional[bool] = None)` |
| `types` | `InputInvoiceStars` | `InputInvoiceStars` | `(self, purpose: 'TypeInputStorePaymentPurpose')` |
| `types` | `InputKeyboardButtonRequestPeer` | `InputKeyboardButtonRequestPeer` | `(self, text: str, button_id: int, peer_type: 'TypeRequestPeerType', max_quantity: int, name_requested: Optional[bool] = None, username_requested: Optional[bool] = None, photo_requested: Optional[bool] = None, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `InputKeyboardButtonUrlAuth` | `InputKeyboardButtonUrlAuth` | `(self, text: str, url: str, bot: 'TypeInputUser', request_write_access: Optional[bool] = None, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None, fwd_text: Optional[str] = None)` |
| `types` | `InputKeyboardButtonUserProfile` | `InputKeyboardButtonUserProfile` | `(self, text: str, user_id: 'TypeInputUser', style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `InputMediaAreaChannelPost` | `InputMediaAreaChannelPost` | `(self, coordinates: 'TypeMediaAreaCoordinates', channel: 'TypeInputChannel', msg_id: int)` |
| `types` | `InputMediaAreaVenue` | `InputMediaAreaVenue` | `(self, coordinates: 'TypeMediaAreaCoordinates', query_id: int, result_id: str)` |
| `types` | `InputMediaContact` | `InputMediaContact` | `(self, phone_number: str, first_name: str, last_name: str, vcard: str)` |
| `types` | `InputMediaDice` | `InputMediaDice` | `(self, emoticon: str)` |
| `types` | `InputMediaDocument` | `InputMediaDocument` | `(self, id: 'TypeInputDocument', spoiler: Optional[bool] = None, video_cover: Optional[ForwardRef('TypeInputPhoto')] = None, video_timestamp: Optional[int] = None, ttl_seconds: Optional[int] = None, query: Optional[str] = None)` |
| `types` | `InputMediaDocumentExternal` | `InputMediaDocumentExternal` | `(self, url: str, spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None, video_cover: Optional[ForwardRef('TypeInputPhoto')] = None, video_timestamp: Optional[int] = None)` |
| `types` | `InputMediaEmpty` | `InputMediaEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputMediaGame` | `InputMediaGame` | `(self, id: 'TypeInputGame')` |
| `types` | `InputMediaGeoLive` | `InputMediaGeoLive` | `(self, geo_point: 'TypeInputGeoPoint', stopped: Optional[bool] = None, heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None)` |
| `types` | `InputMediaGeoPoint` | `InputMediaGeoPoint` | `(self, geo_point: 'TypeInputGeoPoint')` |
| `types` | `InputMediaInvoice` | `InputMediaInvoice` | `(self, title: str, description: str, invoice: 'TypeInvoice', payload: bytes, provider_data: 'TypeDataJSON', photo: Optional[ForwardRef('TypeInputWebDocument')] = None, provider: Optional[str] = None, start_param: Optional[str] = None, extended_media: Optional[ForwardRef('TypeInputMedia')] = None)` |
| `types` | `InputMediaPaidMedia` | `InputMediaPaidMedia` | `(self, stars_amount: int, extended_media: List[ForwardRef('TypeInputMedia')], payload: Optional[str] = None)` |
| `types` | `InputMediaPhoto` | `InputMediaPhoto` | `(self, id: 'TypeInputPhoto', spoiler: Optional[bool] = None, live_photo: Optional[bool] = None, ttl_seconds: Optional[int] = None, video: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `types` | `InputMediaPhotoExternal` | `InputMediaPhotoExternal` | `(self, url: str, spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None)` |
| `types` | `InputMediaPoll` | `InputMediaPoll` | `(self, poll: 'TypePoll', correct_answers: Optional[List[int]] = None, attached_media: Optional[ForwardRef('TypeInputMedia')] = None, solution: Optional[str] = None, solution_entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, solution_media: Optional[ForwardRef('TypeInputMedia')] = None)` |
| `types` | `InputMediaStakeDice` | `InputMediaStakeDice` | `(self, game_hash: str, ton_amount: int, client_seed: bytes)` |
| `types` | `InputMediaStory` | `InputMediaStory` | `(self, peer: 'TypeInputPeer', id: int)` |
| `types` | `InputMediaTodo` | `InputMediaTodo` | `(self, todo: 'TypeTodoList')` |
| `types` | `InputMediaUploadedDocument` | `InputMediaUploadedDocument` | `(self, file: 'TypeInputFile', mime_type: str, attributes: List[ForwardRef('TypeDocumentAttribute')], nosound_video: Optional[bool] = None, force_file: Optional[bool] = None, spoiler: Optional[bool] = None, thumb: Optional[ForwardRef('TypeInputFile')] = None, stickers: Optional[List[ForwardRef('TypeInputDocument')]] = None, video_cover: Optional[ForwardRef('TypeInputPhoto')] = None, video_timestamp: Optional[int] = None, ttl_seconds: Optional[int] = None)` |
| `types` | `InputMediaUploadedPhoto` | `InputMediaUploadedPhoto` | `(self, file: 'TypeInputFile', spoiler: Optional[bool] = None, live_photo: Optional[bool] = None, stickers: Optional[List[ForwardRef('TypeInputDocument')]] = None, ttl_seconds: Optional[int] = None, video: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `types` | `InputMediaVenue` | `InputMediaVenue` | `(self, geo_point: 'TypeInputGeoPoint', title: str, address: str, provider: str, venue_id: str, venue_type: str)` |
| `types` | `InputMediaWebPage` | `InputMediaWebPage` | `(self, url: str, force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, optional: Optional[bool] = None)` |
| `types` | `InputMessageCallbackQuery` | `InputMessageCallbackQuery` | `(self, id: int, query_id: int)` |
| `types` | `InputMessageEntityMentionName` | `InputMessageEntityMentionName` | `(self, offset: int, length: int, user_id: 'TypeInputUser')` |
| `types` | `InputMessageID` | `InputMessageID` | `(self, id: int)` |
| `types` | `InputMessagePinned` | `InputMessagePinned` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessageReadMetric` | `InputMessageReadMetric` | `(self, msg_id: int, view_id: int, time_in_view_ms: int, active_time_in_view_ms: int, height_to_viewport_ratio_permille: int, seen_range_ratio_permille: int)` |
| `types` | `InputMessageReplyTo` | `InputMessageReplyTo` | `(self, id: int)` |
| `types` | `InputMessagesFilterChatPhotos` | `InputMessagesFilterChatPhotos` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterContacts` | `InputMessagesFilterContacts` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterDocument` | `InputMessagesFilterDocument` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterEmpty` | `InputMessagesFilterEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterGeo` | `InputMessagesFilterGeo` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterGif` | `InputMessagesFilterGif` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterMusic` | `InputMessagesFilterMusic` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterMyMentions` | `InputMessagesFilterMyMentions` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterPhoneCalls` | `InputMessagesFilterPhoneCalls` | `(self, missed: Optional[bool] = None)` |
| `types` | `InputMessagesFilterPhotoVideo` | `InputMessagesFilterPhotoVideo` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterPhotos` | `InputMessagesFilterPhotos` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterPinned` | `InputMessagesFilterPinned` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterPoll` | `InputMessagesFilterPoll` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterRoundVideo` | `InputMessagesFilterRoundVideo` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterRoundVoice` | `InputMessagesFilterRoundVoice` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterUrl` | `InputMessagesFilterUrl` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterVideo` | `InputMessagesFilterVideo` | `(self, /, *args, **kwargs)` |
| `types` | `InputMessagesFilterVoice` | `InputMessagesFilterVoice` | `(self, /, *args, **kwargs)` |
| `types` | `InputNotifyBroadcasts` | `InputNotifyBroadcasts` | `(self, /, *args, **kwargs)` |
| `types` | `InputNotifyChats` | `InputNotifyChats` | `(self, /, *args, **kwargs)` |
| `types` | `InputNotifyForumTopic` | `InputNotifyForumTopic` | `(self, peer: 'TypeInputPeer', top_msg_id: int)` |
| `types` | `InputNotifyPeer` | `InputNotifyPeer` | `(self, peer: 'TypeInputPeer')` |
| `types` | `InputNotifyUsers` | `InputNotifyUsers` | `(self, /, *args, **kwargs)` |
| `types` | `InputPageBlockMap` | `InputPageBlockMap` | `(self, geo: 'TypeInputGeoPoint', zoom: int, w: int, h: int, caption: 'TypePageCaption')` |
| `types` | `InputPasskeyCredentialFirebasePNV` | `InputPasskeyCredentialFirebasePNV` | `(self, pnv_token: str)` |
| `types` | `InputPasskeyCredentialPublicKey` | `InputPasskeyCredentialPublicKey` | `(self, id: str, raw_id: str, response: 'TypeInputPasskeyResponse')` |
| `types` | `InputPasskeyResponseLogin` | `InputPasskeyResponseLogin` | `(self, client_data: 'TypeDataJSON', authenticator_data: bytes, signature: bytes, user_handle: str)` |
| `types` | `InputPasskeyResponseRegister` | `InputPasskeyResponseRegister` | `(self, client_data: 'TypeDataJSON', attestation_data: bytes)` |
| `types` | `InputPaymentCredentials` | `InputPaymentCredentials` | `(self, data: 'TypeDataJSON', save: Optional[bool] = None)` |
| `types` | `InputPaymentCredentialsApplePay` | `InputPaymentCredentialsApplePay` | `(self, payment_data: 'TypeDataJSON')` |
| `types` | `InputPaymentCredentialsGooglePay` | `InputPaymentCredentialsGooglePay` | `(self, payment_token: 'TypeDataJSON')` |
| `types` | `InputPaymentCredentialsSaved` | `InputPaymentCredentialsSaved` | `(self, id: str, tmp_password: bytes)` |
| `types` | `InputPeerChannel` | `InputPeerChannel` | `(self, channel_id: int, access_hash: int)` |
| `types` | `InputPeerChannelFromMessage` | `InputPeerChannelFromMessage` | `(self, peer: 'TypeInputPeer', msg_id: int, channel_id: int)` |
| `types` | `InputPeerChat` | `InputPeerChat` | `(self, chat_id: int)` |
| `types` | `InputPeerColorCollectible` | `InputPeerColorCollectible` | `(self, collectible_id: int)` |
| `types` | `InputPeerEmpty` | `InputPeerEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputPeerNotifySettings` | `InputPeerNotifySettings` | `(self, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[datetime.datetime] = None, sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_sound: Optional[ForwardRef('TypeNotificationSound')] = None)` |
| `types` | `InputPeerPhotoFileLocation` | `InputPeerPhotoFileLocation` | `(self, peer: 'TypeInputPeer', photo_id: int, big: Optional[bool] = None)` |
| `types` | `InputPeerSelf` | `InputPeerSelf` | `(self, /, *args, **kwargs)` |
| `types` | `InputPeerUser` | `InputPeerUser` | `(self, user_id: int, access_hash: int)` |
| `types` | `InputPeerUserFromMessage` | `InputPeerUserFromMessage` | `(self, peer: 'TypeInputPeer', msg_id: int, user_id: int)` |
| `types` | `InputPhoneCall` | `InputPhoneCall` | `(self, id: int, access_hash: int)` |
| `types` | `InputPhoneContact` | `InputPhoneContact` | `(self, client_id: int, phone: str, first_name: str, last_name: str, note: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `InputPhoto` | `InputPhoto` | `(self, id: int, access_hash: int, file_reference: bytes)` |
| `types` | `InputPhotoEmpty` | `InputPhotoEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputPhotoFileLocation` | `InputPhotoFileLocation` | `(self, id: int, access_hash: int, file_reference: bytes, thumb_size: str)` |
| `types` | `InputPhotoLegacyFileLocation` | `InputPhotoLegacyFileLocation` | `(self, id: int, access_hash: int, file_reference: bytes, volume_id: int, local_id: int, secret: int)` |
| `types` | `InputPollAnswer` | `InputPollAnswer` | `(self, text: 'TypeTextWithEntities', media: Optional[ForwardRef('TypeInputMedia')] = None)` |
| `types` | `InputPrivacyKeyAbout` | `InputPrivacyKeyAbout` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyAddedByPhone` | `InputPrivacyKeyAddedByPhone` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyBirthday` | `InputPrivacyKeyBirthday` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyChatInvite` | `InputPrivacyKeyChatInvite` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyForwards` | `InputPrivacyKeyForwards` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyNoPaidMessages` | `InputPrivacyKeyNoPaidMessages` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyPhoneCall` | `InputPrivacyKeyPhoneCall` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyPhoneNumber` | `InputPrivacyKeyPhoneNumber` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyPhoneP2P` | `InputPrivacyKeyPhoneP2P` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyProfilePhoto` | `InputPrivacyKeyProfilePhoto` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeySavedMusic` | `InputPrivacyKeySavedMusic` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyStarGiftsAutoSave` | `InputPrivacyKeyStarGiftsAutoSave` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyStatusTimestamp` | `InputPrivacyKeyStatusTimestamp` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyKeyVoiceMessages` | `InputPrivacyKeyVoiceMessages` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueAllowAll` | `InputPrivacyValueAllowAll` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueAllowBots` | `InputPrivacyValueAllowBots` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueAllowChatParticipants` | `InputPrivacyValueAllowChatParticipants` | `(self, chats: List[int])` |
| `types` | `InputPrivacyValueAllowCloseFriends` | `InputPrivacyValueAllowCloseFriends` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueAllowContacts` | `InputPrivacyValueAllowContacts` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueAllowPremium` | `InputPrivacyValueAllowPremium` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueAllowUsers` | `InputPrivacyValueAllowUsers` | `(self, users: List[ForwardRef('TypeInputUser')])` |
| `types` | `InputPrivacyValueDisallowAll` | `InputPrivacyValueDisallowAll` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueDisallowBots` | `InputPrivacyValueDisallowBots` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueDisallowChatParticipants` | `InputPrivacyValueDisallowChatParticipants` | `(self, chats: List[int])` |
| `types` | `InputPrivacyValueDisallowContacts` | `InputPrivacyValueDisallowContacts` | `(self, /, *args, **kwargs)` |
| `types` | `InputPrivacyValueDisallowUsers` | `InputPrivacyValueDisallowUsers` | `(self, users: List[ForwardRef('TypeInputUser')])` |
| `types` | `InputQuickReplyShortcut` | `InputQuickReplyShortcut` | `(self, shortcut: str)` |
| `types` | `InputQuickReplyShortcutId` | `InputQuickReplyShortcutId` | `(self, shortcut_id: int)` |
| `types` | `InputReplyToMessage` | `InputReplyToMessage` | `(self, reply_to_msg_id: int, top_msg_id: Optional[int] = None, reply_to_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, quote_text: Optional[str] = None, quote_entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, quote_offset: Optional[int] = None, monoforum_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, todo_item_id: Optional[int] = None, poll_option: Optional[bytes] = None)` |
| `types` | `InputReplyToMonoForum` | `InputReplyToMonoForum` | `(self, monoforum_peer_id: 'TypeInputPeer')` |
| `types` | `InputReplyToStory` | `InputReplyToStory` | `(self, peer: 'TypeInputPeer', story_id: int)` |
| `types` | `InputReportReasonChildAbuse` | `InputReportReasonChildAbuse` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonCopyright` | `InputReportReasonCopyright` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonFake` | `InputReportReasonFake` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonGeoIrrelevant` | `InputReportReasonGeoIrrelevant` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonIllegalDrugs` | `InputReportReasonIllegalDrugs` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonOther` | `InputReportReasonOther` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonPersonalDetails` | `InputReportReasonPersonalDetails` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonPornography` | `InputReportReasonPornography` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonSpam` | `InputReportReasonSpam` | `(self, /, *args, **kwargs)` |
| `types` | `InputReportReasonViolence` | `InputReportReasonViolence` | `(self, /, *args, **kwargs)` |
| `types` | `InputRichFileDocument` | `InputRichFileDocument` | `(self, id: str, document: 'TypeInputDocument')` |
| `types` | `InputRichFilePhoto` | `InputRichFilePhoto` | `(self, id: str, photo: 'TypeInputPhoto')` |
| `types` | `InputRichMessage` | `InputRichMessage` | `(self, blocks: List[ForwardRef('TypePageBlock')], rtl: Optional[bool] = None, noautolink: Optional[bool] = None, photos: Optional[List[ForwardRef('TypeInputPhoto')]] = None, documents: Optional[List[ForwardRef('TypeInputDocument')]] = None, users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `types` | `InputRichMessageHTML` | `InputRichMessageHTML` | `(self, html: str, rtl: Optional[bool] = None, noautolink: Optional[bool] = None, files: Optional[List[ForwardRef('TypeInputRichFile')]] = None)` |
| `types` | `InputRichMessageMarkdown` | `InputRichMessageMarkdown` | `(self, markdown: str, rtl: Optional[bool] = None, noautolink: Optional[bool] = None, files: Optional[List[ForwardRef('TypeInputRichFile')]] = None)` |
| `types` | `InputSavedStarGiftChat` | `InputSavedStarGiftChat` | `(self, peer: 'TypeInputPeer', saved_id: int)` |
| `types` | `InputSavedStarGiftSlug` | `InputSavedStarGiftSlug` | `(self, slug: str)` |
| `types` | `InputSavedStarGiftUser` | `InputSavedStarGiftUser` | `(self, msg_id: int)` |
| `types` | `InputSecureFile` | `InputSecureFile` | `(self, id: int, access_hash: int)` |
| `types` | `InputSecureFileLocation` | `InputSecureFileLocation` | `(self, id: int, access_hash: int)` |
| `types` | `InputSecureFileUploaded` | `InputSecureFileUploaded` | `(self, id: int, parts: int, md5_checksum: str, file_hash: bytes, secret: bytes)` |
| `types` | `InputSecureValue` | `InputSecureValue` | `(self, type: 'TypeSecureValueType', data: Optional[ForwardRef('TypeSecureData')] = None, front_side: Optional[ForwardRef('TypeInputSecureFile')] = None, reverse_side: Optional[ForwardRef('TypeInputSecureFile')] = None, selfie: Optional[ForwardRef('TypeInputSecureFile')] = None, translation: Optional[List[ForwardRef('TypeInputSecureFile')]] = None, files: Optional[List[ForwardRef('TypeInputSecureFile')]] = None, plain_data: Optional[ForwardRef('TypeSecurePlainData')] = None)` |
| `types` | `InputSendMessageRichMessageDraftAction` | `InputSendMessageRichMessageDraftAction` | `(self, rich_message: 'TypeInputRichMessage', random_id: int = None)` |
| `types` | `InputSingleMedia` | `InputSingleMedia` | `(self, media: 'TypeInputMedia', message: str, random_id: int = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None)` |
| `types` | `InputStarGiftAuction` | `InputStarGiftAuction` | `(self, gift_id: int)` |
| `types` | `InputStarGiftAuctionSlug` | `InputStarGiftAuctionSlug` | `(self, slug: str)` |
| `types` | `InputStarsTransaction` | `InputStarsTransaction` | `(self, id: str, refund: Optional[bool] = None)` |
| `types` | `InputStickerSetAnimatedEmoji` | `InputStickerSetAnimatedEmoji` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetAnimatedEmojiAnimations` | `InputStickerSetAnimatedEmojiAnimations` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetDice` | `InputStickerSetDice` | `(self, emoticon: str)` |
| `types` | `InputStickerSetEmojiChannelDefaultStatuses` | `InputStickerSetEmojiChannelDefaultStatuses` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetEmojiDefaultStatuses` | `InputStickerSetEmojiDefaultStatuses` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetEmojiDefaultTopicIcons` | `InputStickerSetEmojiDefaultTopicIcons` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetEmojiGenericAnimations` | `InputStickerSetEmojiGenericAnimations` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetEmpty` | `InputStickerSetEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetID` | `InputStickerSetID` | `(self, id: int, access_hash: int)` |
| `types` | `InputStickerSetItem` | `InputStickerSetItem` | `(self, document: 'TypeInputDocument', emoji: str, mask_coords: Optional[ForwardRef('TypeMaskCoords')] = None, keywords: Optional[str] = None)` |
| `types` | `InputStickerSetPremiumGifts` | `InputStickerSetPremiumGifts` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickerSetShortName` | `InputStickerSetShortName` | `(self, short_name: str)` |
| `types` | `InputStickerSetThumb` | `InputStickerSetThumb` | `(self, stickerset: 'TypeInputStickerSet', thumb_version: int)` |
| `types` | `InputStickerSetTonGifts` | `InputStickerSetTonGifts` | `(self, /, *args, **kwargs)` |
| `types` | `InputStickeredMediaDocument` | `InputStickeredMediaDocument` | `(self, id: 'TypeInputDocument')` |
| `types` | `InputStickeredMediaPhoto` | `InputStickeredMediaPhoto` | `(self, id: 'TypeInputPhoto')` |
| `types` | `InputStorePaymentAuthCode` | `InputStorePaymentAuthCode` | `(self, phone_number: str, phone_code_hash: str, premium_days: int, currency: str, amount: int, restore: Optional[bool] = None)` |
| `types` | `InputStorePaymentGiftPremium` | `InputStorePaymentGiftPremium` | `(self, user_id: 'TypeInputUser', currency: str, amount: int)` |
| `types` | `InputStorePaymentPremiumGiftCode` | `InputStorePaymentPremiumGiftCode` | `(self, users: List[ForwardRef('TypeInputUser')], currency: str, amount: int, boost_peer: Optional[ForwardRef('TypeInputPeer')] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `InputStorePaymentPremiumGiveaway` | `InputStorePaymentPremiumGiveaway` | `(self, boost_peer: 'TypeInputPeer', until_date: Optional[datetime.datetime], currency: str, amount: int, only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, additional_peers: Optional[List[ForwardRef('TypeInputPeer')]] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None, random_id: int = None)` |
| `types` | `InputStorePaymentPremiumSubscription` | `InputStorePaymentPremiumSubscription` | `(self, restore: Optional[bool] = None, upgrade: Optional[bool] = None)` |
| `types` | `InputStorePaymentStarsGift` | `InputStorePaymentStarsGift` | `(self, user_id: 'TypeInputUser', stars: int, currency: str, amount: int)` |
| `types` | `InputStorePaymentStarsGiveaway` | `InputStorePaymentStarsGiveaway` | `(self, stars: int, boost_peer: 'TypeInputPeer', until_date: Optional[datetime.datetime], currency: str, amount: int, users: int, only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, additional_peers: Optional[List[ForwardRef('TypeInputPeer')]] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None, random_id: int = None)` |
| `types` | `InputStorePaymentStarsTopup` | `InputStorePaymentStarsTopup` | `(self, stars: int, currency: str, amount: int, spend_purpose_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `types` | `InputTakeoutFileLocation` | `InputTakeoutFileLocation` | `(self, /, *args, **kwargs)` |
| `types` | `InputTheme` | `InputTheme` | `(self, id: int, access_hash: int)` |
| `types` | `InputThemeSettings` | `InputThemeSettings` | `(self, base_theme: 'TypeBaseTheme', accent_color: int, message_colors_animated: Optional[bool] = None, outbox_accent_color: Optional[int] = None, message_colors: Optional[List[int]] = None, wallpaper: Optional[ForwardRef('TypeInputWallPaper')] = None, wallpaper_settings: Optional[ForwardRef('TypeWallPaperSettings')] = None)` |
| `types` | `InputThemeSlug` | `InputThemeSlug` | `(self, slug: str)` |
| `types` | `InputUser` | `InputUser` | `(self, user_id: int, access_hash: int)` |
| `types` | `InputUserEmpty` | `InputUserEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `InputUserFromMessage` | `InputUserFromMessage` | `(self, peer: 'TypeInputPeer', msg_id: int, user_id: int)` |
| `types` | `InputUserSelf` | `InputUserSelf` | `(self, /, *args, **kwargs)` |
| `types` | `InputWallPaper` | `InputWallPaper` | `(self, id: int, access_hash: int)` |
| `types` | `InputWallPaperNoFile` | `InputWallPaperNoFile` | `(self, id: int)` |
| `types` | `InputWallPaperSlug` | `InputWallPaperSlug` | `(self, slug: str)` |
| `types` | `InputWebDocument` | `InputWebDocument` | `(self, url: str, size: int, mime_type: str, attributes: List[ForwardRef('TypeDocumentAttribute')])` |
| `types` | `InputWebFileAudioAlbumThumbLocation` | `InputWebFileAudioAlbumThumbLocation` | `(self, small: Optional[bool] = None, document: Optional[ForwardRef('TypeInputDocument')] = None, title: Optional[str] = None, performer: Optional[str] = None)` |
| `types` | `InputWebFileGeoPointLocation` | `InputWebFileGeoPointLocation` | `(self, geo_point: 'TypeInputGeoPoint', access_hash: int, w: int, h: int, zoom: int, scale: int)` |
| `types` | `InputWebFileLocation` | `InputWebFileLocation` | `(self, url: str, access_hash: int)` |
| `types` | `Invoice` | `Invoice` | `(self, currency: str, prices: List[ForwardRef('TypeLabeledPrice')], test: Optional[bool] = None, name_requested: Optional[bool] = None, phone_requested: Optional[bool] = None, email_requested: Optional[bool] = None, shipping_address_requested: Optional[bool] = None, flexible: Optional[bool] = None, phone_to_provider: Optional[bool] = None, email_to_provider: Optional[bool] = None, recurring: Optional[bool] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, terms_url: Optional[str] = None, subscription_period: Optional[int] = None)` |
| `types` | `IpPort` | `IpPort` | `(self, ipv4: int, port: int)` |
| `types` | `IpPortSecret` | `IpPortSecret` | `(self, ipv4: int, port: int, secret: bytes)` |
| `types` | `JoinChatBotResultApproved` | `JoinChatBotResultApproved` | `(self, /, *args, **kwargs)` |
| `types` | `JoinChatBotResultDeclined` | `JoinChatBotResultDeclined` | `(self, /, *args, **kwargs)` |
| `types` | `JoinChatBotResultQueued` | `JoinChatBotResultQueued` | `(self, /, *args, **kwargs)` |
| `types` | `JoinChatBotResultWebView` | `JoinChatBotResultWebView` | `(self, url: str)` |
| `types` | `JsonArray` | `JsonArray` | `(self, value: List[ForwardRef('TypeJSONValue')])` |
| `types` | `JsonBool` | `JsonBool` | `(self, value: bool)` |
| `types` | `JsonNull` | `JsonNull` | `(self, /, *args, **kwargs)` |
| `types` | `JsonNumber` | `JsonNumber` | `(self, value: float)` |
| `types` | `JsonObject` | `JsonObject` | `(self, value: List[ForwardRef('TypeJSONObjectValue')])` |
| `types` | `JsonObjectValue` | `JsonObjectValue` | `(self, key: str, value: 'TypeJSONValue')` |
| `types` | `JsonString` | `JsonString` | `(self, value: str)` |
| `types` | `KeyboardButton` | `KeyboardButton` | `(self, text: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonBuy` | `KeyboardButtonBuy` | `(self, text: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonCallback` | `KeyboardButtonCallback` | `(self, text: str, data: bytes, requires_password: Optional[bool] = None, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonCopy` | `KeyboardButtonCopy` | `(self, text: str, copy_text: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonGame` | `KeyboardButtonGame` | `(self, text: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonRequestGeoLocation` | `KeyboardButtonRequestGeoLocation` | `(self, text: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonRequestPeer` | `KeyboardButtonRequestPeer` | `(self, text: str, button_id: int, peer_type: 'TypeRequestPeerType', max_quantity: int, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonRequestPhone` | `KeyboardButtonRequestPhone` | `(self, text: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonRequestPoll` | `KeyboardButtonRequestPoll` | `(self, text: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None, quiz: Optional[bool] = None)` |
| `types` | `KeyboardButtonRow` | `KeyboardButtonRow` | `(self, buttons: List[ForwardRef('TypeKeyboardButton')])` |
| `types` | `KeyboardButtonSimpleWebView` | `KeyboardButtonSimpleWebView` | `(self, text: str, url: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonStyle` | `KeyboardButtonStyle` | `(self, bg_primary: Optional[bool] = None, bg_danger: Optional[bool] = None, bg_success: Optional[bool] = None, icon: Optional[int] = None)` |
| `types` | `KeyboardButtonSwitchInline` | `KeyboardButtonSwitchInline` | `(self, text: str, query: str, same_peer: Optional[bool] = None, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None, peer_types: Optional[List[ForwardRef('TypeInlineQueryPeerType')]] = None)` |
| `types` | `KeyboardButtonUrl` | `KeyboardButtonUrl` | `(self, text: str, url: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonUrlAuth` | `KeyboardButtonUrlAuth` | `(self, text: str, url: str, button_id: int, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None, fwd_text: Optional[str] = None)` |
| `types` | `KeyboardButtonUserProfile` | `KeyboardButtonUserProfile` | `(self, text: str, user_id: int, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `KeyboardButtonWebView` | `KeyboardButtonWebView` | `(self, text: str, url: str, style: Optional[ForwardRef('TypeKeyboardButtonStyle')] = None)` |
| `types` | `LabeledPrice` | `LabeledPrice` | `(self, label: str, amount: int)` |
| `types` | `LangPackDifference` | `LangPackDifference` | `(self, lang_code: str, from_version: int, version: int, strings: List[ForwardRef('TypeLangPackString')])` |
| `types` | `LangPackLanguage` | `LangPackLanguage` | `(self, name: str, native_name: str, lang_code: str, plural_code: str, strings_count: int, translated_count: int, translations_url: str, official: Optional[bool] = None, rtl: Optional[bool] = None, beta: Optional[bool] = None, base_lang_code: Optional[str] = None)` |
| `types` | `LangPackString` | `LangPackString` | `(self, key: str, value: str)` |
| `types` | `LangPackStringDeleted` | `LangPackStringDeleted` | `(self, key: str)` |
| `types` | `LangPackStringPluralized` | `LangPackStringPluralized` | `(self, key: str, other_value: str, zero_value: Optional[str] = None, one_value: Optional[str] = None, two_value: Optional[str] = None, few_value: Optional[str] = None, many_value: Optional[str] = None)` |
| `types` | `MaskCoords` | `MaskCoords` | `(self, n: int, x: float, y: float, zoom: float)` |
| `types` | `MediaAreaChannelPost` | `MediaAreaChannelPost` | `(self, coordinates: 'TypeMediaAreaCoordinates', channel_id: int, msg_id: int)` |
| `types` | `MediaAreaCoordinates` | `MediaAreaCoordinates` | `(self, x: float, y: float, w: float, h: float, rotation: float, radius: Optional[float] = None)` |
| `types` | `MediaAreaGeoPoint` | `MediaAreaGeoPoint` | `(self, coordinates: 'TypeMediaAreaCoordinates', geo: 'TypeGeoPoint', address: Optional[ForwardRef('TypeGeoPointAddress')] = None)` |
| `types` | `MediaAreaStarGift` | `MediaAreaStarGift` | `(self, coordinates: 'TypeMediaAreaCoordinates', slug: str)` |
| `types` | `MediaAreaSuggestedReaction` | `MediaAreaSuggestedReaction` | `(self, coordinates: 'TypeMediaAreaCoordinates', reaction: 'TypeReaction', dark: Optional[bool] = None, flipped: Optional[bool] = None)` |
| `types` | `MediaAreaUrl` | `MediaAreaUrl` | `(self, coordinates: 'TypeMediaAreaCoordinates', url: str)` |
| `types` | `MediaAreaVenue` | `MediaAreaVenue` | `(self, coordinates: 'TypeMediaAreaCoordinates', geo: 'TypeGeoPoint', title: str, address: str, provider: str, venue_id: str, venue_type: str)` |
| `types` | `MediaAreaWeather` | `MediaAreaWeather` | `(self, coordinates: 'TypeMediaAreaCoordinates', emoji: str, temperature_c: float, color: int)` |
| `types` | `MessageActionBoostApply` | `MessageActionBoostApply` | `(self, boosts: int)` |
| `types` | `MessageActionBotAllowed` | `MessageActionBotAllowed` | `(self, attach_menu: Optional[bool] = None, from_request: Optional[bool] = None, domain: Optional[str] = None, app: Optional[ForwardRef('TypeBotApp')] = None)` |
| `types` | `MessageActionChangeCreator` | `MessageActionChangeCreator` | `(self, new_creator_id: int)` |
| `types` | `MessageActionChannelCreate` | `MessageActionChannelCreate` | `(self, title: str)` |
| `types` | `MessageActionChannelMigrateFrom` | `MessageActionChannelMigrateFrom` | `(self, title: str, chat_id: int)` |
| `types` | `MessageActionChatAddUser` | `MessageActionChatAddUser` | `(self, users: List[int])` |
| `types` | `MessageActionChatCreate` | `MessageActionChatCreate` | `(self, title: str, users: List[int])` |
| `types` | `MessageActionChatDeletePhoto` | `MessageActionChatDeletePhoto` | `(self, /, *args, **kwargs)` |
| `types` | `MessageActionChatDeleteUser` | `MessageActionChatDeleteUser` | `(self, user_id: int)` |
| `types` | `MessageActionChatEditPhoto` | `MessageActionChatEditPhoto` | `(self, photo: 'TypePhoto')` |
| `types` | `MessageActionChatEditTitle` | `MessageActionChatEditTitle` | `(self, title: str)` |
| `types` | `MessageActionChatJoinedByLink` | `MessageActionChatJoinedByLink` | `(self, inviter_id: int)` |
| `types` | `MessageActionChatJoinedByRequest` | `MessageActionChatJoinedByRequest` | `(self, /, *args, **kwargs)` |
| `types` | `MessageActionChatMigrateTo` | `MessageActionChatMigrateTo` | `(self, channel_id: int)` |
| `types` | `MessageActionConferenceCall` | `MessageActionConferenceCall` | `(self, call_id: int, missed: Optional[bool] = None, active: Optional[bool] = None, video: Optional[bool] = None, duration: Optional[int] = None, other_participants: Optional[List[ForwardRef('TypePeer')]] = None)` |
| `types` | `MessageActionContactSignUp` | `MessageActionContactSignUp` | `(self, /, *args, **kwargs)` |
| `types` | `MessageActionCustomAction` | `MessageActionCustomAction` | `(self, message: str)` |
| `types` | `MessageActionEmpty` | `MessageActionEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `MessageActionGameScore` | `MessageActionGameScore` | `(self, game_id: int, score: int)` |
| `types` | `MessageActionGeoProximityReached` | `MessageActionGeoProximityReached` | `(self, from_id: 'TypePeer', to_id: 'TypePeer', distance: int)` |
| `types` | `MessageActionGiftCode` | `MessageActionGiftCode` | `(self, days: int, slug: str, via_giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, boost_peer: Optional[ForwardRef('TypePeer')] = None, currency: Optional[str] = None, amount: Optional[int] = None, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `MessageActionGiftPremium` | `MessageActionGiftPremium` | `(self, currency: str, amount: int, days: int, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `MessageActionGiftStars` | `MessageActionGiftStars` | `(self, currency: str, amount: int, stars: int, crypto_currency: Optional[str] = None, crypto_amount: Optional[int] = None, transaction_id: Optional[str] = None)` |
| `types` | `MessageActionGiftTon` | `MessageActionGiftTon` | `(self, currency: str, amount: int, crypto_currency: str, crypto_amount: int, transaction_id: Optional[str] = None)` |
| `types` | `MessageActionGiveawayLaunch` | `MessageActionGiveawayLaunch` | `(self, stars: Optional[int] = None)` |
| `types` | `MessageActionGiveawayResults` | `MessageActionGiveawayResults` | `(self, winners_count: int, unclaimed_count: int, stars: Optional[bool] = None)` |
| `types` | `MessageActionGroupCall` | `MessageActionGroupCall` | `(self, call: 'TypeInputGroupCall', duration: Optional[int] = None)` |
| `types` | `MessageActionGroupCallScheduled` | `MessageActionGroupCallScheduled` | `(self, call: 'TypeInputGroupCall', schedule_date: Optional[datetime.datetime])` |
| `types` | `MessageActionHistoryClear` | `MessageActionHistoryClear` | `(self, /, *args, **kwargs)` |
| `types` | `MessageActionInviteToGroupCall` | `MessageActionInviteToGroupCall` | `(self, call: 'TypeInputGroupCall', users: List[int])` |
| `types` | `MessageActionManagedBotCreated` | `MessageActionManagedBotCreated` | `(self, bot_id: int)` |
| `types` | `MessageActionNewCreatorPending` | `MessageActionNewCreatorPending` | `(self, new_creator_id: int)` |
| `types` | `MessageActionNoForwardsRequest` | `MessageActionNoForwardsRequest` | `(self, prev_value: bool, new_value: bool, expired: Optional[bool] = None)` |
| `types` | `MessageActionNoForwardsToggle` | `MessageActionNoForwardsToggle` | `(self, prev_value: bool, new_value: bool)` |
| `types` | `MessageActionPaidMessagesPrice` | `MessageActionPaidMessagesPrice` | `(self, stars: int, broadcast_messages_allowed: Optional[bool] = None)` |
| `types` | `MessageActionPaidMessagesRefunded` | `MessageActionPaidMessagesRefunded` | `(self, count: int, stars: int)` |
| `types` | `MessageActionPaymentRefunded` | `MessageActionPaymentRefunded` | `(self, peer: 'TypePeer', currency: str, total_amount: int, charge: 'TypePaymentCharge', payload: Optional[bytes] = None)` |
| `types` | `MessageActionPaymentSent` | `MessageActionPaymentSent` | `(self, currency: str, total_amount: int, recurring_init: Optional[bool] = None, recurring_used: Optional[bool] = None, invoice_slug: Optional[str] = None, subscription_until_date: Optional[datetime.datetime] = None)` |
| `types` | `MessageActionPaymentSentMe` | `MessageActionPaymentSentMe` | `(self, currency: str, total_amount: int, payload: bytes, charge: 'TypePaymentCharge', recurring_init: Optional[bool] = None, recurring_used: Optional[bool] = None, info: Optional[ForwardRef('TypePaymentRequestedInfo')] = None, shipping_option_id: Optional[str] = None, subscription_until_date: Optional[datetime.datetime] = None)` |
| `types` | `MessageActionPhoneCall` | `MessageActionPhoneCall` | `(self, call_id: int, video: Optional[bool] = None, reason: Optional[ForwardRef('TypePhoneCallDiscardReason')] = None, duration: Optional[int] = None)` |
| `types` | `MessageActionPinMessage` | `MessageActionPinMessage` | `(self, /, *args, **kwargs)` |
| `types` | `MessageActionPollAppendAnswer` | `MessageActionPollAppendAnswer` | `(self, answer: 'TypePollAnswer')` |
| `types` | `MessageActionPollDeleteAnswer` | `MessageActionPollDeleteAnswer` | `(self, answer: 'TypePollAnswer')` |
| `types` | `MessageActionPrizeStars` | `MessageActionPrizeStars` | `(self, stars: int, transaction_id: str, boost_peer: 'TypePeer', giveaway_msg_id: int, unclaimed: Optional[bool] = None)` |
| `types` | `MessageActionRequestedPeer` | `MessageActionRequestedPeer` | `(self, button_id: int, peers: List[ForwardRef('TypePeer')])` |
| `types` | `MessageActionRequestedPeerSentMe` | `MessageActionRequestedPeerSentMe` | `(self, button_id: int, peers: List[ForwardRef('TypeRequestedPeer')])` |
| `types` | `MessageActionScreenshotTaken` | `MessageActionScreenshotTaken` | `(self, /, *args, **kwargs)` |
| `types` | `MessageActionSecureValuesSent` | `MessageActionSecureValuesSent` | `(self, types: List[ForwardRef('TypeSecureValueType')])` |
| `types` | `MessageActionSecureValuesSentMe` | `MessageActionSecureValuesSentMe` | `(self, values: List[ForwardRef('TypeSecureValue')], credentials: 'TypeSecureCredentialsEncrypted')` |
| `types` | `MessageActionSetChatTheme` | `MessageActionSetChatTheme` | `(self, theme: 'TypeChatTheme')` |
| `types` | `MessageActionSetChatWallPaper` | `MessageActionSetChatWallPaper` | `(self, wallpaper: 'TypeWallPaper', same: Optional[bool] = None, for_both: Optional[bool] = None)` |
| `types` | `MessageActionSetMessagesTTL` | `MessageActionSetMessagesTTL` | `(self, period: int, auto_setting_from: Optional[int] = None)` |
| `types` | `MessageActionStarGift` | `MessageActionStarGift` | `(self, gift: 'TypeStarGift', name_hidden: Optional[bool] = None, saved: Optional[bool] = None, converted: Optional[bool] = None, upgraded: Optional[bool] = None, refunded: Optional[bool] = None, can_upgrade: Optional[bool] = None, prepaid_upgrade: Optional[bool] = None, upgrade_separate: Optional[bool] = None, auction_acquired: Optional[bool] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None, convert_stars: Optional[int] = None, upgrade_msg_id: Optional[int] = None, upgrade_stars: Optional[int] = None, from_id: Optional[ForwardRef('TypePeer')] = None, peer: Optional[ForwardRef('TypePeer')] = None, saved_id: Optional[int] = None, prepaid_upgrade_hash: Optional[str] = None, gift_msg_id: Optional[int] = None, to_id: Optional[ForwardRef('TypePeer')] = None, gift_num: Optional[int] = None)` |
| `types` | `MessageActionStarGiftPurchaseOffer` | `MessageActionStarGiftPurchaseOffer` | `(self, gift: 'TypeStarGift', price: 'TypeStarsAmount', expires_at: Optional[datetime.datetime], accepted: Optional[bool] = None, declined: Optional[bool] = None)` |
| `types` | `MessageActionStarGiftPurchaseOfferDeclined` | `MessageActionStarGiftPurchaseOfferDeclined` | `(self, gift: 'TypeStarGift', price: 'TypeStarsAmount', expired: Optional[bool] = None)` |
| `types` | `MessageActionStarGiftUnique` | `MessageActionStarGiftUnique` | `(self, gift: 'TypeStarGift', upgrade: Optional[bool] = None, transferred: Optional[bool] = None, saved: Optional[bool] = None, refunded: Optional[bool] = None, prepaid_upgrade: Optional[bool] = None, assigned: Optional[bool] = None, from_offer: Optional[bool] = None, craft: Optional[bool] = None, can_export_at: Optional[int] = None, transfer_stars: Optional[int] = None, from_id: Optional[ForwardRef('TypePeer')] = None, peer: Optional[ForwardRef('TypePeer')] = None, saved_id: Optional[int] = None, resale_amount: Optional[ForwardRef('TypeStarsAmount')] = None, can_transfer_at: Optional[int] = None, can_resell_at: Optional[int] = None, drop_original_details_stars: Optional[int] = None, can_craft_at: Optional[int] = None)` |
| `types` | `MessageActionSuggestBirthday` | `MessageActionSuggestBirthday` | `(self, birthday: 'TypeBirthday')` |
| `types` | `MessageActionSuggestProfilePhoto` | `MessageActionSuggestProfilePhoto` | `(self, photo: 'TypePhoto')` |
| `types` | `MessageActionSuggestedPostApproval` | `MessageActionSuggestedPostApproval` | `(self, rejected: Optional[bool] = None, balance_too_low: Optional[bool] = None, reject_comment: Optional[str] = None, schedule_date: Optional[datetime.datetime] = None, price: Optional[ForwardRef('TypeStarsAmount')] = None)` |
| `types` | `MessageActionSuggestedPostRefund` | `MessageActionSuggestedPostRefund` | `(self, payer_initiated: Optional[bool] = None)` |
| `types` | `MessageActionSuggestedPostSuccess` | `MessageActionSuggestedPostSuccess` | `(self, price: 'TypeStarsAmount')` |
| `types` | `MessageActionTodoAppendTasks` | `MessageActionTodoAppendTasks` | `(self, list: List[ForwardRef('TypeTodoItem')])` |
| `types` | `MessageActionTodoCompletions` | `MessageActionTodoCompletions` | `(self, completed: List[int], incompleted: List[int])` |
| `types` | `MessageActionTopicCreate` | `MessageActionTopicCreate` | `(self, title: str, icon_color: int, title_missing: Optional[bool] = None, icon_emoji_id: Optional[int] = None)` |
| `types` | `MessageActionTopicEdit` | `MessageActionTopicEdit` | `(self, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None)` |
| `types` | `MessageActionWebViewDataSent` | `MessageActionWebViewDataSent` | `(self, text: str)` |
| `types` | `MessageActionWebViewDataSentMe` | `MessageActionWebViewDataSentMe` | `(self, text: str, data: str)` |
| `types` | `MessageEntityBankCard` | `MessageEntityBankCard` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityBlockquote` | `MessageEntityBlockquote` | `(self, offset: int, length: int, collapsed: Optional[bool] = None)` |
| `types` | `MessageEntityBold` | `MessageEntityBold` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityBotCommand` | `MessageEntityBotCommand` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityCashtag` | `MessageEntityCashtag` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityCode` | `MessageEntityCode` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityCustomEmoji` | `MessageEntityCustomEmoji` | `(self, offset: int, length: int, document_id: int)` |
| `types` | `MessageEntityDiffDelete` | `MessageEntityDiffDelete` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityDiffInsert` | `MessageEntityDiffInsert` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityDiffReplace` | `MessageEntityDiffReplace` | `(self, offset: int, length: int, old_text: str)` |
| `types` | `MessageEntityEmail` | `MessageEntityEmail` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityFormattedDate` | `MessageEntityFormattedDate` | `(self, offset: int, length: int, date: Optional[datetime.datetime], relative: Optional[bool] = None, short_time: Optional[bool] = None, long_time: Optional[bool] = None, short_date: Optional[bool] = None, long_date: Optional[bool] = None, day_of_week: Optional[bool] = None)` |
| `types` | `MessageEntityHashtag` | `MessageEntityHashtag` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityItalic` | `MessageEntityItalic` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityMention` | `MessageEntityMention` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityMentionName` | `MessageEntityMentionName` | `(self, offset: int, length: int, user_id: int)` |
| `types` | `MessageEntityPhone` | `MessageEntityPhone` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityPre` | `MessageEntityPre` | `(self, offset: int, length: int, language: str)` |
| `types` | `MessageEntitySpoiler` | `MessageEntitySpoiler` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityStrike` | `MessageEntityStrike` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityTextUrl` | `MessageEntityTextUrl` | `(self, offset: int, length: int, url: str)` |
| `types` | `MessageEntityUnderline` | `MessageEntityUnderline` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityUnknown` | `MessageEntityUnknown` | `(self, offset: int, length: int)` |
| `types` | `MessageEntityUrl` | `MessageEntityUrl` | `(self, offset: int, length: int)` |
| `types` | `MessageExtendedMedia` | `MessageExtendedMedia` | `(self, media: 'TypeMessageMedia')` |
| `types` | `MessageExtendedMediaPreview` | `MessageExtendedMediaPreview` | `(self, w: Optional[int] = None, h: Optional[int] = None, thumb: Optional[ForwardRef('TypePhotoSize')] = None, video_duration: Optional[int] = None)` |
| `types` | `MessageFwdHeader` | `MessageFwdHeader` | `(self, date: Optional[datetime.datetime], imported: Optional[bool] = None, saved_out: Optional[bool] = None, from_id: Optional[ForwardRef('TypePeer')] = None, from_name: Optional[str] = None, channel_post: Optional[int] = None, post_author: Optional[str] = None, saved_from_peer: Optional[ForwardRef('TypePeer')] = None, saved_from_msg_id: Optional[int] = None, saved_from_id: Optional[ForwardRef('TypePeer')] = None, saved_from_name: Optional[str] = None, saved_date: Optional[datetime.datetime] = None, psa_type: Optional[str] = None)` |
| `types` | `MessageMediaContact` | `MessageMediaContact` | `(self, phone_number: str, first_name: str, last_name: str, vcard: str, user_id: int)` |
| `types` | `MessageMediaDice` | `MessageMediaDice` | `(self, value: int, emoticon: str, game_outcome: Optional[ForwardRef('TypeEmojiGameOutcome')] = None)` |
| `types` | `MessageMediaDocument` | `MessageMediaDocument` | `(self, nopremium: Optional[bool] = None, spoiler: Optional[bool] = None, video: Optional[bool] = None, round: Optional[bool] = None, voice: Optional[bool] = None, document: Optional[ForwardRef('TypeDocument')] = None, alt_documents: Optional[List[ForwardRef('TypeDocument')]] = None, video_cover: Optional[ForwardRef('TypePhoto')] = None, video_timestamp: Optional[int] = None, ttl_seconds: Optional[int] = None)` |
| `types` | `MessageMediaEmpty` | `MessageMediaEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `MessageMediaGame` | `MessageMediaGame` | `(self, game: 'TypeGame')` |
| `types` | `MessageMediaGeo` | `MessageMediaGeo` | `(self, geo: 'TypeGeoPoint')` |
| `types` | `MessageMediaGeoLive` | `MessageMediaGeoLive` | `(self, geo: 'TypeGeoPoint', period: int, heading: Optional[int] = None, proximity_notification_radius: Optional[int] = None)` |
| `types` | `MessageMediaGiveaway` | `MessageMediaGiveaway` | `(self, channels: List[int], quantity: int, until_date: Optional[datetime.datetime], only_new_subscribers: Optional[bool] = None, winners_are_visible: Optional[bool] = None, countries_iso2: Optional[List[str]] = None, prize_description: Optional[str] = None, months: Optional[int] = None, stars: Optional[int] = None)` |
| `types` | `MessageMediaGiveawayResults` | `MessageMediaGiveawayResults` | `(self, channel_id: int, launch_msg_id: int, winners_count: int, unclaimed_count: int, winners: List[int], until_date: Optional[datetime.datetime], only_new_subscribers: Optional[bool] = None, refunded: Optional[bool] = None, additional_peers_count: Optional[int] = None, months: Optional[int] = None, stars: Optional[int] = None, prize_description: Optional[str] = None)` |
| `types` | `MessageMediaInvoice` | `MessageMediaInvoice` | `(self, title: str, description: str, currency: str, total_amount: int, start_param: str, shipping_address_requested: Optional[bool] = None, test: Optional[bool] = None, photo: Optional[ForwardRef('TypeWebDocument')] = None, receipt_msg_id: Optional[int] = None, extended_media: Optional[ForwardRef('TypeMessageExtendedMedia')] = None)` |
| `types` | `MessageMediaPaidMedia` | `MessageMediaPaidMedia` | `(self, stars_amount: int, extended_media: List[ForwardRef('TypeMessageExtendedMedia')])` |
| `types` | `MessageMediaPhoto` | `MessageMediaPhoto` | `(self, spoiler: Optional[bool] = None, live_photo: Optional[bool] = None, photo: Optional[ForwardRef('TypePhoto')] = None, ttl_seconds: Optional[int] = None, video: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `MessageMediaPoll` | `MessageMediaPoll` | `(self, poll: 'TypePoll', results: 'TypePollResults', attached_media: Optional[ForwardRef('TypeMessageMedia')] = None)` |
| `types` | `MessageMediaStory` | `MessageMediaStory` | `(self, peer: 'TypePeer', id: int, via_mention: Optional[bool] = None, story: Optional[ForwardRef('TypeStoryItem')] = None)` |
| `types` | `MessageMediaToDo` | `MessageMediaToDo` | `(self, todo: 'TypeTodoList', completions: Optional[List[ForwardRef('TypeTodoCompletion')]] = None)` |
| `types` | `MessageMediaUnsupported` | `MessageMediaUnsupported` | `(self, /, *args, **kwargs)` |
| `types` | `MessageMediaVenue` | `MessageMediaVenue` | `(self, geo: 'TypeGeoPoint', title: str, address: str, provider: str, venue_id: str, venue_type: str)` |
| `types` | `MessageMediaVideoStream` | `MessageMediaVideoStream` | `(self, call: 'TypeInputGroupCall', rtmp_stream: Optional[bool] = None)` |
| `types` | `MessageMediaWebPage` | `MessageMediaWebPage` | `(self, webpage: 'TypeWebPage', force_large_media: Optional[bool] = None, force_small_media: Optional[bool] = None, manual: Optional[bool] = None, safe: Optional[bool] = None)` |
| `types` | `MessagePeerReaction` | `MessagePeerReaction` | `(self, peer_id: 'TypePeer', date: Optional[datetime.datetime], reaction: 'TypeReaction', big: Optional[bool] = None, unread: Optional[bool] = None, my: Optional[bool] = None)` |
| `types` | `MessagePeerVote` | `MessagePeerVote` | `(self, peer: 'TypePeer', option: bytes, date: Optional[datetime.datetime])` |
| `types` | `MessagePeerVoteInputOption` | `MessagePeerVoteInputOption` | `(self, peer: 'TypePeer', date: Optional[datetime.datetime])` |
| `types` | `MessagePeerVoteMultiple` | `MessagePeerVoteMultiple` | `(self, peer: 'TypePeer', options: List[bytes], date: Optional[datetime.datetime])` |
| `types` | `MessageRange` | `MessageRange` | `(self, min_id: int, max_id: int)` |
| `types` | `MessageReactions` | `MessageReactions` | `(self, results: List[ForwardRef('TypeReactionCount')], min: Optional[bool] = None, can_see_list: Optional[bool] = None, reactions_as_tags: Optional[bool] = None, recent_reactions: Optional[List[ForwardRef('TypeMessagePeerReaction')]] = None, top_reactors: Optional[List[ForwardRef('TypeMessageReactor')]] = None)` |
| `types` | `MessageReactor` | `MessageReactor` | `(self, count: int, top: Optional[bool] = None, my: Optional[bool] = None, anonymous: Optional[bool] = None, peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `MessageReplies` | `MessageReplies` | `(self, replies: int, replies_pts: int, comments: Optional[bool] = None, recent_repliers: Optional[List[ForwardRef('TypePeer')]] = None, channel_id: Optional[int] = None, max_id: Optional[int] = None, read_max_id: Optional[int] = None)` |
| `types` | `MessageReplyHeader` | `MessageReplyHeader` | `(self, reply_to_scheduled: Optional[bool] = None, forum_topic: Optional[bool] = None, quote: Optional[bool] = None, reply_to_ephemeral: Optional[bool] = None, reply_to_msg_id: Optional[int] = None, reply_to_peer_id: Optional[ForwardRef('TypePeer')] = None, reply_from: Optional[ForwardRef('TypeMessageFwdHeader')] = None, reply_media: Optional[ForwardRef('TypeMessageMedia')] = None, reply_to_top_id: Optional[int] = None, quote_text: Optional[str] = None, quote_entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, quote_offset: Optional[int] = None, todo_item_id: Optional[int] = None, poll_option: Optional[bytes] = None)` |
| `types` | `MessageReplyStoryHeader` | `MessageReplyStoryHeader` | `(self, peer: 'TypePeer', story_id: int)` |
| `types` | `MessageReportOption` | `MessageReportOption` | `(self, text: str, option: bytes)` |
| `types` | `MessageViews` | `MessageViews` | `(self, views: Optional[int] = None, forwards: Optional[int] = None, replies: Optional[ForwardRef('TypeMessageReplies')] = None)` |
| `types` | `MissingInvitee` | `MissingInvitee` | `(self, user_id: int, premium_would_allow_invite: Optional[bool] = None, premium_required_for_pm: Optional[bool] = None)` |
| `types` | `MonoForumDialog` | `MonoForumDialog` | `(self, peer: 'TypePeer', top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_reactions_count: int, unread_mark: Optional[bool] = None, nopaid_messages_exception: Optional[bool] = None, draft: Optional[ForwardRef('TypeDraftMessage')] = None)` |
| `types` | `MsgDetailedInfo` | `MsgDetailedInfo` | `(self, msg_id: int, answer_msg_id: int, bytes: int, status: int)` |
| `types` | `MsgNewDetailedInfo` | `MsgNewDetailedInfo` | `(self, answer_msg_id: int, bytes: int, status: int)` |
| `types` | `MsgResendReq` | `MsgResendReq` | `(self, msg_ids: List[int])` |
| `types` | `MsgsAck` | `MsgsAck` | `(self, msg_ids: List[int])` |
| `types` | `MsgsAllInfo` | `MsgsAllInfo` | `(self, msg_ids: List[int], info: str)` |
| `types` | `MsgsStateInfo` | `MsgsStateInfo` | `(self, req_msg_id: int, info: str)` |
| `types` | `MsgsStateReq` | `MsgsStateReq` | `(self, msg_ids: List[int])` |
| `types` | `MyBoost` | `MyBoost` | `(self, slot: int, date: Optional[datetime.datetime], expires: Optional[datetime.datetime], peer: Optional[ForwardRef('TypePeer')] = None, cooldown_until_date: Optional[datetime.datetime] = None)` |
| `types` | `NearestDc` | `NearestDc` | `(self, country: str, this_dc: int, nearest_dc: int)` |
| `types` | `NewSessionCreated` | `NewSessionCreated` | `(self, first_msg_id: int, unique_id: int, server_salt: int)` |
| `types` | `NotificationSoundDefault` | `NotificationSoundDefault` | `(self, /, *args, **kwargs)` |
| `types` | `NotificationSoundLocal` | `NotificationSoundLocal` | `(self, title: str, data: str)` |
| `types` | `NotificationSoundNone` | `NotificationSoundNone` | `(self, /, *args, **kwargs)` |
| `types` | `NotificationSoundRingtone` | `NotificationSoundRingtone` | `(self, id: int)` |
| `types` | `NotifyBroadcasts` | `NotifyBroadcasts` | `(self, /, *args, **kwargs)` |
| `types` | `NotifyChats` | `NotifyChats` | `(self, /, *args, **kwargs)` |
| `types` | `NotifyForumTopic` | `NotifyForumTopic` | `(self, peer: 'TypePeer', top_msg_id: int)` |
| `types` | `NotifyPeer` | `NotifyPeer` | `(self, peer: 'TypePeer')` |
| `types` | `NotifyUsers` | `NotifyUsers` | `(self, /, *args, **kwargs)` |
| `types` | `OutboxReadDate` | `OutboxReadDate` | `(self, date: Optional[datetime.datetime])` |
| `types` | `PQInnerData` | `PQInnerData` | `(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int)` |
| `types` | `PQInnerDataDc` | `PQInnerDataDc` | `(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, dc: int)` |
| `types` | `PQInnerDataTemp` | `PQInnerDataTemp` | `(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, expires_in: int)` |
| `types` | `PQInnerDataTempDc` | `PQInnerDataTempDc` | `(self, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, dc: int, expires_in: int)` |
| `types` | `Page` | `Page` | `(self, url: str, blocks: List[ForwardRef('TypePageBlock')], photos: List[ForwardRef('TypePhoto')], documents: List[ForwardRef('TypeDocument')], part: Optional[bool] = None, rtl: Optional[bool] = None, v2: Optional[bool] = None, views: Optional[int] = None)` |
| `types` | `PageBlockAnchor` | `PageBlockAnchor` | `(self, name: str)` |
| `types` | `PageBlockAudio` | `PageBlockAudio` | `(self, audio_id: int, caption: 'TypePageCaption')` |
| `types` | `PageBlockAuthorDate` | `PageBlockAuthorDate` | `(self, author: 'TypeRichText', published_date: Optional[datetime.datetime])` |
| `types` | `PageBlockBlockquote` | `PageBlockBlockquote` | `(self, text: 'TypeRichText', caption: 'TypeRichText')` |
| `types` | `PageBlockBlockquoteBlocks` | `PageBlockBlockquoteBlocks` | `(self, blocks: List[ForwardRef('TypePageBlock')], caption: 'TypeRichText')` |
| `types` | `PageBlockChannel` | `PageBlockChannel` | `(self, channel: 'TypeChat')` |
| `types` | `PageBlockCollage` | `PageBlockCollage` | `(self, items: List[ForwardRef('TypePageBlock')], caption: 'TypePageCaption')` |
| `types` | `PageBlockCover` | `PageBlockCover` | `(self, cover: 'TypePageBlock')` |
| `types` | `PageBlockDetails` | `PageBlockDetails` | `(self, blocks: List[ForwardRef('TypePageBlock')], title: 'TypeRichText', open: Optional[bool] = None)` |
| `types` | `PageBlockDivider` | `PageBlockDivider` | `(self, /, *args, **kwargs)` |
| `types` | `PageBlockEmbed` | `PageBlockEmbed` | `(self, caption: 'TypePageCaption', full_width: Optional[bool] = None, allow_scrolling: Optional[bool] = None, url: Optional[str] = None, html: Optional[str] = None, poster_photo_id: Optional[int] = None, w: Optional[int] = None, h: Optional[int] = None)` |
| `types` | `PageBlockEmbedPost` | `PageBlockEmbedPost` | `(self, url: str, webpage_id: int, author_photo_id: int, author: str, date: Optional[datetime.datetime], blocks: List[ForwardRef('TypePageBlock')], caption: 'TypePageCaption')` |
| `types` | `PageBlockFooter` | `PageBlockFooter` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockHeader` | `PageBlockHeader` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockHeading1` | `PageBlockHeading1` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockHeading2` | `PageBlockHeading2` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockHeading3` | `PageBlockHeading3` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockHeading4` | `PageBlockHeading4` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockHeading5` | `PageBlockHeading5` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockHeading6` | `PageBlockHeading6` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockKicker` | `PageBlockKicker` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockList` | `PageBlockList` | `(self, items: List[ForwardRef('TypePageListItem')])` |
| `types` | `PageBlockMap` | `PageBlockMap` | `(self, geo: 'TypeGeoPoint', zoom: int, w: int, h: int, caption: 'TypePageCaption')` |
| `types` | `PageBlockMath` | `PageBlockMath` | `(self, source: str)` |
| `types` | `PageBlockOrderedList` | `PageBlockOrderedList` | `(self, items: List[ForwardRef('TypePageListOrderedItem')], reversed: Optional[bool] = None, start: Optional[int] = None, type: Optional[str] = None)` |
| `types` | `PageBlockParagraph` | `PageBlockParagraph` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockPhoto` | `PageBlockPhoto` | `(self, photo_id: int, caption: 'TypePageCaption', spoiler: Optional[bool] = None, url: Optional[str] = None, webpage_id: Optional[int] = None)` |
| `types` | `PageBlockPreformatted` | `PageBlockPreformatted` | `(self, text: 'TypeRichText', language: str)` |
| `types` | `PageBlockPullquote` | `PageBlockPullquote` | `(self, text: 'TypeRichText', caption: 'TypeRichText')` |
| `types` | `PageBlockRelatedArticles` | `PageBlockRelatedArticles` | `(self, title: 'TypeRichText', articles: List[ForwardRef('TypePageRelatedArticle')])` |
| `types` | `PageBlockSlideshow` | `PageBlockSlideshow` | `(self, items: List[ForwardRef('TypePageBlock')], caption: 'TypePageCaption')` |
| `types` | `PageBlockSubheader` | `PageBlockSubheader` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockSubtitle` | `PageBlockSubtitle` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockTable` | `PageBlockTable` | `(self, title: 'TypeRichText', rows: List[ForwardRef('TypePageTableRow')], bordered: Optional[bool] = None, striped: Optional[bool] = None)` |
| `types` | `PageBlockThinking` | `PageBlockThinking` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockTitle` | `PageBlockTitle` | `(self, text: 'TypeRichText')` |
| `types` | `PageBlockUnsupported` | `PageBlockUnsupported` | `(self, /, *args, **kwargs)` |
| `types` | `PageBlockVideo` | `PageBlockVideo` | `(self, video_id: int, caption: 'TypePageCaption', autoplay: Optional[bool] = None, loop: Optional[bool] = None, spoiler: Optional[bool] = None)` |
| `types` | `PageCaption` | `PageCaption` | `(self, text: 'TypeRichText', credit: 'TypeRichText')` |
| `types` | `PageListItemBlocks` | `PageListItemBlocks` | `(self, blocks: List[ForwardRef('TypePageBlock')], checkbox: Optional[bool] = None, checked: Optional[bool] = None)` |
| `types` | `PageListItemText` | `PageListItemText` | `(self, text: 'TypeRichText', checkbox: Optional[bool] = None, checked: Optional[bool] = None)` |
| `types` | `PageListOrderedItemBlocks` | `PageListOrderedItemBlocks` | `(self, blocks: List[ForwardRef('TypePageBlock')], checkbox: Optional[bool] = None, checked: Optional[bool] = None, num: Optional[str] = None, value: Optional[int] = None, type: Optional[str] = None)` |
| `types` | `PageListOrderedItemText` | `PageListOrderedItemText` | `(self, text: 'TypeRichText', checkbox: Optional[bool] = None, checked: Optional[bool] = None, num: Optional[str] = None, value: Optional[int] = None, type: Optional[str] = None)` |
| `types` | `PageRelatedArticle` | `PageRelatedArticle` | `(self, url: str, webpage_id: int, title: Optional[str] = None, description: Optional[str] = None, photo_id: Optional[int] = None, author: Optional[str] = None, published_date: Optional[datetime.datetime] = None)` |
| `types` | `PageTableCell` | `PageTableCell` | `(self, header: Optional[bool] = None, align_center: Optional[bool] = None, align_right: Optional[bool] = None, valign_middle: Optional[bool] = None, valign_bottom: Optional[bool] = None, text: Optional[ForwardRef('TypeRichText')] = None, colspan: Optional[int] = None, rowspan: Optional[int] = None)` |
| `types` | `PageTableRow` | `PageTableRow` | `(self, cells: List[ForwardRef('TypePageTableCell')])` |
| `types` | `PaidReactionPrivacyAnonymous` | `PaidReactionPrivacyAnonymous` | `(self, /, *args, **kwargs)` |
| `types` | `PaidReactionPrivacyDefault` | `PaidReactionPrivacyDefault` | `(self, /, *args, **kwargs)` |
| `types` | `PaidReactionPrivacyPeer` | `PaidReactionPrivacyPeer` | `(self, peer: 'TypeInputPeer')` |
| `types` | `Passkey` | `Passkey` | `(self, id: str, name: str, date: Optional[datetime.datetime], software_emoji_id: Optional[int] = None, last_usage_date: Optional[datetime.datetime] = None)` |
| `types` | `PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow` | `PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow` | `(self, salt1: bytes, salt2: bytes, g: int, p: bytes)` |
| `types` | `PasswordKdfAlgoUnknown` | `PasswordKdfAlgoUnknown` | `(self, /, *args, **kwargs)` |
| `types` | `PaymentCharge` | `PaymentCharge` | `(self, id: str, provider_charge_id: str)` |
| `types` | `PaymentFormMethod` | `PaymentFormMethod` | `(self, url: str, title: str)` |
| `types` | `PaymentRequestedInfo` | `PaymentRequestedInfo` | `(self, name: Optional[str] = None, phone: Optional[str] = None, email: Optional[str] = None, shipping_address: Optional[ForwardRef('TypePostAddress')] = None)` |
| `types` | `PaymentSavedCredentialsCard` | `PaymentSavedCredentialsCard` | `(self, id: str, title: str)` |
| `types` | `PeerBlocked` | `PeerBlocked` | `(self, peer_id: 'TypePeer', date: Optional[datetime.datetime])` |
| `types` | `PeerChannel` | `PeerChannel` | `(self, channel_id: int)` |
| `types` | `PeerChat` | `PeerChat` | `(self, chat_id: int)` |
| `types` | `PeerColor` | `PeerColor` | `(self, color: Optional[int] = None, background_emoji_id: Optional[int] = None)` |
| `types` | `PeerColorCollectible` | `PeerColorCollectible` | `(self, collectible_id: int, gift_emoji_id: int, background_emoji_id: int, accent_color: int, colors: List[int], dark_accent_color: Optional[int] = None, dark_colors: Optional[List[int]] = None)` |
| `types` | `PeerLocated` | `PeerLocated` | `(self, peer: 'TypePeer', expires: Optional[datetime.datetime], distance: int)` |
| `types` | `PeerNotifySettings` | `PeerNotifySettings` | `(self, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[datetime.datetime] = None, ios_sound: Optional[ForwardRef('TypeNotificationSound')] = None, android_sound: Optional[ForwardRef('TypeNotificationSound')] = None, other_sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_ios_sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_android_sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_other_sound: Optional[ForwardRef('TypeNotificationSound')] = None)` |
| `types` | `PeerSelfLocated` | `PeerSelfLocated` | `(self, expires: Optional[datetime.datetime])` |
| `types` | `PeerSettings` | `PeerSettings` | `(self, report_spam: Optional[bool] = None, add_contact: Optional[bool] = None, block_contact: Optional[bool] = None, share_contact: Optional[bool] = None, need_contacts_exception: Optional[bool] = None, report_geo: Optional[bool] = None, autoarchived: Optional[bool] = None, invite_members: Optional[bool] = None, request_chat_broadcast: Optional[bool] = None, business_bot_paused: Optional[bool] = None, business_bot_can_reply: Optional[bool] = None, geo_distance: Optional[int] = None, request_chat_title: Optional[str] = None, request_chat_date: Optional[datetime.datetime] = None, business_bot_id: Optional[int] = None, business_bot_manage_url: Optional[str] = None, charge_paid_message_stars: Optional[int] = None, registration_month: Optional[str] = None, phone_country: Optional[str] = None, name_change_date: Optional[datetime.datetime] = None, photo_change_date: Optional[datetime.datetime] = None)` |
| `types` | `PeerStories` | `PeerStories` | `(self, peer: 'TypePeer', stories: List[ForwardRef('TypeStoryItem')], max_read_id: Optional[int] = None)` |
| `types` | `PeerUser` | `PeerUser` | `(self, user_id: int)` |
| `types` | `PendingSuggestion` | `PendingSuggestion` | `(self, suggestion: str, title: 'TypeTextWithEntities', description: 'TypeTextWithEntities', url: str)` |
| `types` | `PhoneCall` | `PhoneCall` | `(self, id: int, access_hash: int, date: Optional[datetime.datetime], admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int, protocol: 'TypePhoneCallProtocol', connections: List[ForwardRef('TypePhoneConnection')], start_date: Optional[datetime.datetime], p2p_allowed: Optional[bool] = None, video: Optional[bool] = None, conference_supported: Optional[bool] = None, custom_parameters: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `types` | `PhoneCallAccepted` | `PhoneCallAccepted` | `(self, id: int, access_hash: int, date: Optional[datetime.datetime], admin_id: int, participant_id: int, g_b: bytes, protocol: 'TypePhoneCallProtocol', video: Optional[bool] = None)` |
| `types` | `PhoneCallDiscardReasonBusy` | `PhoneCallDiscardReasonBusy` | `(self, /, *args, **kwargs)` |
| `types` | `PhoneCallDiscardReasonDisconnect` | `PhoneCallDiscardReasonDisconnect` | `(self, /, *args, **kwargs)` |
| `types` | `PhoneCallDiscardReasonHangup` | `PhoneCallDiscardReasonHangup` | `(self, /, *args, **kwargs)` |
| `types` | `PhoneCallDiscardReasonMigrateConferenceCall` | `PhoneCallDiscardReasonMigrateConferenceCall` | `(self, slug: str)` |
| `types` | `PhoneCallDiscardReasonMissed` | `PhoneCallDiscardReasonMissed` | `(self, /, *args, **kwargs)` |
| `types` | `PhoneCallDiscarded` | `PhoneCallDiscarded` | `(self, id: int, need_rating: Optional[bool] = None, need_debug: Optional[bool] = None, video: Optional[bool] = None, reason: Optional[ForwardRef('TypePhoneCallDiscardReason')] = None, duration: Optional[int] = None)` |
| `types` | `PhoneCallEmpty` | `PhoneCallEmpty` | `(self, id: int)` |
| `types` | `PhoneCallProtocol` | `PhoneCallProtocol` | `(self, min_layer: int, max_layer: int, library_versions: List[str], udp_p2p: Optional[bool] = None, udp_reflector: Optional[bool] = None)` |
| `types` | `PhoneCallRequested` | `PhoneCallRequested` | `(self, id: int, access_hash: int, date: Optional[datetime.datetime], admin_id: int, participant_id: int, g_a_hash: bytes, protocol: 'TypePhoneCallProtocol', video: Optional[bool] = None)` |
| `types` | `PhoneCallWaiting` | `PhoneCallWaiting` | `(self, id: int, access_hash: int, date: Optional[datetime.datetime], admin_id: int, participant_id: int, protocol: 'TypePhoneCallProtocol', video: Optional[bool] = None, receive_date: Optional[datetime.datetime] = None)` |
| `types` | `PhoneConnection` | `PhoneConnection` | `(self, id: int, ip: str, ipv6: str, port: int, peer_tag: bytes, tcp: Optional[bool] = None)` |
| `types` | `PhoneConnectionWebrtc` | `PhoneConnectionWebrtc` | `(self, id: int, ip: str, ipv6: str, port: int, username: str, password: str, turn: Optional[bool] = None, stun: Optional[bool] = None)` |
| `types` | `Photo` | `Photo` | `(self, id: int, access_hash: int, file_reference: bytes, date: Optional[datetime.datetime], sizes: List[ForwardRef('TypePhotoSize')], dc_id: int, has_stickers: Optional[bool] = None, video_sizes: Optional[List[ForwardRef('TypeVideoSize')]] = None)` |
| `types` | `PhotoCachedSize` | `PhotoCachedSize` | `(self, type: str, w: int, h: int, bytes: bytes)` |
| `types` | `PhotoEmpty` | `PhotoEmpty` | `(self, id: int)` |
| `types` | `PhotoPathSize` | `PhotoPathSize` | `(self, type: str, bytes: bytes)` |
| `types` | `PhotoSize` | `PhotoSize` | `(self, type: str, w: int, h: int, size: int)` |
| `types` | `PhotoSizeEmpty` | `PhotoSizeEmpty` | `(self, type: str)` |
| `types` | `PhotoSizeProgressive` | `PhotoSizeProgressive` | `(self, type: str, w: int, h: int, sizes: List[int])` |
| `types` | `PhotoStrippedSize` | `PhotoStrippedSize` | `(self, type: str, bytes: bytes)` |
| `types` | `Poll` | `Poll` | `(self, id: int, question: 'TypeTextWithEntities', answers: List[ForwardRef('TypePollAnswer')], hash: int, closed: Optional[bool] = None, public_voters: Optional[bool] = None, multiple_choice: Optional[bool] = None, quiz: Optional[bool] = None, open_answers: Optional[bool] = None, revoting_disabled: Optional[bool] = None, shuffle_answers: Optional[bool] = None, hide_results_until_close: Optional[bool] = None, creator: Optional[bool] = None, subscribers_only: Optional[bool] = None, close_period: Optional[int] = None, close_date: Optional[datetime.datetime] = None, countries_iso2: Optional[List[str]] = None)` |
| `types` | `PollAnswer` | `PollAnswer` | `(self, text: 'TypeTextWithEntities', option: bytes, media: Optional[ForwardRef('TypeMessageMedia')] = None, added_by: Optional[ForwardRef('TypePeer')] = None, date: Optional[datetime.datetime] = None)` |
| `types` | `PollAnswerVoters` | `PollAnswerVoters` | `(self, option: bytes, chosen: Optional[bool] = None, correct: Optional[bool] = None, voters: Optional[int] = None, recent_voters: Optional[List[ForwardRef('TypePeer')]] = None)` |
| `types` | `PollResults` | `PollResults` | `(self, min: Optional[bool] = None, has_unread_votes: Optional[bool] = None, can_view_stats: Optional[bool] = None, results: Optional[List[ForwardRef('TypePollAnswerVoters')]] = None, total_voters: Optional[int] = None, recent_voters: Optional[List[ForwardRef('TypePeer')]] = None, solution: Optional[str] = None, solution_entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, solution_media: Optional[ForwardRef('TypeMessageMedia')] = None)` |
| `types` | `Pong` | `Pong` | `(self, msg_id: int, ping_id: int)` |
| `types` | `PopularContact` | `PopularContact` | `(self, client_id: int, importers: int)` |
| `types` | `PostAddress` | `PostAddress` | `(self, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str, post_code: str)` |
| `types` | `PostInteractionCountersMessage` | `PostInteractionCountersMessage` | `(self, msg_id: int, views: int, forwards: int, reactions: int)` |
| `types` | `PostInteractionCountersStory` | `PostInteractionCountersStory` | `(self, story_id: int, views: int, forwards: int, reactions: int)` |
| `types` | `PremiumGiftCodeOption` | `PremiumGiftCodeOption` | `(self, users: int, months: int, currency: str, amount: int, store_product: Optional[str] = None, store_quantity: Optional[int] = None)` |
| `types` | `PremiumSubscriptionOption` | `PremiumSubscriptionOption` | `(self, months: int, currency: str, amount: int, bot_url: str, current: Optional[bool] = None, can_purchase_upgrade: Optional[bool] = None, transaction: Optional[str] = None, store_product: Optional[str] = None)` |
| `types` | `PrepaidGiveaway` | `PrepaidGiveaway` | `(self, id: int, months: int, quantity: int, date: Optional[datetime.datetime])` |
| `types` | `PrepaidStarsGiveaway` | `PrepaidStarsGiveaway` | `(self, id: int, stars: int, quantity: int, boosts: int, date: Optional[datetime.datetime])` |
| `types` | `PrivacyKeyAbout` | `PrivacyKeyAbout` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyAddedByPhone` | `PrivacyKeyAddedByPhone` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyBirthday` | `PrivacyKeyBirthday` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyChatInvite` | `PrivacyKeyChatInvite` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyForwards` | `PrivacyKeyForwards` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyNoPaidMessages` | `PrivacyKeyNoPaidMessages` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyPhoneCall` | `PrivacyKeyPhoneCall` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyPhoneNumber` | `PrivacyKeyPhoneNumber` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyPhoneP2P` | `PrivacyKeyPhoneP2P` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyProfilePhoto` | `PrivacyKeyProfilePhoto` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeySavedMusic` | `PrivacyKeySavedMusic` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyStarGiftsAutoSave` | `PrivacyKeyStarGiftsAutoSave` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyStatusTimestamp` | `PrivacyKeyStatusTimestamp` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyKeyVoiceMessages` | `PrivacyKeyVoiceMessages` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueAllowAll` | `PrivacyValueAllowAll` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueAllowBots` | `PrivacyValueAllowBots` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueAllowChatParticipants` | `PrivacyValueAllowChatParticipants` | `(self, chats: List[int])` |
| `types` | `PrivacyValueAllowCloseFriends` | `PrivacyValueAllowCloseFriends` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueAllowContacts` | `PrivacyValueAllowContacts` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueAllowPremium` | `PrivacyValueAllowPremium` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueAllowUsers` | `PrivacyValueAllowUsers` | `(self, users: List[int])` |
| `types` | `PrivacyValueDisallowAll` | `PrivacyValueDisallowAll` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueDisallowBots` | `PrivacyValueDisallowBots` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueDisallowChatParticipants` | `PrivacyValueDisallowChatParticipants` | `(self, chats: List[int])` |
| `types` | `PrivacyValueDisallowContacts` | `PrivacyValueDisallowContacts` | `(self, /, *args, **kwargs)` |
| `types` | `PrivacyValueDisallowUsers` | `PrivacyValueDisallowUsers` | `(self, users: List[int])` |
| `types` | `ProfileTabFiles` | `ProfileTabFiles` | `(self, /, *args, **kwargs)` |
| `types` | `ProfileTabGifs` | `ProfileTabGifs` | `(self, /, *args, **kwargs)` |
| `types` | `ProfileTabGifts` | `ProfileTabGifts` | `(self, /, *args, **kwargs)` |
| `types` | `ProfileTabLinks` | `ProfileTabLinks` | `(self, /, *args, **kwargs)` |
| `types` | `ProfileTabMedia` | `ProfileTabMedia` | `(self, /, *args, **kwargs)` |
| `types` | `ProfileTabMusic` | `ProfileTabMusic` | `(self, /, *args, **kwargs)` |
| `types` | `ProfileTabPosts` | `ProfileTabPosts` | `(self, /, *args, **kwargs)` |
| `types` | `ProfileTabVoice` | `ProfileTabVoice` | `(self, /, *args, **kwargs)` |
| `types` | `PublicForwardMessage` | `PublicForwardMessage` | `(self, message: 'TypeMessage')` |
| `types` | `PublicForwardStory` | `PublicForwardStory` | `(self, peer: 'TypePeer', story: 'TypeStoryItem')` |
| `types` | `QuickReply` | `QuickReply` | `(self, shortcut_id: int, shortcut: str, top_message: int, count: int)` |
| `types` | `ReactionCount` | `ReactionCount` | `(self, reaction: 'TypeReaction', count: int, chosen_order: Optional[int] = None)` |
| `types` | `ReactionCustomEmoji` | `ReactionCustomEmoji` | `(self, document_id: int)` |
| `types` | `ReactionEmoji` | `ReactionEmoji` | `(self, emoticon: str)` |
| `types` | `ReactionEmpty` | `ReactionEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `ReactionNotificationsFromAll` | `ReactionNotificationsFromAll` | `(self, /, *args, **kwargs)` |
| `types` | `ReactionNotificationsFromContacts` | `ReactionNotificationsFromContacts` | `(self, /, *args, **kwargs)` |
| `types` | `ReactionPaid` | `ReactionPaid` | `(self, /, *args, **kwargs)` |
| `types` | `ReactionsNotifySettings` | `ReactionsNotifySettings` | `(self, sound: 'TypeNotificationSound', show_previews: bool, messages_notify_from: Optional[ForwardRef('TypeReactionNotificationsFrom')] = None, stories_notify_from: Optional[ForwardRef('TypeReactionNotificationsFrom')] = None, poll_votes_notify_from: Optional[ForwardRef('TypeReactionNotificationsFrom')] = None)` |
| `types` | `ReadParticipantDate` | `ReadParticipantDate` | `(self, user_id: int, date: Optional[datetime.datetime])` |
| `types` | `ReceivedNotifyMessage` | `ReceivedNotifyMessage` | `(self, id: int, flags: int)` |
| `types` | `RecentMeUrlChat` | `RecentMeUrlChat` | `(self, url: str, chat_id: int)` |
| `types` | `RecentMeUrlChatInvite` | `RecentMeUrlChatInvite` | `(self, url: str, chat_invite: 'TypeChatInvite')` |
| `types` | `RecentMeUrlStickerSet` | `RecentMeUrlStickerSet` | `(self, url: str, set: 'TypeStickerSetCovered')` |
| `types` | `RecentMeUrlUnknown` | `RecentMeUrlUnknown` | `(self, url: str)` |
| `types` | `RecentMeUrlUser` | `RecentMeUrlUser` | `(self, url: str, user_id: int)` |
| `types` | `RecentStory` | `RecentStory` | `(self, live: Optional[bool] = None, max_id: Optional[int] = None)` |
| `types` | `ReplyInlineMarkup` | `ReplyInlineMarkup` | `(self, rows: List[ForwardRef('TypeKeyboardButtonRow')])` |
| `types` | `ReplyKeyboardForceReply` | `ReplyKeyboardForceReply` | `(self, single_use: Optional[bool] = None, selective: Optional[bool] = None, placeholder: Optional[str] = None)` |
| `types` | `ReplyKeyboardHide` | `ReplyKeyboardHide` | `(self, selective: Optional[bool] = None)` |
| `types` | `ReplyKeyboardMarkup` | `ReplyKeyboardMarkup` | `(self, rows: List[ForwardRef('TypeKeyboardButtonRow')], resize: Optional[bool] = None, single_use: Optional[bool] = None, selective: Optional[bool] = None, persistent: Optional[bool] = None, placeholder: Optional[str] = None)` |
| `types` | `ReportResultAddComment` | `ReportResultAddComment` | `(self, option: bytes, optional: Optional[bool] = None)` |
| `types` | `ReportResultChooseOption` | `ReportResultChooseOption` | `(self, title: str, options: List[ForwardRef('TypeMessageReportOption')])` |
| `types` | `ReportResultReported` | `ReportResultReported` | `(self, /, *args, **kwargs)` |
| `types` | `RequestPeerTypeBroadcast` | `RequestPeerTypeBroadcast` | `(self, creator: Optional[bool] = None, has_username: Optional[bool] = None, user_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, bot_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None)` |
| `types` | `RequestPeerTypeChat` | `RequestPeerTypeChat` | `(self, creator: Optional[bool] = None, bot_participant: Optional[bool] = None, has_username: Optional[bool] = None, forum: Optional[bool] = None, user_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, bot_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None)` |
| `types` | `RequestPeerTypeCreateBot` | `RequestPeerTypeCreateBot` | `(self, bot_managed: Optional[bool] = None, suggested_name: Optional[str] = None, suggested_username: Optional[str] = None)` |
| `types` | `RequestPeerTypeUser` | `RequestPeerTypeUser` | `(self, bot: Optional[bool] = None, premium: Optional[bool] = None)` |
| `types` | `RequestedPeerChannel` | `RequestedPeerChannel` | `(self, channel_id: int, title: Optional[str] = None, username: Optional[str] = None, photo: Optional[ForwardRef('TypePhoto')] = None)` |
| `types` | `RequestedPeerChat` | `RequestedPeerChat` | `(self, chat_id: int, title: Optional[str] = None, photo: Optional[ForwardRef('TypePhoto')] = None)` |
| `types` | `RequestedPeerUser` | `RequestedPeerUser` | `(self, user_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None, username: Optional[str] = None, photo: Optional[ForwardRef('TypePhoto')] = None)` |
| `types` | `RequirementToContactEmpty` | `RequirementToContactEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `RequirementToContactPaidMessages` | `RequirementToContactPaidMessages` | `(self, stars_amount: int)` |
| `types` | `RequirementToContactPremium` | `RequirementToContactPremium` | `(self, /, *args, **kwargs)` |
| `types` | `ResPQ` | `ResPQ` | `(self, nonce: int, server_nonce: int, pq: bytes, server_public_key_fingerprints: List[int])` |
| `types` | `RestrictionReason` | `RestrictionReason` | `(self, platform: str, reason: str, text: str)` |
| `types` | `RichMessage` | `RichMessage` | `(self, blocks: List[ForwardRef('TypePageBlock')], photos: List[ForwardRef('TypePhoto')], documents: List[ForwardRef('TypeDocument')], rtl: Optional[bool] = None, part: Optional[bool] = None)` |
| `types` | `RpcAnswerDropped` | `RpcAnswerDropped` | `(self, msg_id: int, seq_no: int, bytes: int)` |
| `types` | `RpcAnswerDroppedRunning` | `RpcAnswerDroppedRunning` | `(self, /, *args, **kwargs)` |
| `types` | `RpcAnswerUnknown` | `RpcAnswerUnknown` | `(self, /, *args, **kwargs)` |
| `types` | `RpcError` | `RpcError` | `(self, error_code: int, error_message: str)` |
| `types` | `SavedDialog` | `SavedDialog` | `(self, peer: 'TypePeer', top_message: int, pinned: Optional[bool] = None)` |
| `types` | `SavedPhoneContact` | `SavedPhoneContact` | `(self, phone: str, first_name: str, last_name: str, date: Optional[datetime.datetime])` |
| `types` | `SavedReactionTag` | `SavedReactionTag` | `(self, reaction: 'TypeReaction', count: int, title: Optional[str] = None)` |
| `types` | `SavedStarGift` | `SavedStarGift` | `(self, date: Optional[datetime.datetime], gift: 'TypeStarGift', name_hidden: Optional[bool] = None, unsaved: Optional[bool] = None, refunded: Optional[bool] = None, can_upgrade: Optional[bool] = None, pinned_to_top: Optional[bool] = None, upgrade_separate: Optional[bool] = None, from_id: Optional[ForwardRef('TypePeer')] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None, msg_id: Optional[int] = None, saved_id: Optional[int] = None, convert_stars: Optional[int] = None, upgrade_stars: Optional[int] = None, can_export_at: Optional[int] = None, transfer_stars: Optional[int] = None, can_transfer_at: Optional[int] = None, can_resell_at: Optional[int] = None, collection_id: Optional[List[int]] = None, prepaid_upgrade_hash: Optional[str] = None, drop_original_details_stars: Optional[int] = None, gift_num: Optional[int] = None, can_craft_at: Optional[int] = None)` |
| `types` | `SearchPostsFlood` | `SearchPostsFlood` | `(self, total_daily: int, remains: int, stars_amount: int, query_is_free: Optional[bool] = None, wait_till: Optional[int] = None)` |
| `types` | `SearchResultPosition` | `SearchResultPosition` | `(self, msg_id: int, date: Optional[datetime.datetime], offset: int)` |
| `types` | `SearchResultsCalendarPeriod` | `SearchResultsCalendarPeriod` | `(self, date: Optional[datetime.datetime], min_msg_id: int, max_msg_id: int, count: int)` |
| `types` | `SecureCredentialsEncrypted` | `SecureCredentialsEncrypted` | `(self, data: bytes, hash: bytes, secret: bytes)` |
| `types` | `SecureData` | `SecureData` | `(self, data: bytes, data_hash: bytes, secret: bytes)` |
| `types` | `SecureFile` | `SecureFile` | `(self, id: int, access_hash: int, size: int, dc_id: int, date: Optional[datetime.datetime], file_hash: bytes, secret: bytes)` |
| `types` | `SecureFileEmpty` | `SecureFileEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000` | `SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000` | `(self, salt: bytes)` |
| `types` | `SecurePasswordKdfAlgoSHA512` | `SecurePasswordKdfAlgoSHA512` | `(self, salt: bytes)` |
| `types` | `SecurePasswordKdfAlgoUnknown` | `SecurePasswordKdfAlgoUnknown` | `(self, /, *args, **kwargs)` |
| `types` | `SecurePlainEmail` | `SecurePlainEmail` | `(self, email: str)` |
| `types` | `SecurePlainPhone` | `SecurePlainPhone` | `(self, phone: str)` |
| `types` | `SecureRequiredType` | `SecureRequiredType` | `(self, type: 'TypeSecureValueType', native_names: Optional[bool] = None, selfie_required: Optional[bool] = None, translation_required: Optional[bool] = None)` |
| `types` | `SecureRequiredTypeOneOf` | `SecureRequiredTypeOneOf` | `(self, types: List[ForwardRef('TypeSecureRequiredType')])` |
| `types` | `SecureSecretSettings` | `SecureSecretSettings` | `(self, secure_algo: 'TypeSecurePasswordKdfAlgo', secure_secret: bytes, secure_secret_id: int)` |
| `types` | `SecureValue` | `SecureValue` | `(self, type: 'TypeSecureValueType', hash: bytes, data: Optional[ForwardRef('TypeSecureData')] = None, front_side: Optional[ForwardRef('TypeSecureFile')] = None, reverse_side: Optional[ForwardRef('TypeSecureFile')] = None, selfie: Optional[ForwardRef('TypeSecureFile')] = None, translation: Optional[List[ForwardRef('TypeSecureFile')]] = None, files: Optional[List[ForwardRef('TypeSecureFile')]] = None, plain_data: Optional[ForwardRef('TypeSecurePlainData')] = None)` |
| `types` | `SecureValueError` | `SecureValueError` | `(self, type: 'TypeSecureValueType', hash: bytes, text: str)` |
| `types` | `SecureValueErrorData` | `SecureValueErrorData` | `(self, type: 'TypeSecureValueType', data_hash: bytes, field: str, text: str)` |
| `types` | `SecureValueErrorFile` | `SecureValueErrorFile` | `(self, type: 'TypeSecureValueType', file_hash: bytes, text: str)` |
| `types` | `SecureValueErrorFiles` | `SecureValueErrorFiles` | `(self, type: 'TypeSecureValueType', file_hash: List[bytes], text: str)` |
| `types` | `SecureValueErrorFrontSide` | `SecureValueErrorFrontSide` | `(self, type: 'TypeSecureValueType', file_hash: bytes, text: str)` |
| `types` | `SecureValueErrorReverseSide` | `SecureValueErrorReverseSide` | `(self, type: 'TypeSecureValueType', file_hash: bytes, text: str)` |
| `types` | `SecureValueErrorSelfie` | `SecureValueErrorSelfie` | `(self, type: 'TypeSecureValueType', file_hash: bytes, text: str)` |
| `types` | `SecureValueErrorTranslationFile` | `SecureValueErrorTranslationFile` | `(self, type: 'TypeSecureValueType', file_hash: bytes, text: str)` |
| `types` | `SecureValueErrorTranslationFiles` | `SecureValueErrorTranslationFiles` | `(self, type: 'TypeSecureValueType', file_hash: List[bytes], text: str)` |
| `types` | `SecureValueHash` | `SecureValueHash` | `(self, type: 'TypeSecureValueType', hash: bytes)` |
| `types` | `SecureValueTypeAddress` | `SecureValueTypeAddress` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeBankStatement` | `SecureValueTypeBankStatement` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeDriverLicense` | `SecureValueTypeDriverLicense` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeEmail` | `SecureValueTypeEmail` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeIdentityCard` | `SecureValueTypeIdentityCard` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeInternalPassport` | `SecureValueTypeInternalPassport` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypePassport` | `SecureValueTypePassport` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypePassportRegistration` | `SecureValueTypePassportRegistration` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypePersonalDetails` | `SecureValueTypePersonalDetails` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypePhone` | `SecureValueTypePhone` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeRentalAgreement` | `SecureValueTypeRentalAgreement` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeTemporaryRegistration` | `SecureValueTypeTemporaryRegistration` | `(self, /, *args, **kwargs)` |
| `types` | `SecureValueTypeUtilityBill` | `SecureValueTypeUtilityBill` | `(self, /, *args, **kwargs)` |
| `types` | `SendAsPeer` | `SendAsPeer` | `(self, peer: 'TypePeer', premium_required: Optional[bool] = None)` |
| `types` | `SendMessageCancelAction` | `SendMessageCancelAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageChooseContactAction` | `SendMessageChooseContactAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageChooseStickerAction` | `SendMessageChooseStickerAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageEmojiInteraction` | `SendMessageEmojiInteraction` | `(self, emoticon: str, msg_id: int, interaction: 'TypeDataJSON')` |
| `types` | `SendMessageEmojiInteractionSeen` | `SendMessageEmojiInteractionSeen` | `(self, emoticon: str)` |
| `types` | `SendMessageGamePlayAction` | `SendMessageGamePlayAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageGeoLocationAction` | `SendMessageGeoLocationAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageHistoryImportAction` | `SendMessageHistoryImportAction` | `(self, progress: int)` |
| `types` | `SendMessageRecordAudioAction` | `SendMessageRecordAudioAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageRecordRoundAction` | `SendMessageRecordRoundAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageRecordVideoAction` | `SendMessageRecordVideoAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageRichMessageDraftAction` | `SendMessageRichMessageDraftAction` | `(self, rich_message: 'TypeRichMessage', random_id: int = None)` |
| `types` | `SendMessageTextDraftAction` | `SendMessageTextDraftAction` | `(self, text: 'TypeTextWithEntities', random_id: int = None)` |
| `types` | `SendMessageTypingAction` | `SendMessageTypingAction` | `(self, /, *args, **kwargs)` |
| `types` | `SendMessageUploadAudioAction` | `SendMessageUploadAudioAction` | `(self, progress: int)` |
| `types` | `SendMessageUploadDocumentAction` | `SendMessageUploadDocumentAction` | `(self, progress: int)` |
| `types` | `SendMessageUploadPhotoAction` | `SendMessageUploadPhotoAction` | `(self, progress: int)` |
| `types` | `SendMessageUploadRoundAction` | `SendMessageUploadRoundAction` | `(self, progress: int)` |
| `types` | `SendMessageUploadVideoAction` | `SendMessageUploadVideoAction` | `(self, progress: int)` |
| `types` | `ServerDHInnerData` | `ServerDHInnerData` | `(self, nonce: int, server_nonce: int, g: int, dh_prime: bytes, g_a: bytes, server_time: int)` |
| `types` | `ServerDHParamsFail` | `ServerDHParamsFail` | `(self, nonce: int, server_nonce: int, new_nonce_hash: int)` |
| `types` | `ServerDHParamsOk` | `ServerDHParamsOk` | `(self, nonce: int, server_nonce: int, encrypted_answer: bytes)` |
| `types` | `ShippingOption` | `ShippingOption` | `(self, id: str, title: str, prices: List[ForwardRef('TypeLabeledPrice')])` |
| `types` | `SmsJob` | `SmsJob` | `(self, job_id: str, phone_number: str, text: str)` |
| `types` | `SpeakingInGroupCallAction` | `SpeakingInGroupCallAction` | `(self, /, *args, **kwargs)` |
| `types` | `SponsoredMessage` | `SponsoredMessage` | `(self, url: str, title: str, message: str, button_text: str, recommended: Optional[bool] = None, can_report: Optional[bool] = None, random_id: bytes = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, photo: Optional[ForwardRef('TypePhoto')] = None, media: Optional[ForwardRef('TypeMessageMedia')] = None, color: Optional[ForwardRef('TypePeerColor')] = None, sponsor_info: Optional[str] = None, additional_info: Optional[str] = None, min_display_duration: Optional[int] = None, max_display_duration: Optional[int] = None)` |
| `types` | `SponsoredMessageReportOption` | `SponsoredMessageReportOption` | `(self, text: str, option: bytes)` |
| `types` | `SponsoredPeer` | `SponsoredPeer` | `(self, peer: 'TypePeer', random_id: bytes = None, sponsor_info: Optional[str] = None, additional_info: Optional[str] = None)` |
| `types` | `StarGift` | `StarGift` | `(self, id: int, sticker: 'TypeDocument', stars: int, convert_stars: int, limited: Optional[bool] = None, sold_out: Optional[bool] = None, birthday: Optional[bool] = None, require_premium: Optional[bool] = None, limited_per_user: Optional[bool] = None, peer_color_available: Optional[bool] = None, auction: Optional[bool] = None, availability_remains: Optional[int] = None, availability_total: Optional[int] = None, availability_resale: Optional[int] = None, first_sale_date: Optional[datetime.datetime] = None, last_sale_date: Optional[datetime.datetime] = None, upgrade_stars: Optional[int] = None, resell_min_stars: Optional[int] = None, title: Optional[str] = None, released_by: Optional[ForwardRef('TypePeer')] = None, per_user_total: Optional[int] = None, per_user_remains: Optional[int] = None, locked_until_date: Optional[datetime.datetime] = None, auction_slug: Optional[str] = None, gifts_per_round: Optional[int] = None, auction_start_date: Optional[datetime.datetime] = None, upgrade_variants: Optional[int] = None, background: Optional[ForwardRef('TypeStarGiftBackground')] = None)` |
| `types` | `StarGiftActiveAuctionState` | `StarGiftActiveAuctionState` | `(self, gift: 'TypeStarGift', state: 'TypeStarGiftAuctionState', user_state: 'TypeStarGiftAuctionUserState')` |
| `types` | `StarGiftAttributeBackdrop` | `StarGiftAttributeBackdrop` | `(self, name: str, backdrop_id: int, center_color: int, edge_color: int, pattern_color: int, text_color: int, rarity: 'TypeStarGiftAttributeRarity')` |
| `types` | `StarGiftAttributeCounter` | `StarGiftAttributeCounter` | `(self, attribute: 'TypeStarGiftAttributeId', count: int)` |
| `types` | `StarGiftAttributeIdBackdrop` | `StarGiftAttributeIdBackdrop` | `(self, backdrop_id: int)` |
| `types` | `StarGiftAttributeIdModel` | `StarGiftAttributeIdModel` | `(self, document_id: int)` |
| `types` | `StarGiftAttributeIdPattern` | `StarGiftAttributeIdPattern` | `(self, document_id: int)` |
| `types` | `StarGiftAttributeModel` | `StarGiftAttributeModel` | `(self, name: str, document: 'TypeDocument', rarity: 'TypeStarGiftAttributeRarity', crafted: Optional[bool] = None)` |
| `types` | `StarGiftAttributeOriginalDetails` | `StarGiftAttributeOriginalDetails` | `(self, recipient_id: 'TypePeer', date: Optional[datetime.datetime], sender_id: Optional[ForwardRef('TypePeer')] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `StarGiftAttributePattern` | `StarGiftAttributePattern` | `(self, name: str, document: 'TypeDocument', rarity: 'TypeStarGiftAttributeRarity')` |
| `types` | `StarGiftAttributeRarity` | `StarGiftAttributeRarity` | `(self, permille: int)` |
| `types` | `StarGiftAttributeRarityEpic` | `StarGiftAttributeRarityEpic` | `(self, /, *args, **kwargs)` |
| `types` | `StarGiftAttributeRarityLegendary` | `StarGiftAttributeRarityLegendary` | `(self, /, *args, **kwargs)` |
| `types` | `StarGiftAttributeRarityRare` | `StarGiftAttributeRarityRare` | `(self, /, *args, **kwargs)` |
| `types` | `StarGiftAttributeRarityUncommon` | `StarGiftAttributeRarityUncommon` | `(self, /, *args, **kwargs)` |
| `types` | `StarGiftAuctionAcquiredGift` | `StarGiftAuctionAcquiredGift` | `(self, peer: 'TypePeer', date: Optional[datetime.datetime], bid_amount: int, round: int, pos: int, name_hidden: Optional[bool] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None, gift_num: Optional[int] = None)` |
| `types` | `StarGiftAuctionRound` | `StarGiftAuctionRound` | `(self, num: int, duration: int)` |
| `types` | `StarGiftAuctionRoundExtendable` | `StarGiftAuctionRoundExtendable` | `(self, num: int, duration: int, extend_top: int, extend_window: int)` |
| `types` | `StarGiftAuctionState` | `StarGiftAuctionState` | `(self, version: int, start_date: Optional[datetime.datetime], end_date: Optional[datetime.datetime], min_bid_amount: int, bid_levels: List[ForwardRef('TypeAuctionBidLevel')], top_bidders: List[int], next_round_at: int, last_gift_num: int, gifts_left: int, current_round: int, total_rounds: int, rounds: List[ForwardRef('TypeStarGiftAuctionRound')])` |
| `types` | `StarGiftAuctionStateFinished` | `StarGiftAuctionStateFinished` | `(self, start_date: Optional[datetime.datetime], end_date: Optional[datetime.datetime], average_price: int, listed_count: Optional[int] = None, fragment_listed_count: Optional[int] = None, fragment_listed_url: Optional[str] = None)` |
| `types` | `StarGiftAuctionStateNotModified` | `StarGiftAuctionStateNotModified` | `(self, /, *args, **kwargs)` |
| `types` | `StarGiftAuctionUserState` | `StarGiftAuctionUserState` | `(self, acquired_count: int, returned: Optional[bool] = None, bid_amount: Optional[int] = None, bid_date: Optional[datetime.datetime] = None, min_bid_amount: Optional[int] = None, bid_peer: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `StarGiftBackground` | `StarGiftBackground` | `(self, center_color: int, edge_color: int, text_color: int)` |
| `types` | `StarGiftCollection` | `StarGiftCollection` | `(self, collection_id: int, title: str, gifts_count: int, hash: int, icon: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `StarGiftUnique` | `StarGiftUnique` | `(self, id: int, gift_id: int, title: str, slug: str, num: int, attributes: List[ForwardRef('TypeStarGiftAttribute')], availability_issued: int, availability_total: int, require_premium: Optional[bool] = None, resale_ton_only: Optional[bool] = None, theme_available: Optional[bool] = None, burned: Optional[bool] = None, crafted: Optional[bool] = None, owner_id: Optional[ForwardRef('TypePeer')] = None, owner_name: Optional[str] = None, owner_address: Optional[str] = None, gift_address: Optional[str] = None, resell_amount: Optional[List[ForwardRef('TypeStarsAmount')]] = None, released_by: Optional[ForwardRef('TypePeer')] = None, value_amount: Optional[int] = None, value_currency: Optional[str] = None, value_usd_amount: Optional[int] = None, theme_peer: Optional[ForwardRef('TypePeer')] = None, peer_color: Optional[ForwardRef('TypePeerColor')] = None, host_id: Optional[ForwardRef('TypePeer')] = None, offer_min_stars: Optional[int] = None, craft_chance_permille: Optional[int] = None)` |
| `types` | `StarGiftUpgradePrice` | `StarGiftUpgradePrice` | `(self, date: Optional[datetime.datetime], upgrade_stars: int)` |
| `types` | `StarRefProgram` | `StarRefProgram` | `(self, bot_id: int, commission_permille: int, duration_months: Optional[int] = None, end_date: Optional[datetime.datetime] = None, daily_revenue_per_user: Optional[ForwardRef('TypeStarsAmount')] = None)` |
| `types` | `StarsAmount` | `StarsAmount` | `(self, amount: int, nanos: int)` |
| `types` | `StarsGiftOption` | `StarsGiftOption` | `(self, stars: int, currency: str, amount: int, extended: Optional[bool] = None, store_product: Optional[str] = None)` |
| `types` | `StarsGiveawayOption` | `StarsGiveawayOption` | `(self, stars: int, yearly_boosts: int, currency: str, amount: int, winners: List[ForwardRef('TypeStarsGiveawayWinnersOption')], extended: Optional[bool] = None, default: Optional[bool] = None, store_product: Optional[str] = None)` |
| `types` | `StarsGiveawayWinnersOption` | `StarsGiveawayWinnersOption` | `(self, users: int, per_user_stars: int, default: Optional[bool] = None)` |
| `types` | `StarsRating` | `StarsRating` | `(self, level: int, current_level_stars: int, stars: int, next_level_stars: Optional[int] = None)` |
| `types` | `StarsRevenueStatus` | `StarsRevenueStatus` | `(self, current_balance: 'TypeStarsAmount', available_balance: 'TypeStarsAmount', overall_revenue: 'TypeStarsAmount', withdrawal_enabled: Optional[bool] = None, next_withdrawal_at: Optional[int] = None)` |
| `types` | `StarsSubscription` | `StarsSubscription` | `(self, id: str, peer: 'TypePeer', until_date: Optional[datetime.datetime], pricing: 'TypeStarsSubscriptionPricing', canceled: Optional[bool] = None, can_refulfill: Optional[bool] = None, missing_balance: Optional[bool] = None, bot_canceled: Optional[bool] = None, chat_invite_hash: Optional[str] = None, title: Optional[str] = None, photo: Optional[ForwardRef('TypeWebDocument')] = None, invoice_slug: Optional[str] = None)` |
| `types` | `StarsSubscriptionPricing` | `StarsSubscriptionPricing` | `(self, period: int, amount: int)` |
| `types` | `StarsTonAmount` | `StarsTonAmount` | `(self, amount: int)` |
| `types` | `StarsTopupOption` | `StarsTopupOption` | `(self, stars: int, currency: str, amount: int, extended: Optional[bool] = None, store_product: Optional[str] = None)` |
| `types` | `StarsTransaction` | `StarsTransaction` | `(self, id: str, amount: 'TypeStarsAmount', date: Optional[datetime.datetime], peer: 'TypeStarsTransactionPeer', refund: Optional[bool] = None, pending: Optional[bool] = None, failed: Optional[bool] = None, gift: Optional[bool] = None, reaction: Optional[bool] = None, stargift_upgrade: Optional[bool] = None, business_transfer: Optional[bool] = None, stargift_resale: Optional[bool] = None, posts_search: Optional[bool] = None, stargift_prepaid_upgrade: Optional[bool] = None, stargift_drop_original_details: Optional[bool] = None, phonegroup_message: Optional[bool] = None, stargift_auction_bid: Optional[bool] = None, offer: Optional[bool] = None, title: Optional[str] = None, description: Optional[str] = None, photo: Optional[ForwardRef('TypeWebDocument')] = None, transaction_date: Optional[datetime.datetime] = None, transaction_url: Optional[str] = None, bot_payload: Optional[bytes] = None, msg_id: Optional[int] = None, extended_media: Optional[List[ForwardRef('TypeMessageMedia')]] = None, subscription_period: Optional[int] = None, giveaway_post_id: Optional[int] = None, stargift: Optional[ForwardRef('TypeStarGift')] = None, floodskip_number: Optional[int] = None, starref_commission_permille: Optional[int] = None, starref_peer: Optional[ForwardRef('TypePeer')] = None, starref_amount: Optional[ForwardRef('TypeStarsAmount')] = None, paid_messages: Optional[int] = None, premium_gift_months: Optional[int] = None, ads_proceeds_from_date: Optional[datetime.datetime] = None, ads_proceeds_to_date: Optional[datetime.datetime] = None)` |
| `types` | `StarsTransactionPeer` | `StarsTransactionPeer` | `(self, peer: 'TypePeer')` |
| `types` | `StarsTransactionPeerAPI` | `StarsTransactionPeerAPI` | `(self, /, *args, **kwargs)` |
| `types` | `StarsTransactionPeerAds` | `StarsTransactionPeerAds` | `(self, /, *args, **kwargs)` |
| `types` | `StarsTransactionPeerAppStore` | `StarsTransactionPeerAppStore` | `(self, /, *args, **kwargs)` |
| `types` | `StarsTransactionPeerFragment` | `StarsTransactionPeerFragment` | `(self, /, *args, **kwargs)` |
| `types` | `StarsTransactionPeerPlayMarket` | `StarsTransactionPeerPlayMarket` | `(self, /, *args, **kwargs)` |
| `types` | `StarsTransactionPeerPremiumBot` | `StarsTransactionPeerPremiumBot` | `(self, /, *args, **kwargs)` |
| `types` | `StarsTransactionPeerUnsupported` | `StarsTransactionPeerUnsupported` | `(self, /, *args, **kwargs)` |
| `types` | `StatsAbsValueAndPrev` | `StatsAbsValueAndPrev` | `(self, current: float, previous: float)` |
| `types` | `StatsDateRangeDays` | `StatsDateRangeDays` | `(self, min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime])` |
| `types` | `StatsGraph` | `StatsGraph` | `(self, json: 'TypeDataJSON', zoom_token: Optional[str] = None)` |
| `types` | `StatsGraphAsync` | `StatsGraphAsync` | `(self, token: str)` |
| `types` | `StatsGraphError` | `StatsGraphError` | `(self, error: str)` |
| `types` | `StatsGroupTopAdmin` | `StatsGroupTopAdmin` | `(self, user_id: int, deleted: int, kicked: int, banned: int)` |
| `types` | `StatsGroupTopInviter` | `StatsGroupTopInviter` | `(self, user_id: int, invitations: int)` |
| `types` | `StatsGroupTopPoster` | `StatsGroupTopPoster` | `(self, user_id: int, messages: int, avg_chars: int)` |
| `types` | `StatsPercentValue` | `StatsPercentValue` | `(self, part: float, total: float)` |
| `types` | `StatsURL` | `StatsURL` | `(self, url: str)` |
| `types` | `StickerKeyword` | `StickerKeyword` | `(self, document_id: int, keyword: List[str])` |
| `types` | `StickerPack` | `StickerPack` | `(self, emoticon: str, documents: List[int])` |
| `types` | `StickerSet` | `StickerSet` | `(self, id: int, access_hash: int, title: str, short_name: str, count: int, hash: int, archived: Optional[bool] = None, official: Optional[bool] = None, masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, channel_emoji_status: Optional[bool] = None, creator: Optional[bool] = None, installed_date: Optional[datetime.datetime] = None, thumbs: Optional[List[ForwardRef('TypePhotoSize')]] = None, thumb_dc_id: Optional[int] = None, thumb_version: Optional[int] = None, thumb_document_id: Optional[int] = None)` |
| `types` | `StickerSetCovered` | `StickerSetCovered` | `(self, set: 'TypeStickerSet', cover: 'TypeDocument')` |
| `types` | `StickerSetFullCovered` | `StickerSetFullCovered` | `(self, set: 'TypeStickerSet', packs: List[ForwardRef('TypeStickerPack')], keywords: List[ForwardRef('TypeStickerKeyword')], documents: List[ForwardRef('TypeDocument')])` |
| `types` | `StickerSetMultiCovered` | `StickerSetMultiCovered` | `(self, set: 'TypeStickerSet', covers: List[ForwardRef('TypeDocument')])` |
| `types` | `StickerSetNoCovered` | `StickerSetNoCovered` | `(self, set: 'TypeStickerSet')` |
| `types` | `StoriesStealthMode` | `StoriesStealthMode` | `(self, active_until_date: Optional[datetime.datetime] = None, cooldown_until_date: Optional[datetime.datetime] = None)` |
| `types` | `StoryAlbum` | `StoryAlbum` | `(self, album_id: int, title: str, icon_photo: Optional[ForwardRef('TypePhoto')] = None, icon_video: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `StoryFwdHeader` | `StoryFwdHeader` | `(self, modified: Optional[bool] = None, from_: Optional[ForwardRef('TypePeer')] = None, from_name: Optional[str] = None, story_id: Optional[int] = None)` |
| `types` | `StoryItem` | `StoryItem` | `(self, id: int, date: Optional[datetime.datetime], expire_date: Optional[datetime.datetime], media: 'TypeMessageMedia', pinned: Optional[bool] = None, public: Optional[bool] = None, close_friends: Optional[bool] = None, min: Optional[bool] = None, noforwards: Optional[bool] = None, edited: Optional[bool] = None, contacts: Optional[bool] = None, selected_contacts: Optional[bool] = None, out: Optional[bool] = None, from_id: Optional[ForwardRef('TypePeer')] = None, fwd_from: Optional[ForwardRef('TypeStoryFwdHeader')] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, media_areas: Optional[List[ForwardRef('TypeMediaArea')]] = None, privacy: Optional[List[ForwardRef('TypePrivacyRule')]] = None, views: Optional[ForwardRef('TypeStoryViews')] = None, sent_reaction: Optional[ForwardRef('TypeReaction')] = None, albums: Optional[List[int]] = None, music: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `StoryItemDeleted` | `StoryItemDeleted` | `(self, id: int)` |
| `types` | `StoryItemSkipped` | `StoryItemSkipped` | `(self, id: int, date: Optional[datetime.datetime], expire_date: Optional[datetime.datetime], close_friends: Optional[bool] = None, live: Optional[bool] = None)` |
| `types` | `StoryReaction` | `StoryReaction` | `(self, peer_id: 'TypePeer', date: Optional[datetime.datetime], reaction: 'TypeReaction')` |
| `types` | `StoryReactionPublicForward` | `StoryReactionPublicForward` | `(self, message: 'TypeMessage')` |
| `types` | `StoryReactionPublicRepost` | `StoryReactionPublicRepost` | `(self, peer_id: 'TypePeer', story: 'TypeStoryItem')` |
| `types` | `StoryView` | `StoryView` | `(self, user_id: int, date: Optional[datetime.datetime], blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None, reaction: Optional[ForwardRef('TypeReaction')] = None)` |
| `types` | `StoryViewPublicForward` | `StoryViewPublicForward` | `(self, message: 'TypeMessage', blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None)` |
| `types` | `StoryViewPublicRepost` | `StoryViewPublicRepost` | `(self, peer_id: 'TypePeer', story: 'TypeStoryItem', blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None)` |
| `types` | `StoryViews` | `StoryViews` | `(self, views_count: int, has_viewers: Optional[bool] = None, forwards_count: Optional[int] = None, reactions: Optional[List[ForwardRef('TypeReactionCount')]] = None, reactions_count: Optional[int] = None, recent_viewers: Optional[List[int]] = None)` |
| `types` | `SuggestedPost` | `SuggestedPost` | `(self, accepted: Optional[bool] = None, rejected: Optional[bool] = None, price: Optional[ForwardRef('TypeStarsAmount')] = None, schedule_date: Optional[datetime.datetime] = None)` |
| `types` | `TextAnchor` | `TextAnchor` | `(self, text: 'TypeRichText', name: str)` |
| `types` | `TextAutoEmail` | `TextAutoEmail` | `(self, text: 'TypeRichText')` |
| `types` | `TextAutoPhone` | `TextAutoPhone` | `(self, text: 'TypeRichText')` |
| `types` | `TextAutoUrl` | `TextAutoUrl` | `(self, text: 'TypeRichText')` |
| `types` | `TextBankCard` | `TextBankCard` | `(self, text: 'TypeRichText')` |
| `types` | `TextBold` | `TextBold` | `(self, text: 'TypeRichText')` |
| `types` | `TextBotCommand` | `TextBotCommand` | `(self, text: 'TypeRichText')` |
| `types` | `TextCashtag` | `TextCashtag` | `(self, text: 'TypeRichText')` |
| `types` | `TextConcat` | `TextConcat` | `(self, texts: List[ForwardRef('TypeRichText')])` |
| `types` | `TextCustomEmoji` | `TextCustomEmoji` | `(self, document_id: int, alt: str)` |
| `types` | `TextDate` | `TextDate` | `(self, text: 'TypeRichText', date: Optional[datetime.datetime], relative: Optional[bool] = None, short_time: Optional[bool] = None, long_time: Optional[bool] = None, short_date: Optional[bool] = None, long_date: Optional[bool] = None, day_of_week: Optional[bool] = None)` |
| `types` | `TextEmail` | `TextEmail` | `(self, text: 'TypeRichText', email: str)` |
| `types` | `TextEmpty` | `TextEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `TextFixed` | `TextFixed` | `(self, text: 'TypeRichText')` |
| `types` | `TextHashtag` | `TextHashtag` | `(self, text: 'TypeRichText')` |
| `types` | `TextImage` | `TextImage` | `(self, document_id: int, w: int, h: int)` |
| `types` | `TextItalic` | `TextItalic` | `(self, text: 'TypeRichText')` |
| `types` | `TextMarked` | `TextMarked` | `(self, text: 'TypeRichText')` |
| `types` | `TextMath` | `TextMath` | `(self, source: str)` |
| `types` | `TextMention` | `TextMention` | `(self, text: 'TypeRichText')` |
| `types` | `TextMentionName` | `TextMentionName` | `(self, text: 'TypeRichText', user_id: int)` |
| `types` | `TextPhone` | `TextPhone` | `(self, text: 'TypeRichText', phone: str)` |
| `types` | `TextPlain` | `TextPlain` | `(self, text: str)` |
| `types` | `TextSpoiler` | `TextSpoiler` | `(self, text: 'TypeRichText')` |
| `types` | `TextStrike` | `TextStrike` | `(self, text: 'TypeRichText')` |
| `types` | `TextSubscript` | `TextSubscript` | `(self, text: 'TypeRichText')` |
| `types` | `TextSuperscript` | `TextSuperscript` | `(self, text: 'TypeRichText')` |
| `types` | `TextUnderline` | `TextUnderline` | `(self, text: 'TypeRichText')` |
| `types` | `TextUrl` | `TextUrl` | `(self, text: 'TypeRichText', url: str, webpage_id: int)` |
| `types` | `TextWithEntities` | `TextWithEntities` | `(self, text: str, entities: List[ForwardRef('TypeMessageEntity')])` |
| `types` | `Theme` | `Theme` | `(self, id: int, access_hash: int, slug: str, title: str, creator: Optional[bool] = None, default: Optional[bool] = None, for_chat: Optional[bool] = None, document: Optional[ForwardRef('TypeDocument')] = None, settings: Optional[List[ForwardRef('TypeThemeSettings')]] = None, emoticon: Optional[str] = None, installs_count: Optional[int] = None)` |
| `types` | `ThemeSettings` | `ThemeSettings` | `(self, base_theme: 'TypeBaseTheme', accent_color: int, message_colors_animated: Optional[bool] = None, outbox_accent_color: Optional[int] = None, message_colors: Optional[List[int]] = None, wallpaper: Optional[ForwardRef('TypeWallPaper')] = None)` |
| `types` | `Timezone` | `Timezone` | `(self, id: str, name: str, utc_offset: int)` |
| `types` | `TlsBlockDomain` | `TlsBlockDomain` | `(self, /, *args, **kwargs)` |
| `types` | `TlsBlockGrease` | `TlsBlockGrease` | `(self, seed: int)` |
| `types` | `TlsBlockPublicKey` | `TlsBlockPublicKey` | `(self, /, *args, **kwargs)` |
| `types` | `TlsBlockRandom` | `TlsBlockRandom` | `(self, length: int)` |
| `types` | `TlsBlockScope` | `TlsBlockScope` | `(self, entries: List[ForwardRef('TypeTlsBlock')])` |
| `types` | `TlsBlockString` | `TlsBlockString` | `(self, data: str)` |
| `types` | `TlsBlockZero` | `TlsBlockZero` | `(self, length: int)` |
| `types` | `TlsClientHello` | `TlsClientHello` | `(self, blocks: List[ForwardRef('TypeTlsBlock')])` |
| `types` | `TodoCompletion` | `TodoCompletion` | `(self, id: int, completed_by: 'TypePeer', date: Optional[datetime.datetime])` |
| `types` | `TodoItem` | `TodoItem` | `(self, id: int, title: 'TypeTextWithEntities')` |
| `types` | `TodoList` | `TodoList` | `(self, title: 'TypeTextWithEntities', list: List[ForwardRef('TypeTodoItem')], others_can_append: Optional[bool] = None, others_can_complete: Optional[bool] = None)` |
| `types` | `TopPeer` | `TopPeer` | `(self, peer: 'TypePeer', rating: float)` |
| `types` | `TopPeerCategoryBotsApp` | `TopPeerCategoryBotsApp` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryBotsGuestChat` | `TopPeerCategoryBotsGuestChat` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryBotsInline` | `TopPeerCategoryBotsInline` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryBotsPM` | `TopPeerCategoryBotsPM` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryChannels` | `TopPeerCategoryChannels` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryCorrespondents` | `TopPeerCategoryCorrespondents` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryForwardChats` | `TopPeerCategoryForwardChats` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryForwardUsers` | `TopPeerCategoryForwardUsers` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryGroups` | `TopPeerCategoryGroups` | `(self, /, *args, **kwargs)` |
| `types` | `TopPeerCategoryPeers` | `TopPeerCategoryPeers` | `(self, category: 'TypeTopPeerCategory', count: int, peers: List[ForwardRef('TypeTopPeer')])` |
| `types` | `TopPeerCategoryPhoneCalls` | `TopPeerCategoryPhoneCalls` | `(self, /, *args, **kwargs)` |
| `types` | `TypeAccessPointRule` | `TypeAccessPointRule` | `(self, phone_prefix_rules: str, dc_id: int, ips: List[ForwardRef('TypeIpPort')])` |
| `types` | `TypeAccountDaysTTL` | `TypeAccountDaysTTL` | `(self, days: int)` |
| `types` | `TypeAiComposeToneExample` | `TypeAiComposeToneExample` | `(self, from_: 'TypeTextWithEntities', to: 'TypeTextWithEntities')` |
| `types` | `TypeAttachMenuBot` | `TypeAttachMenuBot` | `(self, bot_id: int, short_name: str, icons: List[ForwardRef('TypeAttachMenuBotIcon')], inactive: Optional[bool] = None, has_settings: Optional[bool] = None, request_write_access: Optional[bool] = None, show_in_attach_menu: Optional[bool] = None, show_in_side_menu: Optional[bool] = None, side_menu_disclaimer_needed: Optional[bool] = None, peer_types: Optional[List[ForwardRef('TypeAttachMenuPeerType')]] = None)` |
| `types` | `TypeAttachMenuBotIcon` | `TypeAttachMenuBotIcon` | `(self, name: str, icon: 'TypeDocument', colors: Optional[List[ForwardRef('TypeAttachMenuBotIconColor')]] = None)` |
| `types` | `TypeAttachMenuBotIconColor` | `TypeAttachMenuBotIconColor` | `(self, name: str, color: int)` |
| `types` | `TypeAttachMenuBotsBot` | `TypeAttachMenuBotsBot` | `(self, bot: 'TypeAttachMenuBot', users: List[ForwardRef('TypeUser')])` |
| `types` | `TypeAuctionBidLevel` | `TypeAuctionBidLevel` | `(self, pos: int, amount: int, date: Optional[datetime.datetime])` |
| `types` | `TypeAuthorization` | `TypeAuthorization` | `(self, hash: int, device_model: str, platform: str, system_version: str, api_id: int, app_name: str, app_version: str, date_created: Optional[datetime.datetime], date_active: Optional[datetime.datetime], ip: str, country: str, region: str, current: Optional[bool] = None, official_app: Optional[bool] = None, password_pending: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None, unconfirmed: Optional[bool] = None)` |
| `types` | `TypeAutoDownloadSettings` | `TypeAutoDownloadSettings` | `(self, photo_size_max: int, video_size_max: int, file_size_max: int, video_upload_maxbitrate: int, small_queue_active_operations_max: int, large_queue_active_operations_max: int, disabled: Optional[bool] = None, video_preload_large: Optional[bool] = None, audio_preload_next: Optional[bool] = None, phonecalls_less_data: Optional[bool] = None, stories_preload: Optional[bool] = None)` |
| `types` | `TypeAutoSaveException` | `TypeAutoSaveException` | `(self, peer: 'TypePeer', settings: 'TypeAutoSaveSettings')` |
| `types` | `TypeAutoSaveSettings` | `TypeAutoSaveSettings` | `(self, photos: Optional[bool] = None, videos: Optional[bool] = None, video_max_size: Optional[int] = None)` |
| `types` | `TypeAvailableEffect` | `TypeAvailableEffect` | `(self, id: int, emoticon: str, effect_sticker_id: int, premium_required: Optional[bool] = None, static_icon_id: Optional[int] = None, effect_animation_id: Optional[int] = None)` |
| `types` | `TypeAvailableReaction` | `TypeAvailableReaction` | `(self, reaction: str, title: str, static_icon: 'TypeDocument', appear_animation: 'TypeDocument', select_animation: 'TypeDocument', activate_animation: 'TypeDocument', effect_animation: 'TypeDocument', inactive: Optional[bool] = None, premium: Optional[bool] = None, around_animation: Optional[ForwardRef('TypeDocument')] = None, center_icon: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `TypeBankCardOpenUrl` | `TypeBankCardOpenUrl` | `(self, url: str, name: str)` |
| `types` | `TypeBindAuthKeyInner` | `TypeBindAuthKeyInner` | `(self, nonce: int, temp_auth_key_id: int, perm_auth_key_id: int, temp_session_id: int, expires_at: Optional[datetime.datetime])` |
| `types` | `TypeBirthday` | `TypeBirthday` | `(self, day: int, month: int, year: Optional[int] = None)` |
| `types` | `TypeBoost` | `TypeBoost` | `(self, id: str, date: Optional[datetime.datetime], expires: Optional[datetime.datetime], gift: Optional[bool] = None, giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, user_id: Optional[int] = None, giveaway_msg_id: Optional[int] = None, used_gift_slug: Optional[str] = None, multiplier: Optional[int] = None, stars: Optional[int] = None)` |
| `types` | `TypeBotAppSettings` | `TypeBotAppSettings` | `(self, placeholder_path: Optional[bytes] = None, background_color: Optional[int] = None, background_dark_color: Optional[int] = None, header_color: Optional[int] = None, header_dark_color: Optional[int] = None)` |
| `types` | `TypeBotBusinessConnection` | `TypeBotBusinessConnection` | `(self, connection_id: str, user_id: int, dc_id: int, date: Optional[datetime.datetime], disabled: Optional[bool] = None, rights: Optional[ForwardRef('TypeBusinessBotRights')] = None)` |
| `types` | `TypeBotCommand` | `TypeBotCommand` | `(self, command: str, description: str)` |
| `types` | `TypeBotInfo` | `TypeBotInfo` | `(self, has_preview_medias: Optional[bool] = None, user_id: Optional[int] = None, description: Optional[str] = None, description_photo: Optional[ForwardRef('TypePhoto')] = None, description_document: Optional[ForwardRef('TypeDocument')] = None, commands: Optional[List[ForwardRef('TypeBotCommand')]] = None, menu_button: Optional[ForwardRef('TypeBotMenuButton')] = None, privacy_policy_url: Optional[str] = None, app_settings: Optional[ForwardRef('TypeBotAppSettings')] = None, verifier_settings: Optional[ForwardRef('TypeBotVerifierSettings')] = None)` |
| `types` | `TypeBotPreviewMedia` | `TypeBotPreviewMedia` | `(self, date: Optional[datetime.datetime], media: 'TypeMessageMedia')` |
| `types` | `TypeBotVerification` | `TypeBotVerification` | `(self, bot_id: int, icon: int, description: str)` |
| `types` | `TypeBotVerifierSettings` | `TypeBotVerifierSettings` | `(self, icon: int, company: str, can_modify_custom_description: Optional[bool] = None, custom_description: Optional[str] = None)` |
| `types` | `TypeBusinessAwayMessage` | `TypeBusinessAwayMessage` | `(self, shortcut_id: int, schedule: 'TypeBusinessAwayMessageSchedule', recipients: 'TypeBusinessRecipients', offline_only: Optional[bool] = None)` |
| `types` | `TypeBusinessBotRecipients` | `TypeBusinessBotRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[int]] = None, exclude_users: Optional[List[int]] = None)` |
| `types` | `TypeBusinessBotRights` | `TypeBusinessBotRights` | `(self, reply: Optional[bool] = None, read_messages: Optional[bool] = None, delete_sent_messages: Optional[bool] = None, delete_received_messages: Optional[bool] = None, edit_name: Optional[bool] = None, edit_bio: Optional[bool] = None, edit_profile_photo: Optional[bool] = None, edit_username: Optional[bool] = None, view_gifts: Optional[bool] = None, sell_gifts: Optional[bool] = None, change_gift_settings: Optional[bool] = None, transfer_and_upgrade_gifts: Optional[bool] = None, transfer_stars: Optional[bool] = None, manage_stories: Optional[bool] = None)` |
| `types` | `TypeBusinessChatLink` | `TypeBusinessChatLink` | `(self, link: str, message: str, views: int, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, title: Optional[str] = None)` |
| `types` | `TypeBusinessGreetingMessage` | `TypeBusinessGreetingMessage` | `(self, shortcut_id: int, recipients: 'TypeBusinessRecipients', no_activity_days: int)` |
| `types` | `TypeBusinessIntro` | `TypeBusinessIntro` | `(self, title: str, description: str, sticker: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `TypeBusinessLocation` | `TypeBusinessLocation` | `(self, address: str, geo_point: Optional[ForwardRef('TypeGeoPoint')] = None)` |
| `types` | `TypeBusinessRecipients` | `TypeBusinessRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[int]] = None)` |
| `types` | `TypeBusinessWeeklyOpen` | `TypeBusinessWeeklyOpen` | `(self, start_minute: int, end_minute: int)` |
| `types` | `TypeBusinessWorkHours` | `TypeBusinessWorkHours` | `(self, timezone_id: str, weekly_open: List[ForwardRef('TypeBusinessWeeklyOpen')], open_now: Optional[bool] = None)` |
| `types` | `TypeCdnConfig` | `TypeCdnConfig` | `(self, public_keys: List[ForwardRef('TypeCdnPublicKey')])` |
| `types` | `TypeCdnPublicKey` | `TypeCdnPublicKey` | `(self, dc_id: int, public_key: str)` |
| `types` | `TypeChannelAdminLogEvent` | `TypeChannelAdminLogEvent` | `(self, id: int, date: Optional[datetime.datetime], user_id: int, action: 'TypeChannelAdminLogEventAction')` |
| `types` | `TypeChannelAdminLogEventsFilter` | `TypeChannelAdminLogEventsFilter` | `(self, join: Optional[bool] = None, leave: Optional[bool] = None, invite: Optional[bool] = None, ban: Optional[bool] = None, unban: Optional[bool] = None, kick: Optional[bool] = None, unkick: Optional[bool] = None, promote: Optional[bool] = None, demote: Optional[bool] = None, info: Optional[bool] = None, settings: Optional[bool] = None, pinned: Optional[bool] = None, edit: Optional[bool] = None, delete: Optional[bool] = None, group_call: Optional[bool] = None, invites: Optional[bool] = None, send: Optional[bool] = None, forums: Optional[bool] = None, sub_extend: Optional[bool] = None, edit_rank: Optional[bool] = None)` |
| `types` | `TypeChatAdminRights` | `TypeChatAdminRights` | `(self, change_info: Optional[bool] = None, post_messages: Optional[bool] = None, edit_messages: Optional[bool] = None, delete_messages: Optional[bool] = None, ban_users: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, add_admins: Optional[bool] = None, anonymous: Optional[bool] = None, manage_call: Optional[bool] = None, other: Optional[bool] = None, manage_topics: Optional[bool] = None, post_stories: Optional[bool] = None, edit_stories: Optional[bool] = None, delete_stories: Optional[bool] = None, manage_direct_messages: Optional[bool] = None, manage_ranks: Optional[bool] = None)` |
| `types` | `TypeChatAdminWithInvites` | `TypeChatAdminWithInvites` | `(self, admin_id: int, invites_count: int, revoked_invites_count: int)` |
| `types` | `TypeChatBannedRights` | `TypeChatBannedRights` | `(self, until_date: Optional[datetime.datetime], view_messages: Optional[bool] = None, send_messages: Optional[bool] = None, send_media: Optional[bool] = None, send_stickers: Optional[bool] = None, send_gifs: Optional[bool] = None, send_games: Optional[bool] = None, send_inline: Optional[bool] = None, embed_links: Optional[bool] = None, send_polls: Optional[bool] = None, change_info: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, manage_topics: Optional[bool] = None, send_photos: Optional[bool] = None, send_videos: Optional[bool] = None, send_roundvideos: Optional[bool] = None, send_audios: Optional[bool] = None, send_voices: Optional[bool] = None, send_docs: Optional[bool] = None, send_plain: Optional[bool] = None, edit_rank: Optional[bool] = None, send_reactions: Optional[bool] = None)` |
| `types` | `TypeChatInviteImporter` | `TypeChatInviteImporter` | `(self, user_id: int, date: Optional[datetime.datetime], requested: Optional[bool] = None, via_chatlist: Optional[bool] = None, about: Optional[str] = None, approved_by: Optional[int] = None)` |
| `types` | `TypeChatOnlines` | `TypeChatOnlines` | `(self, onlines: int)` |
| `types` | `TypeClient_DH_Inner_Data` | `TypeClient_DH_Inner_Data` | `(self, nonce: int, server_nonce: int, retry_id: int, g_b: bytes)` |
| `types` | `TypeCodeSettings` | `TypeCodeSettings` | `(self, allow_flashcall: Optional[bool] = None, current_number: Optional[bool] = None, allow_app_hash: Optional[bool] = None, allow_missed_call: Optional[bool] = None, allow_firebase: Optional[bool] = None, unknown_number: Optional[bool] = None, logout_tokens: Optional[List[bytes]] = None, token: Optional[str] = None, app_sandbox: Optional[bool] = None)` |
| `types` | `TypeConfig` | `TypeConfig` | `(self, date: Optional[datetime.datetime], expires: Optional[datetime.datetime], test_mode: bool, this_dc: int, dc_options: List[ForwardRef('TypeDcOption')], dc_txt_domain_name: str, chat_size_max: int, megagroup_size_max: int, forwarded_count_max: int, online_update_period_ms: int, offline_blur_timeout_ms: int, offline_idle_timeout_ms: int, online_cloud_timeout_ms: int, notify_cloud_delay_ms: int, notify_default_delay_ms: int, push_chat_period_ms: int, push_chat_limit: int, edit_time_limit: int, revoke_time_limit: int, revoke_pm_time_limit: int, rating_e_decay: int, stickers_recent_limit: int, channels_read_media_period: int, call_receive_timeout_ms: int, call_ring_timeout_ms: int, call_connect_timeout_ms: int, call_packet_timeout_ms: int, me_url_prefix: str, caption_length_max: int, message_length_max: int, webfile_dc_id: int, default_p2p_contacts: Optional[bool] = None, preload_featured_stickers: Optional[bool] = None, revoke_pm_inbox: Optional[bool] = None, blocked_mode: Optional[bool] = None, force_try_ipv6: Optional[bool] = None, tmp_sessions: Optional[int] = None, autoupdate_url_prefix: Optional[str] = None, gif_search_username: Optional[str] = None, venue_search_username: Optional[str] = None, img_search_username: Optional[str] = None, static_maps_provider: Optional[str] = None, suggested_lang_code: Optional[str] = None, lang_pack_version: Optional[int] = None, base_lang_pack_version: Optional[int] = None, reactions_default: Optional[ForwardRef('TypeReaction')] = None, autologin_token: Optional[str] = None)` |
| `types` | `TypeConnectedBot` | `TypeConnectedBot` | `(self, bot_id: int, recipients: 'TypeBusinessBotRecipients', rights: 'TypeBusinessBotRights', device: Optional[str] = None, date: Optional[datetime.datetime] = None, location: Optional[str] = None)` |
| `types` | `TypeConnectedBotStarRef` | `TypeConnectedBotStarRef` | `(self, url: str, date: Optional[datetime.datetime], bot_id: int, commission_permille: int, participants: int, revenue: int, revoked: Optional[bool] = None, duration_months: Optional[int] = None)` |
| `types` | `TypeContact` | `TypeContact` | `(self, user_id: int, mutual: bool)` |
| `types` | `TypeContactBirthday` | `TypeContactBirthday` | `(self, contact_id: int, birthday: 'TypeBirthday')` |
| `types` | `TypeContactStatus` | `TypeContactStatus` | `(self, user_id: int, status: 'TypeUserStatus')` |
| `types` | `TypeDataJSON` | `TypeDataJSON` | `(self, data: str)` |
| `types` | `TypeDcOption` | `TypeDcOption` | `(self, id: int, ip_address: str, port: int, ipv6: Optional[bool] = None, media_only: Optional[bool] = None, tcpo_only: Optional[bool] = None, cdn: Optional[bool] = None, static: Optional[bool] = None, this_port_only: Optional[bool] = None, secret: Optional[bytes] = None)` |
| `types` | `TypeDefaultHistoryTTL` | `TypeDefaultHistoryTTL` | `(self, period: int)` |
| `types` | `TypeDialogFilterSuggested` | `TypeDialogFilterSuggested` | `(self, filter: 'TypeDialogFilter', description: str)` |
| `types` | `TypeDisallowedGiftsSettings` | `TypeDisallowedGiftsSettings` | `(self, disallow_unlimited_stargifts: Optional[bool] = None, disallow_limited_stargifts: Optional[bool] = None, disallow_unique_stargifts: Optional[bool] = None, disallow_premium_gifts: Optional[bool] = None, disallow_stargifts_from_channels: Optional[bool] = None)` |
| `types` | `TypeEmojiKeywordsDifference` | `TypeEmojiKeywordsDifference` | `(self, lang_code: str, from_version: int, version: int, keywords: List[ForwardRef('TypeEmojiKeyword')])` |
| `types` | `TypeEmojiLanguage` | `TypeEmojiLanguage` | `(self, lang_code: str)` |
| `types` | `TypeEmojiURL` | `TypeEmojiURL` | `(self, url: str)` |
| `types` | `TypeExportedChatlistInvite` | `TypeExportedChatlistInvite` | `(self, title: str, url: str, peers: List[ForwardRef('TypePeer')])` |
| `types` | `TypeExportedContactToken` | `TypeExportedContactToken` | `(self, url: str, expires: Optional[datetime.datetime])` |
| `types` | `TypeExportedMessageLink` | `TypeExportedMessageLink` | `(self, link: str, html: str)` |
| `types` | `TypeExportedStoryLink` | `TypeExportedStoryLink` | `(self, link: str)` |
| `types` | `TypeFactCheck` | `TypeFactCheck` | `(self, hash: int, need_check: Optional[bool] = None, country: Optional[str] = None, text: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `TypeFileHash` | `TypeFileHash` | `(self, offset: int, limit: int, hash: bytes)` |
| `types` | `TypeFolder` | `TypeFolder` | `(self, id: int, title: str, autofill_new_broadcasts: Optional[bool] = None, autofill_public_groups: Optional[bool] = None, autofill_new_correspondents: Optional[bool] = None, photo: Optional[ForwardRef('TypeChatPhoto')] = None)` |
| `types` | `TypeFolderPeer` | `TypeFolderPeer` | `(self, peer: 'TypePeer', folder_id: int)` |
| `types` | `TypeFoundStory` | `TypeFoundStory` | `(self, peer: 'TypePeer', story: 'TypeStoryItem')` |
| `types` | `TypeFutureSalt` | `TypeFutureSalt` | `(self, valid_since: Optional[datetime.datetime], valid_until: Optional[datetime.datetime], salt: int)` |
| `types` | `TypeFutureSalts` | `TypeFutureSalts` | `(self, req_msg_id: int, now: int, salts: List[ForwardRef('Typefuture_salt')])` |
| `types` | `TypeGame` | `TypeGame` | `(self, id: int, access_hash: int, short_name: str, title: str, description: str, photo: 'TypePhoto', document: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `TypeGeoPointAddress` | `TypeGeoPointAddress` | `(self, country_iso2: str, state: Optional[str] = None, city: Optional[str] = None, street: Optional[str] = None)` |
| `types` | `TypeGlobalPrivacySettings` | `TypeGlobalPrivacySettings` | `(self, archive_and_mute_new_noncontact_peers: Optional[bool] = None, keep_archived_unmuted: Optional[bool] = None, keep_archived_folders: Optional[bool] = None, hide_read_marks: Optional[bool] = None, new_noncontact_peers_require_premium: Optional[bool] = None, display_gifts_button: Optional[bool] = None, noncontact_peers_paid_stars: Optional[int] = None, disallowed_gifts: Optional[ForwardRef('TypeDisallowedGiftsSettings')] = None)` |
| `types` | `TypeGroupCallDonor` | `TypeGroupCallDonor` | `(self, stars: int, top: Optional[bool] = None, my: Optional[bool] = None, peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `TypeGroupCallMessage` | `TypeGroupCallMessage` | `(self, id: int, from_id: 'TypePeer', date: Optional[datetime.datetime], message: 'TypeTextWithEntities', from_admin: Optional[bool] = None, paid_message_stars: Optional[int] = None)` |
| `types` | `TypeGroupCallParticipant` | `TypeGroupCallParticipant` | `(self, peer: 'TypePeer', date: Optional[datetime.datetime], source: int, muted: Optional[bool] = None, left: Optional[bool] = None, can_self_unmute: Optional[bool] = None, just_joined: Optional[bool] = None, versioned: Optional[bool] = None, min: Optional[bool] = None, muted_by_you: Optional[bool] = None, volume_by_admin: Optional[bool] = None, is_self: Optional[bool] = None, video_joined: Optional[bool] = None, active_date: Optional[datetime.datetime] = None, volume: Optional[int] = None, about: Optional[str] = None, raise_hand_rating: Optional[int] = None, video: Optional[ForwardRef('TypeGroupCallParticipantVideo')] = None, presentation: Optional[ForwardRef('TypeGroupCallParticipantVideo')] = None, paid_stars_total: Optional[int] = None)` |
| `types` | `TypeGroupCallParticipantVideo` | `TypeGroupCallParticipantVideo` | `(self, endpoint: str, source_groups: List[ForwardRef('TypeGroupCallParticipantVideoSourceGroup')], paused: Optional[bool] = None, audio_source: Optional[int] = None)` |
| `types` | `TypeGroupCallParticipantVideoSourceGroup` | `TypeGroupCallParticipantVideoSourceGroup` | `(self, semantics: str, sources: List[int])` |
| `types` | `TypeGroupCallStreamChannel` | `TypeGroupCallStreamChannel` | `(self, channel: int, scale: int, last_timestamp_ms: int)` |
| `types` | `TypeHighScore` | `TypeHighScore` | `(self, pos: int, user_id: int, score: int)` |
| `types` | `TypeHttpWait` | `TypeHttpWait` | `(self, max_delay: int, wait_after: int, max_wait: int)` |
| `types` | `TypeImportedContact` | `TypeImportedContact` | `(self, user_id: int, client_id: int)` |
| `types` | `TypeInlineBotSwitchPM` | `TypeInlineBotSwitchPM` | `(self, text: str, start_param: str)` |
| `types` | `TypeInlineBotWebView` | `TypeInlineBotWebView` | `(self, text: str, url: str)` |
| `types` | `TypeInputAppEvent` | `TypeInputAppEvent` | `(self, time: float, type: str, peer: int, data: 'TypeJSONValue')` |
| `types` | `TypeInputBusinessAwayMessage` | `TypeInputBusinessAwayMessage` | `(self, shortcut_id: int, schedule: 'TypeBusinessAwayMessageSchedule', recipients: 'TypeInputBusinessRecipients', offline_only: Optional[bool] = None)` |
| `types` | `TypeInputBusinessBotRecipients` | `TypeInputBusinessBotRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[ForwardRef('TypeInputUser')]] = None, exclude_users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `types` | `TypeInputBusinessChatLink` | `TypeInputBusinessChatLink` | `(self, message: str, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, title: Optional[str] = None)` |
| `types` | `TypeInputBusinessGreetingMessage` | `TypeInputBusinessGreetingMessage` | `(self, shortcut_id: int, recipients: 'TypeInputBusinessRecipients', no_activity_days: int)` |
| `types` | `TypeInputBusinessIntro` | `TypeInputBusinessIntro` | `(self, title: str, description: str, sticker: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `types` | `TypeInputBusinessRecipients` | `TypeInputBusinessRecipients` | `(self, existing_chats: Optional[bool] = None, new_chats: Optional[bool] = None, contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, exclude_selected: Optional[bool] = None, users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `types` | `TypeInputChatlist` | `TypeInputChatlist` | `(self, filter_id: int)` |
| `types` | `TypeInputClientProxy` | `TypeInputClientProxy` | `(self, address: str, port: int)` |
| `types` | `TypeInputContact` | `TypeInputContact` | `(self, client_id: int, phone: str, first_name: str, last_name: str, note: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `types` | `TypeInputEncryptedChat` | `TypeInputEncryptedChat` | `(self, chat_id: int, access_hash: int)` |
| `types` | `TypeInputFolderPeer` | `TypeInputFolderPeer` | `(self, peer: 'TypeInputPeer', folder_id: int)` |
| `types` | `TypeInputMessageReadMetric` | `TypeInputMessageReadMetric` | `(self, msg_id: int, view_id: int, time_in_view_ms: int, active_time_in_view_ms: int, height_to_viewport_ratio_permille: int, seen_range_ratio_permille: int)` |
| `types` | `TypeInputPeerNotifySettings` | `TypeInputPeerNotifySettings` | `(self, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[datetime.datetime] = None, sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_sound: Optional[ForwardRef('TypeNotificationSound')] = None)` |
| `types` | `TypeInputPhoneCall` | `TypeInputPhoneCall` | `(self, id: int, access_hash: int)` |
| `types` | `TypeInputSecureValue` | `TypeInputSecureValue` | `(self, type: 'TypeSecureValueType', data: Optional[ForwardRef('TypeSecureData')] = None, front_side: Optional[ForwardRef('TypeInputSecureFile')] = None, reverse_side: Optional[ForwardRef('TypeInputSecureFile')] = None, selfie: Optional[ForwardRef('TypeInputSecureFile')] = None, translation: Optional[List[ForwardRef('TypeInputSecureFile')]] = None, files: Optional[List[ForwardRef('TypeInputSecureFile')]] = None, plain_data: Optional[ForwardRef('TypeSecurePlainData')] = None)` |
| `types` | `TypeInputSingleMedia` | `TypeInputSingleMedia` | `(self, media: 'TypeInputMedia', message: str, random_id: int = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None)` |
| `types` | `TypeInputStarsTransaction` | `TypeInputStarsTransaction` | `(self, id: str, refund: Optional[bool] = None)` |
| `types` | `TypeInputStickerSetItem` | `TypeInputStickerSetItem` | `(self, document: 'TypeInputDocument', emoji: str, mask_coords: Optional[ForwardRef('TypeMaskCoords')] = None, keywords: Optional[str] = None)` |
| `types` | `TypeInputThemeSettings` | `TypeInputThemeSettings` | `(self, base_theme: 'TypeBaseTheme', accent_color: int, message_colors_animated: Optional[bool] = None, outbox_accent_color: Optional[int] = None, message_colors: Optional[List[int]] = None, wallpaper: Optional[ForwardRef('TypeInputWallPaper')] = None, wallpaper_settings: Optional[ForwardRef('TypeWallPaperSettings')] = None)` |
| `types` | `TypeInputWebDocument` | `TypeInputWebDocument` | `(self, url: str, size: int, mime_type: str, attributes: List[ForwardRef('TypeDocumentAttribute')])` |
| `types` | `TypeInvoice` | `TypeInvoice` | `(self, currency: str, prices: List[ForwardRef('TypeLabeledPrice')], test: Optional[bool] = None, name_requested: Optional[bool] = None, phone_requested: Optional[bool] = None, email_requested: Optional[bool] = None, shipping_address_requested: Optional[bool] = None, flexible: Optional[bool] = None, phone_to_provider: Optional[bool] = None, email_to_provider: Optional[bool] = None, recurring: Optional[bool] = None, max_tip_amount: Optional[int] = None, suggested_tip_amounts: Optional[List[int]] = None, terms_url: Optional[str] = None, subscription_period: Optional[int] = None)` |
| `types` | `TypeJSONObjectValue` | `TypeJSONObjectValue` | `(self, key: str, value: 'TypeJSONValue')` |
| `types` | `TypeKeyboardButtonRow` | `TypeKeyboardButtonRow` | `(self, buttons: List[ForwardRef('TypeKeyboardButton')])` |
| `types` | `TypeKeyboardButtonStyle` | `TypeKeyboardButtonStyle` | `(self, bg_primary: Optional[bool] = None, bg_danger: Optional[bool] = None, bg_success: Optional[bool] = None, icon: Optional[int] = None)` |
| `types` | `TypeLabeledPrice` | `TypeLabeledPrice` | `(self, label: str, amount: int)` |
| `types` | `TypeLangPackDifference` | `TypeLangPackDifference` | `(self, lang_code: str, from_version: int, version: int, strings: List[ForwardRef('TypeLangPackString')])` |
| `types` | `TypeLangPackLanguage` | `TypeLangPackLanguage` | `(self, name: str, native_name: str, lang_code: str, plural_code: str, strings_count: int, translated_count: int, translations_url: str, official: Optional[bool] = None, rtl: Optional[bool] = None, beta: Optional[bool] = None, base_lang_code: Optional[str] = None)` |
| `types` | `TypeMaskCoords` | `TypeMaskCoords` | `(self, n: int, x: float, y: float, zoom: float)` |
| `types` | `TypeMediaAreaCoordinates` | `TypeMediaAreaCoordinates` | `(self, x: float, y: float, w: float, h: float, rotation: float, radius: Optional[float] = None)` |
| `types` | `TypeMessageFwdHeader` | `TypeMessageFwdHeader` | `(self, date: Optional[datetime.datetime], imported: Optional[bool] = None, saved_out: Optional[bool] = None, from_id: Optional[ForwardRef('TypePeer')] = None, from_name: Optional[str] = None, channel_post: Optional[int] = None, post_author: Optional[str] = None, saved_from_peer: Optional[ForwardRef('TypePeer')] = None, saved_from_msg_id: Optional[int] = None, saved_from_id: Optional[ForwardRef('TypePeer')] = None, saved_from_name: Optional[str] = None, saved_date: Optional[datetime.datetime] = None, psa_type: Optional[str] = None)` |
| `types` | `TypeMessagePeerReaction` | `TypeMessagePeerReaction` | `(self, peer_id: 'TypePeer', date: Optional[datetime.datetime], reaction: 'TypeReaction', big: Optional[bool] = None, unread: Optional[bool] = None, my: Optional[bool] = None)` |
| `types` | `TypeMessageRange` | `TypeMessageRange` | `(self, min_id: int, max_id: int)` |
| `types` | `TypeMessageReactions` | `TypeMessageReactions` | `(self, results: List[ForwardRef('TypeReactionCount')], min: Optional[bool] = None, can_see_list: Optional[bool] = None, reactions_as_tags: Optional[bool] = None, recent_reactions: Optional[List[ForwardRef('TypeMessagePeerReaction')]] = None, top_reactors: Optional[List[ForwardRef('TypeMessageReactor')]] = None)` |
| `types` | `TypeMessageReactor` | `TypeMessageReactor` | `(self, count: int, top: Optional[bool] = None, my: Optional[bool] = None, anonymous: Optional[bool] = None, peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `TypeMessageReplies` | `TypeMessageReplies` | `(self, replies: int, replies_pts: int, comments: Optional[bool] = None, recent_repliers: Optional[List[ForwardRef('TypePeer')]] = None, channel_id: Optional[int] = None, max_id: Optional[int] = None, read_max_id: Optional[int] = None)` |
| `types` | `TypeMessageReportOption` | `TypeMessageReportOption` | `(self, text: str, option: bytes)` |
| `types` | `TypeMessageViews` | `TypeMessageViews` | `(self, views: Optional[int] = None, forwards: Optional[int] = None, replies: Optional[ForwardRef('TypeMessageReplies')] = None)` |
| `types` | `TypeMissingInvitee` | `TypeMissingInvitee` | `(self, user_id: int, premium_would_allow_invite: Optional[bool] = None, premium_required_for_pm: Optional[bool] = None)` |
| `types` | `TypeMsgResendReq` | `TypeMsgResendReq` | `(self, msg_ids: List[int])` |
| `types` | `TypeMsgsAck` | `TypeMsgsAck` | `(self, msg_ids: List[int])` |
| `types` | `TypeMsgsAllInfo` | `TypeMsgsAllInfo` | `(self, msg_ids: List[int], info: str)` |
| `types` | `TypeMsgsStateInfo` | `TypeMsgsStateInfo` | `(self, req_msg_id: int, info: str)` |
| `types` | `TypeMsgsStateReq` | `TypeMsgsStateReq` | `(self, msg_ids: List[int])` |
| `types` | `TypeMyBoost` | `TypeMyBoost` | `(self, slot: int, date: Optional[datetime.datetime], expires: Optional[datetime.datetime], peer: Optional[ForwardRef('TypePeer')] = None, cooldown_until_date: Optional[datetime.datetime] = None)` |
| `types` | `TypeNearestDc` | `TypeNearestDc` | `(self, country: str, this_dc: int, nearest_dc: int)` |
| `types` | `TypeNewSession` | `TypeNewSession` | `(self, first_msg_id: int, unique_id: int, server_salt: int)` |
| `types` | `TypeOutboxReadDate` | `TypeOutboxReadDate` | `(self, date: Optional[datetime.datetime])` |
| `types` | `TypePage` | `TypePage` | `(self, url: str, blocks: List[ForwardRef('TypePageBlock')], photos: List[ForwardRef('TypePhoto')], documents: List[ForwardRef('TypeDocument')], part: Optional[bool] = None, rtl: Optional[bool] = None, v2: Optional[bool] = None, views: Optional[int] = None)` |
| `types` | `TypePageCaption` | `TypePageCaption` | `(self, text: 'TypeRichText', credit: 'TypeRichText')` |
| `types` | `TypePageRelatedArticle` | `TypePageRelatedArticle` | `(self, url: str, webpage_id: int, title: Optional[str] = None, description: Optional[str] = None, photo_id: Optional[int] = None, author: Optional[str] = None, published_date: Optional[datetime.datetime] = None)` |
| `types` | `TypePageTableCell` | `TypePageTableCell` | `(self, header: Optional[bool] = None, align_center: Optional[bool] = None, align_right: Optional[bool] = None, valign_middle: Optional[bool] = None, valign_bottom: Optional[bool] = None, text: Optional[ForwardRef('TypeRichText')] = None, colspan: Optional[int] = None, rowspan: Optional[int] = None)` |
| `types` | `TypePageTableRow` | `TypePageTableRow` | `(self, cells: List[ForwardRef('TypePageTableCell')])` |
| `types` | `TypePasskey` | `TypePasskey` | `(self, id: str, name: str, date: Optional[datetime.datetime], software_emoji_id: Optional[int] = None, last_usage_date: Optional[datetime.datetime] = None)` |
| `types` | `TypePaymentCharge` | `TypePaymentCharge` | `(self, id: str, provider_charge_id: str)` |
| `types` | `TypePaymentFormMethod` | `TypePaymentFormMethod` | `(self, url: str, title: str)` |
| `types` | `TypePaymentRequestedInfo` | `TypePaymentRequestedInfo` | `(self, name: Optional[str] = None, phone: Optional[str] = None, email: Optional[str] = None, shipping_address: Optional[ForwardRef('TypePostAddress')] = None)` |
| `types` | `TypePaymentSavedCredentials` | `TypePaymentSavedCredentials` | `(self, id: str, title: str)` |
| `types` | `TypePeerBlocked` | `TypePeerBlocked` | `(self, peer_id: 'TypePeer', date: Optional[datetime.datetime])` |
| `types` | `TypePeerNotifySettings` | `TypePeerNotifySettings` | `(self, show_previews: Optional[bool] = None, silent: Optional[bool] = None, mute_until: Optional[datetime.datetime] = None, ios_sound: Optional[ForwardRef('TypeNotificationSound')] = None, android_sound: Optional[ForwardRef('TypeNotificationSound')] = None, other_sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_muted: Optional[bool] = None, stories_hide_sender: Optional[bool] = None, stories_ios_sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_android_sound: Optional[ForwardRef('TypeNotificationSound')] = None, stories_other_sound: Optional[ForwardRef('TypeNotificationSound')] = None)` |
| `types` | `TypePeerSettings` | `TypePeerSettings` | `(self, report_spam: Optional[bool] = None, add_contact: Optional[bool] = None, block_contact: Optional[bool] = None, share_contact: Optional[bool] = None, need_contacts_exception: Optional[bool] = None, report_geo: Optional[bool] = None, autoarchived: Optional[bool] = None, invite_members: Optional[bool] = None, request_chat_broadcast: Optional[bool] = None, business_bot_paused: Optional[bool] = None, business_bot_can_reply: Optional[bool] = None, geo_distance: Optional[int] = None, request_chat_title: Optional[str] = None, request_chat_date: Optional[datetime.datetime] = None, business_bot_id: Optional[int] = None, business_bot_manage_url: Optional[str] = None, charge_paid_message_stars: Optional[int] = None, registration_month: Optional[str] = None, phone_country: Optional[str] = None, name_change_date: Optional[datetime.datetime] = None, photo_change_date: Optional[datetime.datetime] = None)` |
| `types` | `TypePeerStories` | `TypePeerStories` | `(self, peer: 'TypePeer', stories: List[ForwardRef('TypeStoryItem')], max_read_id: Optional[int] = None)` |
| `types` | `TypePendingSuggestion` | `TypePendingSuggestion` | `(self, suggestion: str, title: 'TypeTextWithEntities', description: 'TypeTextWithEntities', url: str)` |
| `types` | `TypePhoneCallProtocol` | `TypePhoneCallProtocol` | `(self, min_layer: int, max_layer: int, library_versions: List[str], udp_p2p: Optional[bool] = None, udp_reflector: Optional[bool] = None)` |
| `types` | `TypePoll` | `TypePoll` | `(self, id: int, question: 'TypeTextWithEntities', answers: List[ForwardRef('TypePollAnswer')], hash: int, closed: Optional[bool] = None, public_voters: Optional[bool] = None, multiple_choice: Optional[bool] = None, quiz: Optional[bool] = None, open_answers: Optional[bool] = None, revoting_disabled: Optional[bool] = None, shuffle_answers: Optional[bool] = None, hide_results_until_close: Optional[bool] = None, creator: Optional[bool] = None, subscribers_only: Optional[bool] = None, close_period: Optional[int] = None, close_date: Optional[datetime.datetime] = None, countries_iso2: Optional[List[str]] = None)` |
| `types` | `TypePollAnswerVoters` | `TypePollAnswerVoters` | `(self, option: bytes, chosen: Optional[bool] = None, correct: Optional[bool] = None, voters: Optional[int] = None, recent_voters: Optional[List[ForwardRef('TypePeer')]] = None)` |
| `types` | `TypePollResults` | `TypePollResults` | `(self, min: Optional[bool] = None, has_unread_votes: Optional[bool] = None, can_view_stats: Optional[bool] = None, results: Optional[List[ForwardRef('TypePollAnswerVoters')]] = None, total_voters: Optional[int] = None, recent_voters: Optional[List[ForwardRef('TypePeer')]] = None, solution: Optional[str] = None, solution_entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, solution_media: Optional[ForwardRef('TypeMessageMedia')] = None)` |
| `types` | `TypePong` | `TypePong` | `(self, msg_id: int, ping_id: int)` |
| `types` | `TypePopularContact` | `TypePopularContact` | `(self, client_id: int, importers: int)` |
| `types` | `TypePostAddress` | `TypePostAddress` | `(self, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str, post_code: str)` |
| `types` | `TypePremiumGiftCodeOption` | `TypePremiumGiftCodeOption` | `(self, users: int, months: int, currency: str, amount: int, store_product: Optional[str] = None, store_quantity: Optional[int] = None)` |
| `types` | `TypePremiumSubscriptionOption` | `TypePremiumSubscriptionOption` | `(self, months: int, currency: str, amount: int, bot_url: str, current: Optional[bool] = None, can_purchase_upgrade: Optional[bool] = None, transaction: Optional[str] = None, store_product: Optional[str] = None)` |
| `types` | `TypeQuickReply` | `TypeQuickReply` | `(self, shortcut_id: int, shortcut: str, top_message: int, count: int)` |
| `types` | `TypeReactionCount` | `TypeReactionCount` | `(self, reaction: 'TypeReaction', count: int, chosen_order: Optional[int] = None)` |
| `types` | `TypeReactionsNotifySettings` | `TypeReactionsNotifySettings` | `(self, sound: 'TypeNotificationSound', show_previews: bool, messages_notify_from: Optional[ForwardRef('TypeReactionNotificationsFrom')] = None, stories_notify_from: Optional[ForwardRef('TypeReactionNotificationsFrom')] = None, poll_votes_notify_from: Optional[ForwardRef('TypeReactionNotificationsFrom')] = None)` |
| `types` | `TypeReadParticipantDate` | `TypeReadParticipantDate` | `(self, user_id: int, date: Optional[datetime.datetime])` |
| `types` | `TypeReceivedNotifyMessage` | `TypeReceivedNotifyMessage` | `(self, id: int, flags: int)` |
| `types` | `TypeRecentStory` | `TypeRecentStory` | `(self, live: Optional[bool] = None, max_id: Optional[int] = None)` |
| `types` | `TypeResPQ` | `TypeResPQ` | `(self, nonce: int, server_nonce: int, pq: bytes, server_public_key_fingerprints: List[int])` |
| `types` | `TypeRestrictionReason` | `TypeRestrictionReason` | `(self, platform: str, reason: str, text: str)` |
| `types` | `TypeRichMessage` | `TypeRichMessage` | `(self, blocks: List[ForwardRef('TypePageBlock')], photos: List[ForwardRef('TypePhoto')], documents: List[ForwardRef('TypeDocument')], rtl: Optional[bool] = None, part: Optional[bool] = None)` |
| `types` | `TypeRpcError` | `TypeRpcError` | `(self, error_code: int, error_message: str)` |
| `types` | `TypeSavedContact` | `TypeSavedContact` | `(self, phone: str, first_name: str, last_name: str, date: Optional[datetime.datetime])` |
| `types` | `TypeSavedReactionTag` | `TypeSavedReactionTag` | `(self, reaction: 'TypeReaction', count: int, title: Optional[str] = None)` |
| `types` | `TypeSavedStarGift` | `TypeSavedStarGift` | `(self, date: Optional[datetime.datetime], gift: 'TypeStarGift', name_hidden: Optional[bool] = None, unsaved: Optional[bool] = None, refunded: Optional[bool] = None, can_upgrade: Optional[bool] = None, pinned_to_top: Optional[bool] = None, upgrade_separate: Optional[bool] = None, from_id: Optional[ForwardRef('TypePeer')] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None, msg_id: Optional[int] = None, saved_id: Optional[int] = None, convert_stars: Optional[int] = None, upgrade_stars: Optional[int] = None, can_export_at: Optional[int] = None, transfer_stars: Optional[int] = None, can_transfer_at: Optional[int] = None, can_resell_at: Optional[int] = None, collection_id: Optional[List[int]] = None, prepaid_upgrade_hash: Optional[str] = None, drop_original_details_stars: Optional[int] = None, gift_num: Optional[int] = None, can_craft_at: Optional[int] = None)` |
| `types` | `TypeSearchPostsFlood` | `TypeSearchPostsFlood` | `(self, total_daily: int, remains: int, stars_amount: int, query_is_free: Optional[bool] = None, wait_till: Optional[int] = None)` |
| `types` | `TypeSearchResultsCalendarPeriod` | `TypeSearchResultsCalendarPeriod` | `(self, date: Optional[datetime.datetime], min_msg_id: int, max_msg_id: int, count: int)` |
| `types` | `TypeSearchResultsPosition` | `TypeSearchResultsPosition` | `(self, msg_id: int, date: Optional[datetime.datetime], offset: int)` |
| `types` | `TypeSecureCredentialsEncrypted` | `TypeSecureCredentialsEncrypted` | `(self, data: bytes, hash: bytes, secret: bytes)` |
| `types` | `TypeSecureData` | `TypeSecureData` | `(self, data: bytes, data_hash: bytes, secret: bytes)` |
| `types` | `TypeSecureSecretSettings` | `TypeSecureSecretSettings` | `(self, secure_algo: 'TypeSecurePasswordKdfAlgo', secure_secret: bytes, secure_secret_id: int)` |
| `types` | `TypeSecureValue` | `TypeSecureValue` | `(self, type: 'TypeSecureValueType', hash: bytes, data: Optional[ForwardRef('TypeSecureData')] = None, front_side: Optional[ForwardRef('TypeSecureFile')] = None, reverse_side: Optional[ForwardRef('TypeSecureFile')] = None, selfie: Optional[ForwardRef('TypeSecureFile')] = None, translation: Optional[List[ForwardRef('TypeSecureFile')]] = None, files: Optional[List[ForwardRef('TypeSecureFile')]] = None, plain_data: Optional[ForwardRef('TypeSecurePlainData')] = None)` |
| `types` | `TypeSecureValueHash` | `TypeSecureValueHash` | `(self, type: 'TypeSecureValueType', hash: bytes)` |
| `types` | `TypeSendAsPeer` | `TypeSendAsPeer` | `(self, peer: 'TypePeer', premium_required: Optional[bool] = None)` |
| `types` | `TypeServer_DH_inner_data` | `TypeServer_DH_inner_data` | `(self, nonce: int, server_nonce: int, g: int, dh_prime: bytes, g_a: bytes, server_time: int)` |
| `types` | `TypeShippingOption` | `TypeShippingOption` | `(self, id: str, title: str, prices: List[ForwardRef('TypeLabeledPrice')])` |
| `types` | `TypeSmsJob` | `TypeSmsJob` | `(self, job_id: str, phone_number: str, text: str)` |
| `types` | `TypeSponsoredMessage` | `TypeSponsoredMessage` | `(self, url: str, title: str, message: str, button_text: str, recommended: Optional[bool] = None, can_report: Optional[bool] = None, random_id: bytes = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, photo: Optional[ForwardRef('TypePhoto')] = None, media: Optional[ForwardRef('TypeMessageMedia')] = None, color: Optional[ForwardRef('TypePeerColor')] = None, sponsor_info: Optional[str] = None, additional_info: Optional[str] = None, min_display_duration: Optional[int] = None, max_display_duration: Optional[int] = None)` |
| `types` | `TypeSponsoredMessageReportOption` | `TypeSponsoredMessageReportOption` | `(self, text: str, option: bytes)` |
| `types` | `TypeSponsoredPeer` | `TypeSponsoredPeer` | `(self, peer: 'TypePeer', random_id: bytes = None, sponsor_info: Optional[str] = None, additional_info: Optional[str] = None)` |
| `types` | `TypeStarGiftActiveAuctionState` | `TypeStarGiftActiveAuctionState` | `(self, gift: 'TypeStarGift', state: 'TypeStarGiftAuctionState', user_state: 'TypeStarGiftAuctionUserState')` |
| `types` | `TypeStarGiftAttributeCounter` | `TypeStarGiftAttributeCounter` | `(self, attribute: 'TypeStarGiftAttributeId', count: int)` |
| `types` | `TypeStarGiftAuctionAcquiredGift` | `TypeStarGiftAuctionAcquiredGift` | `(self, peer: 'TypePeer', date: Optional[datetime.datetime], bid_amount: int, round: int, pos: int, name_hidden: Optional[bool] = None, message: Optional[ForwardRef('TypeTextWithEntities')] = None, gift_num: Optional[int] = None)` |
| `types` | `TypeStarGiftAuctionUserState` | `TypeStarGiftAuctionUserState` | `(self, acquired_count: int, returned: Optional[bool] = None, bid_amount: Optional[int] = None, bid_date: Optional[datetime.datetime] = None, min_bid_amount: Optional[int] = None, bid_peer: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `TypeStarGiftBackground` | `TypeStarGiftBackground` | `(self, center_color: int, edge_color: int, text_color: int)` |
| `types` | `TypeStarGiftCollection` | `TypeStarGiftCollection` | `(self, collection_id: int, title: str, gifts_count: int, hash: int, icon: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `TypeStarGiftUpgradePrice` | `TypeStarGiftUpgradePrice` | `(self, date: Optional[datetime.datetime], upgrade_stars: int)` |
| `types` | `TypeStarRefProgram` | `TypeStarRefProgram` | `(self, bot_id: int, commission_permille: int, duration_months: Optional[int] = None, end_date: Optional[datetime.datetime] = None, daily_revenue_per_user: Optional[ForwardRef('TypeStarsAmount')] = None)` |
| `types` | `TypeStarsGiftOption` | `TypeStarsGiftOption` | `(self, stars: int, currency: str, amount: int, extended: Optional[bool] = None, store_product: Optional[str] = None)` |
| `types` | `TypeStarsGiveawayOption` | `TypeStarsGiveawayOption` | `(self, stars: int, yearly_boosts: int, currency: str, amount: int, winners: List[ForwardRef('TypeStarsGiveawayWinnersOption')], extended: Optional[bool] = None, default: Optional[bool] = None, store_product: Optional[str] = None)` |
| `types` | `TypeStarsGiveawayWinnersOption` | `TypeStarsGiveawayWinnersOption` | `(self, users: int, per_user_stars: int, default: Optional[bool] = None)` |
| `types` | `TypeStarsRating` | `TypeStarsRating` | `(self, level: int, current_level_stars: int, stars: int, next_level_stars: Optional[int] = None)` |
| `types` | `TypeStarsRevenueStatus` | `TypeStarsRevenueStatus` | `(self, current_balance: 'TypeStarsAmount', available_balance: 'TypeStarsAmount', overall_revenue: 'TypeStarsAmount', withdrawal_enabled: Optional[bool] = None, next_withdrawal_at: Optional[int] = None)` |
| `types` | `TypeStarsSubscription` | `TypeStarsSubscription` | `(self, id: str, peer: 'TypePeer', until_date: Optional[datetime.datetime], pricing: 'TypeStarsSubscriptionPricing', canceled: Optional[bool] = None, can_refulfill: Optional[bool] = None, missing_balance: Optional[bool] = None, bot_canceled: Optional[bool] = None, chat_invite_hash: Optional[str] = None, title: Optional[str] = None, photo: Optional[ForwardRef('TypeWebDocument')] = None, invoice_slug: Optional[str] = None)` |
| `types` | `TypeStarsSubscriptionPricing` | `TypeStarsSubscriptionPricing` | `(self, period: int, amount: int)` |
| `types` | `TypeStarsTopupOption` | `TypeStarsTopupOption` | `(self, stars: int, currency: str, amount: int, extended: Optional[bool] = None, store_product: Optional[str] = None)` |
| `types` | `TypeStarsTransaction` | `TypeStarsTransaction` | `(self, id: str, amount: 'TypeStarsAmount', date: Optional[datetime.datetime], peer: 'TypeStarsTransactionPeer', refund: Optional[bool] = None, pending: Optional[bool] = None, failed: Optional[bool] = None, gift: Optional[bool] = None, reaction: Optional[bool] = None, stargift_upgrade: Optional[bool] = None, business_transfer: Optional[bool] = None, stargift_resale: Optional[bool] = None, posts_search: Optional[bool] = None, stargift_prepaid_upgrade: Optional[bool] = None, stargift_drop_original_details: Optional[bool] = None, phonegroup_message: Optional[bool] = None, stargift_auction_bid: Optional[bool] = None, offer: Optional[bool] = None, title: Optional[str] = None, description: Optional[str] = None, photo: Optional[ForwardRef('TypeWebDocument')] = None, transaction_date: Optional[datetime.datetime] = None, transaction_url: Optional[str] = None, bot_payload: Optional[bytes] = None, msg_id: Optional[int] = None, extended_media: Optional[List[ForwardRef('TypeMessageMedia')]] = None, subscription_period: Optional[int] = None, giveaway_post_id: Optional[int] = None, stargift: Optional[ForwardRef('TypeStarGift')] = None, floodskip_number: Optional[int] = None, starref_commission_permille: Optional[int] = None, starref_peer: Optional[ForwardRef('TypePeer')] = None, starref_amount: Optional[ForwardRef('TypeStarsAmount')] = None, paid_messages: Optional[int] = None, premium_gift_months: Optional[int] = None, ads_proceeds_from_date: Optional[datetime.datetime] = None, ads_proceeds_to_date: Optional[datetime.datetime] = None)` |
| `types` | `TypeStatsAbsValueAndPrev` | `TypeStatsAbsValueAndPrev` | `(self, current: float, previous: float)` |
| `types` | `TypeStatsDateRangeDays` | `TypeStatsDateRangeDays` | `(self, min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime])` |
| `types` | `TypeStatsGroupTopAdmin` | `TypeStatsGroupTopAdmin` | `(self, user_id: int, deleted: int, kicked: int, banned: int)` |
| `types` | `TypeStatsGroupTopInviter` | `TypeStatsGroupTopInviter` | `(self, user_id: int, invitations: int)` |
| `types` | `TypeStatsGroupTopPoster` | `TypeStatsGroupTopPoster` | `(self, user_id: int, messages: int, avg_chars: int)` |
| `types` | `TypeStatsPercentValue` | `TypeStatsPercentValue` | `(self, part: float, total: float)` |
| `types` | `TypeStatsURL` | `TypeStatsURL` | `(self, url: str)` |
| `types` | `TypeStickerKeyword` | `TypeStickerKeyword` | `(self, document_id: int, keyword: List[str])` |
| `types` | `TypeStickerPack` | `TypeStickerPack` | `(self, emoticon: str, documents: List[int])` |
| `types` | `TypeStickerSet` | `TypeStickerSet` | `(self, id: int, access_hash: int, title: str, short_name: str, count: int, hash: int, archived: Optional[bool] = None, official: Optional[bool] = None, masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, channel_emoji_status: Optional[bool] = None, creator: Optional[bool] = None, installed_date: Optional[datetime.datetime] = None, thumbs: Optional[List[ForwardRef('TypePhotoSize')]] = None, thumb_dc_id: Optional[int] = None, thumb_version: Optional[int] = None, thumb_document_id: Optional[int] = None)` |
| `types` | `TypeStoriesStealthMode` | `TypeStoriesStealthMode` | `(self, active_until_date: Optional[datetime.datetime] = None, cooldown_until_date: Optional[datetime.datetime] = None)` |
| `types` | `TypeStoryAlbum` | `TypeStoryAlbum` | `(self, album_id: int, title: str, icon_photo: Optional[ForwardRef('TypePhoto')] = None, icon_video: Optional[ForwardRef('TypeDocument')] = None)` |
| `types` | `TypeStoryFwdHeader` | `TypeStoryFwdHeader` | `(self, modified: Optional[bool] = None, from_: Optional[ForwardRef('TypePeer')] = None, from_name: Optional[str] = None, story_id: Optional[int] = None)` |
| `types` | `TypeStoryViews` | `TypeStoryViews` | `(self, views_count: int, has_viewers: Optional[bool] = None, forwards_count: Optional[int] = None, reactions: Optional[List[ForwardRef('TypeReactionCount')]] = None, reactions_count: Optional[int] = None, recent_viewers: Optional[List[int]] = None)` |
| `types` | `TypeSuggestedPost` | `TypeSuggestedPost` | `(self, accepted: Optional[bool] = None, rejected: Optional[bool] = None, price: Optional[ForwardRef('TypeStarsAmount')] = None, schedule_date: Optional[datetime.datetime] = None)` |
| `types` | `TypeTextWithEntities` | `TypeTextWithEntities` | `(self, text: str, entities: List[ForwardRef('TypeMessageEntity')])` |
| `types` | `TypeTheme` | `TypeTheme` | `(self, id: int, access_hash: int, slug: str, title: str, creator: Optional[bool] = None, default: Optional[bool] = None, for_chat: Optional[bool] = None, document: Optional[ForwardRef('TypeDocument')] = None, settings: Optional[List[ForwardRef('TypeThemeSettings')]] = None, emoticon: Optional[str] = None, installs_count: Optional[int] = None)` |
| `types` | `TypeThemeSettings` | `TypeThemeSettings` | `(self, base_theme: 'TypeBaseTheme', accent_color: int, message_colors_animated: Optional[bool] = None, outbox_accent_color: Optional[int] = None, message_colors: Optional[List[int]] = None, wallpaper: Optional[ForwardRef('TypeWallPaper')] = None)` |
| `types` | `TypeTimezone` | `TypeTimezone` | `(self, id: str, name: str, utc_offset: int)` |
| `types` | `TypeTlsClientHello` | `TypeTlsClientHello` | `(self, blocks: List[ForwardRef('TypeTlsBlock')])` |
| `types` | `TypeTodoCompletion` | `TypeTodoCompletion` | `(self, id: int, completed_by: 'TypePeer', date: Optional[datetime.datetime])` |
| `types` | `TypeTodoItem` | `TypeTodoItem` | `(self, id: int, title: 'TypeTextWithEntities')` |
| `types` | `TypeTodoList` | `TypeTodoList` | `(self, title: 'TypeTextWithEntities', list: List[ForwardRef('TypeTodoItem')], others_can_append: Optional[bool] = None, others_can_complete: Optional[bool] = None)` |
| `types` | `TypeTopPeer` | `TypeTopPeer` | `(self, peer: 'TypePeer', rating: float)` |
| `types` | `TypeTopPeerCategoryPeers` | `TypeTopPeerCategoryPeers` | `(self, category: 'TypeTopPeerCategory', count: int, peers: List[ForwardRef('TypeTopPeer')])` |
| `types` | `TypeUserFull` | `TypeUserFull` | `(self, id: int, settings: 'TypePeerSettings', notify_settings: 'TypePeerNotifySettings', common_chats_count: int, blocked: Optional[bool] = None, phone_calls_available: Optional[bool] = None, phone_calls_private: Optional[bool] = None, can_pin_message: Optional[bool] = None, has_scheduled: Optional[bool] = None, video_calls_available: Optional[bool] = None, voice_messages_forbidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None, wallpaper_overridden: Optional[bool] = None, contact_require_premium: Optional[bool] = None, read_dates_private: Optional[bool] = None, sponsored_enabled: Optional[bool] = None, can_view_revenue: Optional[bool] = None, bot_can_manage_emoji_status: Optional[bool] = None, display_gifts_button: Optional[bool] = None, noforwards_my_enabled: Optional[bool] = None, noforwards_peer_enabled: Optional[bool] = None, unofficial_security_risk: Optional[bool] = None, about: Optional[str] = None, personal_photo: Optional[ForwardRef('TypePhoto')] = None, profile_photo: Optional[ForwardRef('TypePhoto')] = None, fallback_photo: Optional[ForwardRef('TypePhoto')] = None, bot_info: Optional[ForwardRef('TypeBotInfo')] = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None, theme: Optional[ForwardRef('TypeChatTheme')] = None, private_forward_name: Optional[str] = None, bot_group_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, bot_broadcast_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, wallpaper: Optional[ForwardRef('TypeWallPaper')] = None, stories: Optional[ForwardRef('TypePeerStories')] = None, business_work_hours: Optional[ForwardRef('TypeBusinessWorkHours')] = None, business_location: Optional[ForwardRef('TypeBusinessLocation')] = None, business_greeting_message: Optional[ForwardRef('TypeBusinessGreetingMessage')] = None, business_away_message: Optional[ForwardRef('TypeBusinessAwayMessage')] = None, business_intro: Optional[ForwardRef('TypeBusinessIntro')] = None, birthday: Optional[ForwardRef('TypeBirthday')] = None, personal_channel_id: Optional[int] = None, personal_channel_message: Optional[int] = None, stargifts_count: Optional[int] = None, starref_program: Optional[ForwardRef('TypeStarRefProgram')] = None, bot_verification: Optional[ForwardRef('TypeBotVerification')] = None, send_paid_messages_stars: Optional[int] = None, disallowed_gifts: Optional[ForwardRef('TypeDisallowedGiftsSettings')] = None, stars_rating: Optional[ForwardRef('TypeStarsRating')] = None, stars_my_pending_rating: Optional[ForwardRef('TypeStarsRating')] = None, stars_my_pending_rating_date: Optional[datetime.datetime] = None, main_tab: Optional[ForwardRef('TypeProfileTab')] = None, saved_music: Optional[ForwardRef('TypeDocument')] = None, note: Optional[ForwardRef('TypeTextWithEntities')] = None, bot_manager_id: Optional[int] = None)` |
| `types` | `TypeUsername` | `TypeUsername` | `(self, username: str, editable: Optional[bool] = None, active: Optional[bool] = None)` |
| `types` | `TypeWallPaperSettings` | `TypeWallPaperSettings` | `(self, blur: Optional[bool] = None, motion: Optional[bool] = None, background_color: Optional[int] = None, second_background_color: Optional[int] = None, third_background_color: Optional[int] = None, fourth_background_color: Optional[int] = None, intensity: Optional[int] = None, rotation: Optional[int] = None, emoticon: Optional[str] = None)` |
| `types` | `TypeWebAuthorization` | `TypeWebAuthorization` | `(self, hash: int, bot_id: int, domain: str, browser: str, platform: str, date_created: Optional[datetime.datetime], date_active: Optional[datetime.datetime], ip: str, region: str)` |
| `types` | `TypeWebDomainException` | `TypeWebDomainException` | `(self, domain: str, url: str, title: str, favicon: Optional[int] = None)` |
| `types` | `TypeWebViewMessageSent` | `TypeWebViewMessageSent` | `(self, msg_id: Optional[ForwardRef('TypeInputBotInlineMessageID')] = None)` |
| `types` | `TypeWebViewResult` | `TypeWebViewResult` | `(self, url: str, fullsize: Optional[bool] = None, fullscreen: Optional[bool] = None, same_origin: Optional[bool] = None, query_id: Optional[int] = None)` |
| `types` | `UpdateAiComposeTones` | `UpdateAiComposeTones` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateAttachMenuBots` | `UpdateAttachMenuBots` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateAutoSaveSettings` | `UpdateAutoSaveSettings` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateBotBusinessConnect` | `UpdateBotBusinessConnect` | `(self, connection: 'TypeBotBusinessConnection', qts: int)` |
| `types` | `UpdateBotCallbackQuery` | `UpdateBotCallbackQuery` | `(self, query_id: int, user_id: int, peer: 'TypePeer', msg_id: int, chat_instance: int, data: Optional[bytes] = None, game_short_name: Optional[str] = None)` |
| `types` | `UpdateBotChatBoost` | `UpdateBotChatBoost` | `(self, peer: 'TypePeer', boost: 'TypeBoost', qts: int)` |
| `types` | `UpdateBotChatInviteRequester` | `UpdateBotChatInviteRequester` | `(self, peer: 'TypePeer', date: Optional[datetime.datetime], user_id: int, about: str, invite: 'TypeExportedChatInvite', qts: int, query_id: Optional[int] = None)` |
| `types` | `UpdateBotCommands` | `UpdateBotCommands` | `(self, peer: 'TypePeer', bot_id: int, commands: List[ForwardRef('TypeBotCommand')])` |
| `types` | `UpdateBotDeleteBusinessMessage` | `UpdateBotDeleteBusinessMessage` | `(self, connection_id: str, peer: 'TypePeer', messages: List[int], qts: int)` |
| `types` | `UpdateBotEditBusinessMessage` | `UpdateBotEditBusinessMessage` | `(self, connection_id: str, message: 'TypeMessage', qts: int, reply_to_message: Optional[ForwardRef('TypeMessage')] = None)` |
| `types` | `UpdateBotGuestChatQuery` | `UpdateBotGuestChatQuery` | `(self, query_id: int, message: 'TypeMessage', qts: int, reference_messages: Optional[List[ForwardRef('TypeMessage')]] = None)` |
| `types` | `UpdateBotInlineQuery` | `UpdateBotInlineQuery` | `(self, query_id: int, user_id: int, query: str, offset: str, geo: Optional[ForwardRef('TypeGeoPoint')] = None, peer_type: Optional[ForwardRef('TypeInlineQueryPeerType')] = None)` |
| `types` | `UpdateBotInlineSend` | `UpdateBotInlineSend` | `(self, user_id: int, query: str, id: str, geo: Optional[ForwardRef('TypeGeoPoint')] = None, msg_id: Optional[ForwardRef('TypeInputBotInlineMessageID')] = None)` |
| `types` | `UpdateBotMenuButton` | `UpdateBotMenuButton` | `(self, bot_id: int, button: 'TypeBotMenuButton')` |
| `types` | `UpdateBotMessageReaction` | `UpdateBotMessageReaction` | `(self, peer: 'TypePeer', msg_id: int, date: Optional[datetime.datetime], actor: 'TypePeer', old_reactions: List[ForwardRef('TypeReaction')], new_reactions: List[ForwardRef('TypeReaction')], qts: int)` |
| `types` | `UpdateBotMessageReactions` | `UpdateBotMessageReactions` | `(self, peer: 'TypePeer', msg_id: int, date: Optional[datetime.datetime], reactions: List[ForwardRef('TypeReactionCount')], qts: int)` |
| `types` | `UpdateBotNewBusinessMessage` | `UpdateBotNewBusinessMessage` | `(self, connection_id: str, message: 'TypeMessage', qts: int, reply_to_message: Optional[ForwardRef('TypeMessage')] = None)` |
| `types` | `UpdateBotPrecheckoutQuery` | `UpdateBotPrecheckoutQuery` | `(self, query_id: int, user_id: int, payload: bytes, currency: str, total_amount: int, info: Optional[ForwardRef('TypePaymentRequestedInfo')] = None, shipping_option_id: Optional[str] = None)` |
| `types` | `UpdateBotPurchasedPaidMedia` | `UpdateBotPurchasedPaidMedia` | `(self, user_id: int, payload: str, qts: int)` |
| `types` | `UpdateBotShippingQuery` | `UpdateBotShippingQuery` | `(self, query_id: int, user_id: int, payload: bytes, shipping_address: 'TypePostAddress')` |
| `types` | `UpdateBotStopped` | `UpdateBotStopped` | `(self, user_id: int, date: Optional[datetime.datetime], stopped: bool, qts: int)` |
| `types` | `UpdateBotWebhookJSON` | `UpdateBotWebhookJSON` | `(self, data: 'TypeDataJSON')` |
| `types` | `UpdateBotWebhookJSONQuery` | `UpdateBotWebhookJSONQuery` | `(self, query_id: int, data: 'TypeDataJSON', timeout: int)` |
| `types` | `UpdateBusinessBotCallbackQuery` | `UpdateBusinessBotCallbackQuery` | `(self, query_id: int, user_id: int, connection_id: str, message: 'TypeMessage', chat_instance: int, reply_to_message: Optional[ForwardRef('TypeMessage')] = None, data: Optional[bytes] = None)` |
| `types` | `UpdateChannel` | `UpdateChannel` | `(self, channel_id: int)` |
| `types` | `UpdateChannelAvailableMessages` | `UpdateChannelAvailableMessages` | `(self, channel_id: int, available_min_id: int)` |
| `types` | `UpdateChannelMessageForwards` | `UpdateChannelMessageForwards` | `(self, channel_id: int, id: int, forwards: int)` |
| `types` | `UpdateChannelMessageViews` | `UpdateChannelMessageViews` | `(self, channel_id: int, id: int, views: int)` |
| `types` | `UpdateChannelParticipant` | `UpdateChannelParticipant` | `(self, channel_id: int, date: Optional[datetime.datetime], actor_id: int, user_id: int, qts: int, via_chatlist: Optional[bool] = None, prev_participant: Optional[ForwardRef('TypeChannelParticipant')] = None, new_participant: Optional[ForwardRef('TypeChannelParticipant')] = None, invite: Optional[ForwardRef('TypeExportedChatInvite')] = None)` |
| `types` | `UpdateChannelReadMessagesContents` | `UpdateChannelReadMessagesContents` | `(self, channel_id: int, messages: List[int], top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `UpdateChannelTooLong` | `UpdateChannelTooLong` | `(self, channel_id: int, pts: Optional[int] = None)` |
| `types` | `UpdateChannelUserTyping` | `UpdateChannelUserTyping` | `(self, channel_id: int, from_id: 'TypePeer', action: 'TypeSendMessageAction', top_msg_id: Optional[int] = None)` |
| `types` | `UpdateChannelViewForumAsMessages` | `UpdateChannelViewForumAsMessages` | `(self, channel_id: int, enabled: bool)` |
| `types` | `UpdateChannelWebPage` | `UpdateChannelWebPage` | `(self, channel_id: int, webpage: 'TypeWebPage', pts: int, pts_count: int)` |
| `types` | `UpdateChat` | `UpdateChat` | `(self, chat_id: int)` |
| `types` | `UpdateChatDefaultBannedRights` | `UpdateChatDefaultBannedRights` | `(self, peer: 'TypePeer', default_banned_rights: 'TypeChatBannedRights', version: int)` |
| `types` | `UpdateChatParticipant` | `UpdateChatParticipant` | `(self, chat_id: int, date: Optional[datetime.datetime], actor_id: int, user_id: int, qts: int, prev_participant: Optional[ForwardRef('TypeChatParticipant')] = None, new_participant: Optional[ForwardRef('TypeChatParticipant')] = None, invite: Optional[ForwardRef('TypeExportedChatInvite')] = None)` |
| `types` | `UpdateChatParticipantAdd` | `UpdateChatParticipantAdd` | `(self, chat_id: int, user_id: int, inviter_id: int, date: Optional[datetime.datetime], version: int)` |
| `types` | `UpdateChatParticipantAdmin` | `UpdateChatParticipantAdmin` | `(self, chat_id: int, user_id: int, is_admin: bool, version: int)` |
| `types` | `UpdateChatParticipantDelete` | `UpdateChatParticipantDelete` | `(self, chat_id: int, user_id: int, version: int)` |
| `types` | `UpdateChatParticipantRank` | `UpdateChatParticipantRank` | `(self, chat_id: int, user_id: int, rank: str, version: int)` |
| `types` | `UpdateChatParticipants` | `UpdateChatParticipants` | `(self, participants: 'TypeChatParticipants')` |
| `types` | `UpdateChatUserTyping` | `UpdateChatUserTyping` | `(self, chat_id: int, from_id: 'TypePeer', action: 'TypeSendMessageAction')` |
| `types` | `UpdateConfig` | `UpdateConfig` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateContactsReset` | `UpdateContactsReset` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateDcOptions` | `UpdateDcOptions` | `(self, dc_options: List[ForwardRef('TypeDcOption')])` |
| `types` | `UpdateDeleteChannelMessages` | `UpdateDeleteChannelMessages` | `(self, channel_id: int, messages: List[int], pts: int, pts_count: int)` |
| `types` | `UpdateDeleteGroupCallMessages` | `UpdateDeleteGroupCallMessages` | `(self, call: 'TypeInputGroupCall', messages: List[int])` |
| `types` | `UpdateDeleteMessages` | `UpdateDeleteMessages` | `(self, messages: List[int], pts: int, pts_count: int)` |
| `types` | `UpdateDeleteQuickReply` | `UpdateDeleteQuickReply` | `(self, shortcut_id: int)` |
| `types` | `UpdateDeleteQuickReplyMessages` | `UpdateDeleteQuickReplyMessages` | `(self, shortcut_id: int, messages: List[int])` |
| `types` | `UpdateDeleteScheduledMessages` | `UpdateDeleteScheduledMessages` | `(self, peer: 'TypePeer', messages: List[int], sent_messages: Optional[List[int]] = None)` |
| `types` | `UpdateDialogFilter` | `UpdateDialogFilter` | `(self, id: int, filter: Optional[ForwardRef('TypeDialogFilter')] = None)` |
| `types` | `UpdateDialogFilterOrder` | `UpdateDialogFilterOrder` | `(self, order: List[int])` |
| `types` | `UpdateDialogFilters` | `UpdateDialogFilters` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateDialogPinned` | `UpdateDialogPinned` | `(self, peer: 'TypeDialogPeer', pinned: Optional[bool] = None, folder_id: Optional[int] = None)` |
| `types` | `UpdateDialogUnreadMark` | `UpdateDialogUnreadMark` | `(self, peer: 'TypeDialogPeer', unread: Optional[bool] = None, saved_peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `UpdateDraftMessage` | `UpdateDraftMessage` | `(self, peer: 'TypePeer', draft: 'TypeDraftMessage', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `UpdateEditChannelMessage` | `UpdateEditChannelMessage` | `(self, message: 'TypeMessage', pts: int, pts_count: int)` |
| `types` | `UpdateEditMessage` | `UpdateEditMessage` | `(self, message: 'TypeMessage', pts: int, pts_count: int)` |
| `types` | `UpdateEmojiGameInfo` | `UpdateEmojiGameInfo` | `(self, info: 'TypeEmojiGameInfo')` |
| `types` | `UpdateEncryptedChatTyping` | `UpdateEncryptedChatTyping` | `(self, chat_id: int)` |
| `types` | `UpdateEncryptedMessagesRead` | `UpdateEncryptedMessagesRead` | `(self, chat_id: int, max_date: Optional[datetime.datetime], date: Optional[datetime.datetime])` |
| `types` | `UpdateEncryption` | `UpdateEncryption` | `(self, chat: 'TypeEncryptedChat', date: Optional[datetime.datetime])` |
| `types` | `UpdateFavedStickers` | `UpdateFavedStickers` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateFolderPeers` | `UpdateFolderPeers` | `(self, folder_peers: List[ForwardRef('TypeFolderPeer')], pts: int, pts_count: int)` |
| `types` | `UpdateGeoLiveViewed` | `UpdateGeoLiveViewed` | `(self, peer: 'TypePeer', msg_id: int)` |
| `types` | `UpdateGroupCall` | `UpdateGroupCall` | `(self, call: 'TypeGroupCall', live_story: Optional[bool] = None, peer: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `UpdateGroupCallChainBlocks` | `UpdateGroupCallChainBlocks` | `(self, call: 'TypeInputGroupCall', sub_chain_id: int, blocks: List[bytes], next_offset: int)` |
| `types` | `UpdateGroupCallConnection` | `UpdateGroupCallConnection` | `(self, params: 'TypeDataJSON', presentation: Optional[bool] = None)` |
| `types` | `UpdateGroupCallEncryptedMessage` | `UpdateGroupCallEncryptedMessage` | `(self, call: 'TypeInputGroupCall', from_id: 'TypePeer', encrypted_message: bytes)` |
| `types` | `UpdateGroupCallMessage` | `UpdateGroupCallMessage` | `(self, call: 'TypeInputGroupCall', message: 'TypeGroupCallMessage')` |
| `types` | `UpdateGroupCallParticipants` | `UpdateGroupCallParticipants` | `(self, call: 'TypeInputGroupCall', participants: List[ForwardRef('TypeGroupCallParticipant')], version: int)` |
| `types` | `UpdateInlineBotCallbackQuery` | `UpdateInlineBotCallbackQuery` | `(self, query_id: int, user_id: int, msg_id: 'TypeInputBotInlineMessageID', chat_instance: int, data: Optional[bytes] = None, game_short_name: Optional[str] = None)` |
| `types` | `UpdateJoinChatWebViewDecision` | `UpdateJoinChatWebViewDecision` | `(self, peer: 'TypePeer', query_id: int, result: 'TypeJoinChatBotResult')` |
| `types` | `UpdateLangPack` | `UpdateLangPack` | `(self, difference: 'TypeLangPackDifference')` |
| `types` | `UpdateLangPackTooLong` | `UpdateLangPackTooLong` | `(self, lang_code: str)` |
| `types` | `UpdateLoginToken` | `UpdateLoginToken` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateManagedBot` | `UpdateManagedBot` | `(self, user_id: int, bot_id: int, qts: int)` |
| `types` | `UpdateMessageExtendedMedia` | `UpdateMessageExtendedMedia` | `(self, peer: 'TypePeer', msg_id: int, extended_media: List[ForwardRef('TypeMessageExtendedMedia')])` |
| `types` | `UpdateMessageID` | `UpdateMessageID` | `(self, id: int, random_id: int = None)` |
| `types` | `UpdateMessagePoll` | `UpdateMessagePoll` | `(self, poll_id: int, results: 'TypePollResults', peer: Optional[ForwardRef('TypePeer')] = None, msg_id: Optional[int] = None, top_msg_id: Optional[int] = None, poll: Optional[ForwardRef('TypePoll')] = None)` |
| `types` | `UpdateMessagePollVote` | `UpdateMessagePollVote` | `(self, poll_id: int, peer: 'TypePeer', options: List[bytes], positions: List[int], qts: int)` |
| `types` | `UpdateMessageReactions` | `UpdateMessageReactions` | `(self, peer: 'TypePeer', msg_id: int, reactions: 'TypeMessageReactions', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypePeer')] = None)` |
| `types` | `UpdateMonoForumNoPaidException` | `UpdateMonoForumNoPaidException` | `(self, channel_id: int, saved_peer_id: 'TypePeer', exception: Optional[bool] = None)` |
| `types` | `UpdateMoveStickerSetToTop` | `UpdateMoveStickerSetToTop` | `(self, stickerset: int, masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `types` | `UpdateNewAuthorization` | `UpdateNewAuthorization` | `(self, hash: int, unconfirmed: Optional[bool] = None, date: Optional[datetime.datetime] = None, device: Optional[str] = None, location: Optional[str] = None)` |
| `types` | `UpdateNewBotConnection` | `UpdateNewBotConnection` | `(self, bot_id: int, confirmed: Optional[bool] = None, date: Optional[datetime.datetime] = None, device: Optional[str] = None, location: Optional[str] = None)` |
| `types` | `UpdateNewChannelMessage` | `UpdateNewChannelMessage` | `(self, message: 'TypeMessage', pts: int, pts_count: int)` |
| `types` | `UpdateNewEncryptedMessage` | `UpdateNewEncryptedMessage` | `(self, message: 'TypeEncryptedMessage', qts: int)` |
| `types` | `UpdateNewMessage` | `UpdateNewMessage` | `(self, message: 'TypeMessage', pts: int, pts_count: int)` |
| `types` | `UpdateNewQuickReply` | `UpdateNewQuickReply` | `(self, quick_reply: 'TypeQuickReply')` |
| `types` | `UpdateNewScheduledMessage` | `UpdateNewScheduledMessage` | `(self, message: 'TypeMessage')` |
| `types` | `UpdateNewStickerSet` | `UpdateNewStickerSet` | `(self, stickerset: 'TypeStickerSet')` |
| `types` | `UpdateNewStoryReaction` | `UpdateNewStoryReaction` | `(self, story_id: int, peer: 'TypePeer', reaction: 'TypeReaction')` |
| `types` | `UpdateNotifySettings` | `UpdateNotifySettings` | `(self, peer: 'TypeNotifyPeer', notify_settings: 'TypePeerNotifySettings')` |
| `types` | `UpdatePaidReactionPrivacy` | `UpdatePaidReactionPrivacy` | `(self, private: 'TypePaidReactionPrivacy')` |
| `types` | `UpdatePeerBlocked` | `UpdatePeerBlocked` | `(self, peer_id: 'TypePeer', blocked: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None)` |
| `types` | `UpdatePeerHistoryTTL` | `UpdatePeerHistoryTTL` | `(self, peer: 'TypePeer', ttl_period: Optional[int] = None)` |
| `types` | `UpdatePeerLocated` | `UpdatePeerLocated` | `(self, peers: List[ForwardRef('TypePeerLocated')])` |
| `types` | `UpdatePeerSettings` | `UpdatePeerSettings` | `(self, peer: 'TypePeer', settings: 'TypePeerSettings')` |
| `types` | `UpdatePeerWallpaper` | `UpdatePeerWallpaper` | `(self, peer: 'TypePeer', wallpaper_overridden: Optional[bool] = None, wallpaper: Optional[ForwardRef('TypeWallPaper')] = None)` |
| `types` | `UpdatePendingJoinRequests` | `UpdatePendingJoinRequests` | `(self, peer: 'TypePeer', requests_pending: int, recent_requesters: List[int])` |
| `types` | `UpdatePhoneCall` | `UpdatePhoneCall` | `(self, phone_call: 'TypePhoneCall')` |
| `types` | `UpdatePhoneCallSignalingData` | `UpdatePhoneCallSignalingData` | `(self, phone_call_id: int, data: bytes)` |
| `types` | `UpdatePinnedChannelMessages` | `UpdatePinnedChannelMessages` | `(self, channel_id: int, messages: List[int], pts: int, pts_count: int, pinned: Optional[bool] = None)` |
| `types` | `UpdatePinnedDialogs` | `UpdatePinnedDialogs` | `(self, folder_id: Optional[int] = None, order: Optional[List[ForwardRef('TypeDialogPeer')]] = None)` |
| `types` | `UpdatePinnedForumTopic` | `UpdatePinnedForumTopic` | `(self, peer: 'TypePeer', topic_id: int, pinned: Optional[bool] = None)` |
| `types` | `UpdatePinnedForumTopics` | `UpdatePinnedForumTopics` | `(self, peer: 'TypePeer', order: Optional[List[int]] = None)` |
| `types` | `UpdatePinnedMessages` | `UpdatePinnedMessages` | `(self, peer: 'TypePeer', messages: List[int], pts: int, pts_count: int, pinned: Optional[bool] = None)` |
| `types` | `UpdatePinnedSavedDialogs` | `UpdatePinnedSavedDialogs` | `(self, order: Optional[List[ForwardRef('TypeDialogPeer')]] = None)` |
| `types` | `UpdatePrivacy` | `UpdatePrivacy` | `(self, key: 'TypePrivacyKey', rules: List[ForwardRef('TypePrivacyRule')])` |
| `types` | `UpdatePtsChanged` | `UpdatePtsChanged` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateQuickReplies` | `UpdateQuickReplies` | `(self, quick_replies: List[ForwardRef('TypeQuickReply')])` |
| `types` | `UpdateQuickReplyMessage` | `UpdateQuickReplyMessage` | `(self, message: 'TypeMessage')` |
| `types` | `UpdateReadChannelDiscussionInbox` | `UpdateReadChannelDiscussionInbox` | `(self, channel_id: int, top_msg_id: int, read_max_id: int, broadcast_id: Optional[int] = None, broadcast_post: Optional[int] = None)` |
| `types` | `UpdateReadChannelDiscussionOutbox` | `UpdateReadChannelDiscussionOutbox` | `(self, channel_id: int, top_msg_id: int, read_max_id: int)` |
| `types` | `UpdateReadChannelInbox` | `UpdateReadChannelInbox` | `(self, channel_id: int, max_id: int, still_unread_count: int, pts: int, folder_id: Optional[int] = None)` |
| `types` | `UpdateReadChannelOutbox` | `UpdateReadChannelOutbox` | `(self, channel_id: int, max_id: int)` |
| `types` | `UpdateReadFeaturedEmojiStickers` | `UpdateReadFeaturedEmojiStickers` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateReadFeaturedStickers` | `UpdateReadFeaturedStickers` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateReadHistoryInbox` | `UpdateReadHistoryInbox` | `(self, peer: 'TypePeer', max_id: int, still_unread_count: int, pts: int, pts_count: int, folder_id: Optional[int] = None, top_msg_id: Optional[int] = None)` |
| `types` | `UpdateReadHistoryOutbox` | `UpdateReadHistoryOutbox` | `(self, peer: 'TypePeer', max_id: int, pts: int, pts_count: int)` |
| `types` | `UpdateReadMessagesContents` | `UpdateReadMessagesContents` | `(self, messages: List[int], pts: int, pts_count: int, date: Optional[datetime.datetime] = None)` |
| `types` | `UpdateReadMonoForumInbox` | `UpdateReadMonoForumInbox` | `(self, channel_id: int, saved_peer_id: 'TypePeer', read_max_id: int)` |
| `types` | `UpdateReadMonoForumOutbox` | `UpdateReadMonoForumOutbox` | `(self, channel_id: int, saved_peer_id: 'TypePeer', read_max_id: int)` |
| `types` | `UpdateReadStories` | `UpdateReadStories` | `(self, peer: 'TypePeer', max_id: int)` |
| `types` | `UpdateRecentEmojiStatuses` | `UpdateRecentEmojiStatuses` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateRecentReactions` | `UpdateRecentReactions` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateRecentStickers` | `UpdateRecentStickers` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateSavedDialogPinned` | `UpdateSavedDialogPinned` | `(self, peer: 'TypeDialogPeer', pinned: Optional[bool] = None)` |
| `types` | `UpdateSavedGifs` | `UpdateSavedGifs` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateSavedReactionTags` | `UpdateSavedReactionTags` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateSavedRingtones` | `UpdateSavedRingtones` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateSentPhoneCode` | `UpdateSentPhoneCode` | `(self, sent_code: 'TypeSentCode')` |
| `types` | `UpdateSentStoryReaction` | `UpdateSentStoryReaction` | `(self, peer: 'TypePeer', story_id: int, reaction: 'TypeReaction')` |
| `types` | `UpdateServiceNotification` | `UpdateServiceNotification` | `(self, type: str, message: str, media: 'TypeMessageMedia', entities: List[ForwardRef('TypeMessageEntity')], popup: Optional[bool] = None, invert_media: Optional[bool] = None, inbox_date: Optional[datetime.datetime] = None)` |
| `types` | `UpdateShort` | `UpdateShort` | `(self, update: 'TypeUpdate', date: Optional[datetime.datetime])` |
| `types` | `UpdateShortChatMessage` | `UpdateShortChatMessage` | `(self, id: int, from_id: int, chat_id: int, message: str, pts: int, pts_count: int, date: Optional[datetime.datetime], out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, silent: Optional[bool] = None, fwd_from: Optional[ForwardRef('TypeMessageFwdHeader')] = None, via_bot_id: Optional[int] = None, reply_to: Optional[ForwardRef('TypeMessageReplyHeader')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, ttl_period: Optional[int] = None)` |
| `types` | `UpdateShortMessage` | `UpdateShortMessage` | `(self, id: int, user_id: int, message: str, pts: int, pts_count: int, date: Optional[datetime.datetime], out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, silent: Optional[bool] = None, fwd_from: Optional[ForwardRef('TypeMessageFwdHeader')] = None, via_bot_id: Optional[int] = None, reply_to: Optional[ForwardRef('TypeMessageReplyHeader')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, ttl_period: Optional[int] = None)` |
| `types` | `UpdateShortSentMessage` | `UpdateShortSentMessage` | `(self, id: int, pts: int, pts_count: int, date: Optional[datetime.datetime], out: Optional[bool] = None, media: Optional[ForwardRef('TypeMessageMedia')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, ttl_period: Optional[int] = None)` |
| `types` | `UpdateSmsJob` | `UpdateSmsJob` | `(self, job_id: str)` |
| `types` | `UpdateStarGiftAuctionState` | `UpdateStarGiftAuctionState` | `(self, gift_id: int, state: 'TypeStarGiftAuctionState')` |
| `types` | `UpdateStarGiftAuctionUserState` | `UpdateStarGiftAuctionUserState` | `(self, gift_id: int, user_state: 'TypeStarGiftAuctionUserState')` |
| `types` | `UpdateStarGiftCraftFail` | `UpdateStarGiftCraftFail` | `(self, /, *args, **kwargs)` |
| `types` | `UpdateStarsBalance` | `UpdateStarsBalance` | `(self, balance: 'TypeStarsAmount')` |
| `types` | `UpdateStarsRevenueStatus` | `UpdateStarsRevenueStatus` | `(self, peer: 'TypePeer', status: 'TypeStarsRevenueStatus')` |
| `types` | `UpdateStickerSets` | `UpdateStickerSets` | `(self, masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `types` | `UpdateStickerSetsOrder` | `UpdateStickerSetsOrder` | `(self, order: List[int], masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `types` | `UpdateStoriesStealthMode` | `UpdateStoriesStealthMode` | `(self, stealth_mode: 'TypeStoriesStealthMode')` |
| `types` | `UpdateStory` | `UpdateStory` | `(self, peer: 'TypePeer', story: 'TypeStoryItem')` |
| `types` | `UpdateStoryID` | `UpdateStoryID` | `(self, id: int, random_id: int = None)` |
| `types` | `UpdateTheme` | `UpdateTheme` | `(self, theme: 'TypeTheme')` |
| `types` | `UpdateTranscribedAudio` | `UpdateTranscribedAudio` | `(self, peer: 'TypePeer', msg_id: int, transcription_id: int, text: str, pending: Optional[bool] = None)` |
| `types` | `UpdateUser` | `UpdateUser` | `(self, user_id: int)` |
| `types` | `UpdateUserEmojiStatus` | `UpdateUserEmojiStatus` | `(self, user_id: int, emoji_status: 'TypeEmojiStatus')` |
| `types` | `UpdateUserName` | `UpdateUserName` | `(self, user_id: int, first_name: str, last_name: str, usernames: List[ForwardRef('TypeUsername')])` |
| `types` | `UpdateUserPhone` | `UpdateUserPhone` | `(self, user_id: int, phone: str)` |
| `types` | `UpdateUserStatus` | `UpdateUserStatus` | `(self, user_id: int, status: 'TypeUserStatus')` |
| `types` | `UpdateUserTyping` | `UpdateUserTyping` | `(self, user_id: int, action: 'TypeSendMessageAction', top_msg_id: Optional[int] = None)` |
| `types` | `UpdateWebBrowserException` | `UpdateWebBrowserException` | `(self, exception: 'TypeWebDomainException', delete: Optional[bool] = None, open_external_browser: Optional[bool] = None)` |
| `types` | `UpdateWebBrowserSettings` | `UpdateWebBrowserSettings` | `(self, open_external_browser: Optional[bool] = None, display_close_button: Optional[bool] = None)` |
| `types` | `UpdateWebPage` | `UpdateWebPage` | `(self, webpage: 'TypeWebPage', pts: int, pts_count: int)` |
| `types` | `UpdateWebViewResultSent` | `UpdateWebViewResultSent` | `(self, query_id: int)` |
| `types` | `Updates` | `Updates` | `(self, updates: List[ForwardRef('TypeUpdate')], users: List[ForwardRef('TypeUser')], chats: List[ForwardRef('TypeChat')], date: Optional[datetime.datetime], seq: int)` |
| `types` | `UpdatesCombined` | `UpdatesCombined` | `(self, updates: List[ForwardRef('TypeUpdate')], users: List[ForwardRef('TypeUser')], chats: List[ForwardRef('TypeChat')], date: Optional[datetime.datetime], seq_start: int, seq: int)` |
| `types` | `UpdatesTooLong` | `UpdatesTooLong` | `(self, /, *args, **kwargs)` |
| `types` | `UrlAuthResultAccepted` | `UrlAuthResultAccepted` | `(self, url: Optional[str] = None)` |
| `types` | `UrlAuthResultDefault` | `UrlAuthResultDefault` | `(self, /, *args, **kwargs)` |
| `types` | `UrlAuthResultRequest` | `UrlAuthResultRequest` | `(self, bot: 'TypeUser', domain: str, request_write_access: Optional[bool] = None, request_phone_number: Optional[bool] = None, match_codes_first: Optional[bool] = None, is_app: Optional[bool] = None, browser: Optional[str] = None, platform: Optional[str] = None, ip: Optional[str] = None, region: Optional[str] = None, match_codes: Optional[List[str]] = None, user_id_hint: Optional[int] = None, verified_app_name: Optional[str] = None)` |
| `types` | `User` | `User` | `(self, id: int, is_self: Optional[bool] = None, contact: Optional[bool] = None, mutual_contact: Optional[bool] = None, deleted: Optional[bool] = None, bot: Optional[bool] = None, bot_chat_history: Optional[bool] = None, bot_nochats: Optional[bool] = None, verified: Optional[bool] = None, restricted: Optional[bool] = None, min: Optional[bool] = None, bot_inline_geo: Optional[bool] = None, support: Optional[bool] = None, scam: Optional[bool] = None, apply_min_photo: Optional[bool] = None, fake: Optional[bool] = None, bot_attach_menu: Optional[bool] = None, premium: Optional[bool] = None, attach_menu_enabled: Optional[bool] = None, bot_can_edit: Optional[bool] = None, close_friend: Optional[bool] = None, stories_hidden: Optional[bool] = None, stories_unavailable: Optional[bool] = None, contact_require_premium: Optional[bool] = None, bot_business: Optional[bool] = None, bot_has_main_app: Optional[bool] = None, bot_forum_view: Optional[bool] = None, bot_forum_can_manage_topics: Optional[bool] = None, bot_can_manage_bots: Optional[bool] = None, bot_guestchat: Optional[bool] = None, bot_guard: Optional[bool] = None, access_hash: Optional[int] = None, first_name: Optional[str] = None, last_name: Optional[str] = None, username: Optional[str] = None, phone: Optional[str] = None, photo: Optional[ForwardRef('TypeUserProfilePhoto')] = None, status: Optional[ForwardRef('TypeUserStatus')] = None, bot_info_version: Optional[int] = None, restriction_reason: Optional[List[ForwardRef('TypeRestrictionReason')]] = None, bot_inline_placeholder: Optional[str] = None, lang_code: Optional[str] = None, emoji_status: Optional[ForwardRef('TypeEmojiStatus')] = None, usernames: Optional[List[ForwardRef('TypeUsername')]] = None, stories_max_id: Optional[ForwardRef('TypeRecentStory')] = None, color: Optional[ForwardRef('TypePeerColor')] = None, profile_color: Optional[ForwardRef('TypePeerColor')] = None, bot_active_users: Optional[int] = None, bot_verification_icon: Optional[int] = None, send_paid_messages_stars: Optional[int] = None)` |
| `types` | `UserEmpty` | `UserEmpty` | `(self, id: int)` |
| `types` | `UserFull` | `UserFull` | `(self, id: int, settings: 'TypePeerSettings', notify_settings: 'TypePeerNotifySettings', common_chats_count: int, blocked: Optional[bool] = None, phone_calls_available: Optional[bool] = None, phone_calls_private: Optional[bool] = None, can_pin_message: Optional[bool] = None, has_scheduled: Optional[bool] = None, video_calls_available: Optional[bool] = None, voice_messages_forbidden: Optional[bool] = None, translations_disabled: Optional[bool] = None, stories_pinned_available: Optional[bool] = None, blocked_my_stories_from: Optional[bool] = None, wallpaper_overridden: Optional[bool] = None, contact_require_premium: Optional[bool] = None, read_dates_private: Optional[bool] = None, sponsored_enabled: Optional[bool] = None, can_view_revenue: Optional[bool] = None, bot_can_manage_emoji_status: Optional[bool] = None, display_gifts_button: Optional[bool] = None, noforwards_my_enabled: Optional[bool] = None, noforwards_peer_enabled: Optional[bool] = None, unofficial_security_risk: Optional[bool] = None, about: Optional[str] = None, personal_photo: Optional[ForwardRef('TypePhoto')] = None, profile_photo: Optional[ForwardRef('TypePhoto')] = None, fallback_photo: Optional[ForwardRef('TypePhoto')] = None, bot_info: Optional[ForwardRef('TypeBotInfo')] = None, pinned_msg_id: Optional[int] = None, folder_id: Optional[int] = None, ttl_period: Optional[int] = None, theme: Optional[ForwardRef('TypeChatTheme')] = None, private_forward_name: Optional[str] = None, bot_group_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, bot_broadcast_admin_rights: Optional[ForwardRef('TypeChatAdminRights')] = None, wallpaper: Optional[ForwardRef('TypeWallPaper')] = None, stories: Optional[ForwardRef('TypePeerStories')] = None, business_work_hours: Optional[ForwardRef('TypeBusinessWorkHours')] = None, business_location: Optional[ForwardRef('TypeBusinessLocation')] = None, business_greeting_message: Optional[ForwardRef('TypeBusinessGreetingMessage')] = None, business_away_message: Optional[ForwardRef('TypeBusinessAwayMessage')] = None, business_intro: Optional[ForwardRef('TypeBusinessIntro')] = None, birthday: Optional[ForwardRef('TypeBirthday')] = None, personal_channel_id: Optional[int] = None, personal_channel_message: Optional[int] = None, stargifts_count: Optional[int] = None, starref_program: Optional[ForwardRef('TypeStarRefProgram')] = None, bot_verification: Optional[ForwardRef('TypeBotVerification')] = None, send_paid_messages_stars: Optional[int] = None, disallowed_gifts: Optional[ForwardRef('TypeDisallowedGiftsSettings')] = None, stars_rating: Optional[ForwardRef('TypeStarsRating')] = None, stars_my_pending_rating: Optional[ForwardRef('TypeStarsRating')] = None, stars_my_pending_rating_date: Optional[datetime.datetime] = None, main_tab: Optional[ForwardRef('TypeProfileTab')] = None, saved_music: Optional[ForwardRef('TypeDocument')] = None, note: Optional[ForwardRef('TypeTextWithEntities')] = None, bot_manager_id: Optional[int] = None)` |
| `types` | `UserProfilePhoto` | `UserProfilePhoto` | `(self, photo_id: int, dc_id: int, has_video: Optional[bool] = None, personal: Optional[bool] = None, stripped_thumb: Optional[bytes] = None)` |
| `types` | `UserProfilePhotoEmpty` | `UserProfilePhotoEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `UserStatusEmpty` | `UserStatusEmpty` | `(self, /, *args, **kwargs)` |
| `types` | `UserStatusLastMonth` | `UserStatusLastMonth` | `(self, by_me: Optional[bool] = None)` |
| `types` | `UserStatusLastWeek` | `UserStatusLastWeek` | `(self, by_me: Optional[bool] = None)` |
| `types` | `UserStatusOffline` | `UserStatusOffline` | `(self, was_online: Optional[datetime.datetime])` |
| `types` | `UserStatusOnline` | `UserStatusOnline` | `(self, expires: Optional[datetime.datetime])` |
| `types` | `UserStatusRecently` | `UserStatusRecently` | `(self, by_me: Optional[bool] = None)` |
| `types` | `Username` | `Username` | `(self, username: str, editable: Optional[bool] = None, active: Optional[bool] = None)` |
| `types` | `VideoSize` | `VideoSize` | `(self, type: str, w: int, h: int, size: int, video_start_ts: Optional[float] = None)` |
| `types` | `VideoSizeEmojiMarkup` | `VideoSizeEmojiMarkup` | `(self, emoji_id: int, background_colors: List[int])` |
| `types` | `VideoSizeStickerMarkup` | `VideoSizeStickerMarkup` | `(self, stickerset: 'TypeInputStickerSet', sticker_id: int, background_colors: List[int])` |
| `types` | `WallPaper` | `WallPaper` | `(self, id: int, access_hash: int, slug: str, document: 'TypeDocument', creator: Optional[bool] = None, default: Optional[bool] = None, pattern: Optional[bool] = None, dark: Optional[bool] = None, settings: Optional[ForwardRef('TypeWallPaperSettings')] = None)` |
| `types` | `WallPaperNoFile` | `WallPaperNoFile` | `(self, id: int, default: Optional[bool] = None, dark: Optional[bool] = None, settings: Optional[ForwardRef('TypeWallPaperSettings')] = None)` |
| `types` | `WallPaperSettings` | `WallPaperSettings` | `(self, blur: Optional[bool] = None, motion: Optional[bool] = None, background_color: Optional[int] = None, second_background_color: Optional[int] = None, third_background_color: Optional[int] = None, fourth_background_color: Optional[int] = None, intensity: Optional[int] = None, rotation: Optional[int] = None, emoticon: Optional[str] = None)` |
| `types` | `WebAuthorization` | `WebAuthorization` | `(self, hash: int, bot_id: int, domain: str, browser: str, platform: str, date_created: Optional[datetime.datetime], date_active: Optional[datetime.datetime], ip: str, region: str)` |
| `types` | `WebDocument` | `WebDocument` | `(self, url: str, access_hash: int, size: int, mime_type: str, attributes: List[ForwardRef('TypeDocumentAttribute')])` |
| `types` | `WebDocumentNoProxy` | `WebDocumentNoProxy` | `(self, url: str, size: int, mime_type: str, attributes: List[ForwardRef('TypeDocumentAttribute')])` |
| `types` | `WebDomainException` | `WebDomainException` | `(self, domain: str, url: str, title: str, favicon: Optional[int] = None)` |
| `types` | `WebPage` | `WebPage` | `(self, id: int, url: str, display_url: str, hash: int, has_large_media: Optional[bool] = None, video_cover_photo: Optional[bool] = None, type: Optional[str] = None, site_name: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None, photo: Optional[ForwardRef('TypePhoto')] = None, embed_url: Optional[str] = None, embed_type: Optional[str] = None, embed_width: Optional[int] = None, embed_height: Optional[int] = None, duration: Optional[int] = None, author: Optional[str] = None, document: Optional[ForwardRef('TypeDocument')] = None, cached_page: Optional[ForwardRef('TypePage')] = None, attributes: Optional[List[ForwardRef('TypeWebPageAttribute')]] = None)` |
| `types` | `WebPageAttributeAiComposeTone` | `WebPageAttributeAiComposeTone` | `(self, emoji_id: int)` |
| `types` | `WebPageAttributeStarGiftAuction` | `WebPageAttributeStarGiftAuction` | `(self, gift: 'TypeStarGift', end_date: Optional[datetime.datetime])` |
| `types` | `WebPageAttributeStarGiftCollection` | `WebPageAttributeStarGiftCollection` | `(self, icons: List[ForwardRef('TypeDocument')])` |
| `types` | `WebPageAttributeStickerSet` | `WebPageAttributeStickerSet` | `(self, stickers: List[ForwardRef('TypeDocument')], emojis: Optional[bool] = None, text_color: Optional[bool] = None)` |
| `types` | `WebPageAttributeStory` | `WebPageAttributeStory` | `(self, peer: 'TypePeer', id: int, story: Optional[ForwardRef('TypeStoryItem')] = None)` |
| `types` | `WebPageAttributeTheme` | `WebPageAttributeTheme` | `(self, documents: Optional[List[ForwardRef('TypeDocument')]] = None, settings: Optional[ForwardRef('TypeThemeSettings')] = None)` |
| `types` | `WebPageAttributeUniqueStarGift` | `WebPageAttributeUniqueStarGift` | `(self, gift: 'TypeStarGift')` |
| `types` | `WebPageEmpty` | `WebPageEmpty` | `(self, id: int, url: Optional[str] = None)` |
| `types` | `WebPageNotModified` | `WebPageNotModified` | `(self, cached_page_views: Optional[int] = None)` |
| `types` | `WebPagePending` | `WebPagePending` | `(self, id: int, date: Optional[datetime.datetime], url: Optional[str] = None)` |
| `types` | `WebViewMessageSent` | `WebViewMessageSent` | `(self, msg_id: Optional[ForwardRef('TypeInputBotInlineMessageID')] = None)` |
| `types` | `WebViewResultUrl` | `WebViewResultUrl` | `(self, url: str, fullsize: Optional[bool] = None, fullscreen: Optional[bool] = None, same_origin: Optional[bool] = None, query_id: Optional[int] = None)` |
