# MTProto API Functions

Source: Telethon generated TL schema, version `1.44.0`.

Total functions: `779`.

Use `callable_path` values with `/raw/invoke`, for example:

```json
{"request":"users.GetFullUserRequest","kwargs":{"id":"me"}}
```

## Namespaces

- `account`: 128 functions
- `aicompose`: 7 functions
- `auth`: 26 functions
- `bots`: 38 functions
- `channels`: 58 functions
- `chatlists`: 11 functions
- `contacts`: 28 functions
- `folders`: 1 functions
- `fragment`: 1 functions
- `help`: 25 functions
- `langpack`: 5 functions
- `messages`: 256 functions
- `payments`: 65 functions
- `phone`: 43 functions
- `photos`: 5 functions
- `premium`: 5 functions
- `smsjobs`: 7 functions
- `stats`: 8 functions
- `stickers`: 11 functions
- `stories`: 33 functions
- `updates`: 3 functions
- `upload`: 8 functions
- `users`: 7 functions

## Full List

### `account`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AcceptAuthorizationRequest` | `account.AcceptAuthorizationRequest` | `(self, bot_id: int, scope: str, public_key: str, value_hashes: List[ForwardRef('TypeSecureValueHash')], credentials: 'TypeSecureCredentialsEncrypted')` |
| `CancelPasswordEmailRequest` | `account.CancelPasswordEmailRequest` | `(self, /, *args, **kwargs)` |
| `ChangeAuthorizationSettingsRequest` | `account.ChangeAuthorizationSettingsRequest` | `(self, hash: int, confirmed: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None)` |
| `ChangePhoneRequest` | `account.ChangePhoneRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: str)` |
| `CheckUsernameRequest` | `account.CheckUsernameRequest` | `(self, username: str)` |
| `ClearRecentEmojiStatusesRequest` | `account.ClearRecentEmojiStatusesRequest` | `(self, /, *args, **kwargs)` |
| `ConfirmBotConnectionRequest` | `account.ConfirmBotConnectionRequest` | `(self, bot_id: 'TypeInputUser')` |
| `ConfirmPasswordEmailRequest` | `account.ConfirmPasswordEmailRequest` | `(self, code: str)` |
| `ConfirmPhoneRequest` | `account.ConfirmPhoneRequest` | `(self, phone_code_hash: str, phone_code: str)` |
| `CreateBusinessChatLinkRequest` | `account.CreateBusinessChatLinkRequest` | `(self, link: 'TypeInputBusinessChatLink')` |
| `CreateThemeRequest` | `account.CreateThemeRequest` | `(self, slug: str, title: str, document: Optional[ForwardRef('TypeInputDocument')] = None, settings: Optional[List[ForwardRef('TypeInputThemeSettings')]] = None)` |
| `DeclinePasswordResetRequest` | `account.DeclinePasswordResetRequest` | `(self, /, *args, **kwargs)` |
| `DeleteAccountRequest` | `account.DeleteAccountRequest` | `(self, reason: str, password: Optional[ForwardRef('TypeInputCheckPasswordSRP')] = None)` |
| `DeleteAutoSaveExceptionsRequest` | `account.DeleteAutoSaveExceptionsRequest` | `(self, /, *args, **kwargs)` |
| `DeleteBusinessChatLinkRequest` | `account.DeleteBusinessChatLinkRequest` | `(self, slug: str)` |
| `DeletePasskeyRequest` | `account.DeletePasskeyRequest` | `(self, id: str)` |
| `DeleteSecureValueRequest` | `account.DeleteSecureValueRequest` | `(self, types: List[ForwardRef('TypeSecureValueType')])` |
| `DeleteWebBrowserSettingsExceptionsRequest` | `account.DeleteWebBrowserSettingsExceptionsRequest` | `(self, /, *args, **kwargs)` |
| `DisablePeerConnectedBotRequest` | `account.DisablePeerConnectedBotRequest` | `(self, peer: 'TypeInputPeer')` |
| `EditBusinessChatLinkRequest` | `account.EditBusinessChatLinkRequest` | `(self, slug: str, link: 'TypeInputBusinessChatLink')` |
| `FinishTakeoutSessionRequest` | `account.FinishTakeoutSessionRequest` | `(self, success: Optional[bool] = None)` |
| `GetAccountTTLRequest` | `account.GetAccountTTLRequest` | `(self, /, *args, **kwargs)` |
| `GetAllSecureValuesRequest` | `account.GetAllSecureValuesRequest` | `(self, /, *args, **kwargs)` |
| `GetAuthorizationFormRequest` | `account.GetAuthorizationFormRequest` | `(self, bot_id: int, scope: str, public_key: str)` |
| `GetAuthorizationsRequest` | `account.GetAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `GetAutoDownloadSettingsRequest` | `account.GetAutoDownloadSettingsRequest` | `(self, /, *args, **kwargs)` |
| `GetAutoSaveSettingsRequest` | `account.GetAutoSaveSettingsRequest` | `(self, /, *args, **kwargs)` |
| `GetBotBusinessConnectionRequest` | `account.GetBotBusinessConnectionRequest` | `(self, connection_id: str)` |
| `GetBusinessChatLinksRequest` | `account.GetBusinessChatLinksRequest` | `(self, /, *args, **kwargs)` |
| `GetChannelDefaultEmojiStatusesRequest` | `account.GetChannelDefaultEmojiStatusesRequest` | `(self, hash: int)` |
| `GetChannelRestrictedStatusEmojisRequest` | `account.GetChannelRestrictedStatusEmojisRequest` | `(self, hash: int)` |
| `GetChatThemesRequest` | `account.GetChatThemesRequest` | `(self, hash: int)` |
| `GetCollectibleEmojiStatusesRequest` | `account.GetCollectibleEmojiStatusesRequest` | `(self, hash: int)` |
| `GetConnectedBotsRequest` | `account.GetConnectedBotsRequest` | `(self, /, *args, **kwargs)` |
| `GetContactSignUpNotificationRequest` | `account.GetContactSignUpNotificationRequest` | `(self, /, *args, **kwargs)` |
| `GetContentSettingsRequest` | `account.GetContentSettingsRequest` | `(self, /, *args, **kwargs)` |
| `GetDefaultBackgroundEmojisRequest` | `account.GetDefaultBackgroundEmojisRequest` | `(self, hash: int)` |
| `GetDefaultEmojiStatusesRequest` | `account.GetDefaultEmojiStatusesRequest` | `(self, hash: int)` |
| `GetDefaultGroupPhotoEmojisRequest` | `account.GetDefaultGroupPhotoEmojisRequest` | `(self, hash: int)` |
| `GetDefaultProfilePhotoEmojisRequest` | `account.GetDefaultProfilePhotoEmojisRequest` | `(self, hash: int)` |
| `GetGlobalPrivacySettingsRequest` | `account.GetGlobalPrivacySettingsRequest` | `(self, /, *args, **kwargs)` |
| `GetMultiWallPapersRequest` | `account.GetMultiWallPapersRequest` | `(self, wallpapers: List[ForwardRef('TypeInputWallPaper')])` |
| `GetNotifyExceptionsRequest` | `account.GetNotifyExceptionsRequest` | `(self, compare_sound: Optional[bool] = None, compare_stories: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputNotifyPeer')] = None)` |
| `GetNotifySettingsRequest` | `account.GetNotifySettingsRequest` | `(self, peer: 'TypeInputNotifyPeer')` |
| `GetPaidMessagesRevenueRequest` | `account.GetPaidMessagesRevenueRequest` | `(self, user_id: 'TypeInputUser', parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetPasskeysRequest` | `account.GetPasskeysRequest` | `(self, /, *args, **kwargs)` |
| `GetPasswordRequest` | `account.GetPasswordRequest` | `(self, /, *args, **kwargs)` |
| `GetPasswordSettingsRequest` | `account.GetPasswordSettingsRequest` | `(self, password: 'TypeInputCheckPasswordSRP')` |
| `GetPrivacyRequest` | `account.GetPrivacyRequest` | `(self, key: 'TypeInputPrivacyKey')` |
| `GetReactionsNotifySettingsRequest` | `account.GetReactionsNotifySettingsRequest` | `(self, /, *args, **kwargs)` |
| `GetRecentEmojiStatusesRequest` | `account.GetRecentEmojiStatusesRequest` | `(self, hash: int)` |
| `GetSavedMusicIdsRequest` | `account.GetSavedMusicIdsRequest` | `(self, hash: int)` |
| `GetSavedRingtonesRequest` | `account.GetSavedRingtonesRequest` | `(self, hash: int)` |
| `GetSecureValueRequest` | `account.GetSecureValueRequest` | `(self, types: List[ForwardRef('TypeSecureValueType')])` |
| `GetThemeRequest` | `account.GetThemeRequest` | `(self, format: str, theme: 'TypeInputTheme')` |
| `GetThemesRequest` | `account.GetThemesRequest` | `(self, format: str, hash: int)` |
| `GetTmpPasswordRequest` | `account.GetTmpPasswordRequest` | `(self, password: 'TypeInputCheckPasswordSRP', period: int)` |
| `GetUniqueGiftChatThemesRequest` | `account.GetUniqueGiftChatThemesRequest` | `(self, offset: str, limit: int, hash: int)` |
| `GetWallPaperRequest` | `account.GetWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper')` |
| `GetWallPapersRequest` | `account.GetWallPapersRequest` | `(self, hash: int)` |
| `GetWebAuthorizationsRequest` | `account.GetWebAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `GetWebBrowserSettingsRequest` | `account.GetWebBrowserSettingsRequest` | `(self, hash: int)` |
| `InitPasskeyRegistrationRequest` | `account.InitPasskeyRegistrationRequest` | `(self, /, *args, **kwargs)` |
| `InitTakeoutSessionRequest` | `account.InitTakeoutSessionRequest` | `(self, contacts: Optional[bool] = None, message_users: Optional[bool] = None, message_chats: Optional[bool] = None, message_megagroups: Optional[bool] = None, message_channels: Optional[bool] = None, files: Optional[bool] = None, file_max_size: Optional[int] = None)` |
| `InstallThemeRequest` | `account.InstallThemeRequest` | `(self, dark: Optional[bool] = None, theme: Optional[ForwardRef('TypeInputTheme')] = None, format: Optional[str] = None, base_theme: Optional[ForwardRef('TypeBaseTheme')] = None)` |
| `InstallWallPaperRequest` | `account.InstallWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper', settings: 'TypeWallPaperSettings')` |
| `InvalidateSignInCodesRequest` | `account.InvalidateSignInCodesRequest` | `(self, codes: List[str])` |
| `RegisterDeviceRequest` | `account.RegisterDeviceRequest` | `(self, token_type: int, token: str, app_sandbox: bool, secret: bytes, other_uids: List[int], no_muted: Optional[bool] = None)` |
| `RegisterPasskeyRequest` | `account.RegisterPasskeyRequest` | `(self, credential: 'TypeInputPasskeyCredential')` |
| `ReorderUsernamesRequest` | `account.ReorderUsernamesRequest` | `(self, order: List[str])` |
| `ReportPeerRequest` | `account.ReportPeerRequest` | `(self, peer: 'TypeInputPeer', reason: 'TypeReportReason', message: str)` |
| `ReportProfilePhotoRequest` | `account.ReportProfilePhotoRequest` | `(self, peer: 'TypeInputPeer', photo_id: 'TypeInputPhoto', reason: 'TypeReportReason', message: str)` |
| `ResendPasswordEmailRequest` | `account.ResendPasswordEmailRequest` | `(self, /, *args, **kwargs)` |
| `ResetAuthorizationRequest` | `account.ResetAuthorizationRequest` | `(self, hash: int)` |
| `ResetNotifySettingsRequest` | `account.ResetNotifySettingsRequest` | `(self, /, *args, **kwargs)` |
| `ResetPasswordRequest` | `account.ResetPasswordRequest` | `(self, /, *args, **kwargs)` |
| `ResetWallPapersRequest` | `account.ResetWallPapersRequest` | `(self, /, *args, **kwargs)` |
| `ResetWebAuthorizationRequest` | `account.ResetWebAuthorizationRequest` | `(self, hash: int)` |
| `ResetWebAuthorizationsRequest` | `account.ResetWebAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `ResolveBusinessChatLinkRequest` | `account.ResolveBusinessChatLinkRequest` | `(self, slug: str)` |
| `SaveAutoDownloadSettingsRequest` | `account.SaveAutoDownloadSettingsRequest` | `(self, settings: 'TypeAutoDownloadSettings', low: Optional[bool] = None, high: Optional[bool] = None)` |
| `SaveAutoSaveSettingsRequest` | `account.SaveAutoSaveSettingsRequest` | `(self, settings: 'TypeAutoSaveSettings', users: Optional[bool] = None, chats: Optional[bool] = None, broadcasts: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `SaveMusicRequest` | `account.SaveMusicRequest` | `(self, id: 'TypeInputDocument', unsave: Optional[bool] = None, after_id: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `SaveRingtoneRequest` | `account.SaveRingtoneRequest` | `(self, id: 'TypeInputDocument', unsave: bool)` |
| `SaveSecureValueRequest` | `account.SaveSecureValueRequest` | `(self, value: 'TypeInputSecureValue', secure_secret_id: int)` |
| `SaveThemeRequest` | `account.SaveThemeRequest` | `(self, theme: 'TypeInputTheme', unsave: bool)` |
| `SaveWallPaperRequest` | `account.SaveWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper', unsave: bool, settings: 'TypeWallPaperSettings')` |
| `SendChangePhoneCodeRequest` | `account.SendChangePhoneCodeRequest` | `(self, phone_number: str, settings: 'TypeCodeSettings')` |
| `SendConfirmPhoneCodeRequest` | `account.SendConfirmPhoneCodeRequest` | `(self, hash: str, settings: 'TypeCodeSettings')` |
| `SendVerifyEmailCodeRequest` | `account.SendVerifyEmailCodeRequest` | `(self, purpose: 'TypeEmailVerifyPurpose', email: str)` |
| `SendVerifyPhoneCodeRequest` | `account.SendVerifyPhoneCodeRequest` | `(self, phone_number: str, settings: 'TypeCodeSettings')` |
| `SetAccountTTLRequest` | `account.SetAccountTTLRequest` | `(self, ttl: 'TypeAccountDaysTTL')` |
| `SetAuthorizationTTLRequest` | `account.SetAuthorizationTTLRequest` | `(self, authorization_ttl_days: int)` |
| `SetContactSignUpNotificationRequest` | `account.SetContactSignUpNotificationRequest` | `(self, silent: bool)` |
| `SetContentSettingsRequest` | `account.SetContentSettingsRequest` | `(self, sensitive_enabled: Optional[bool] = None)` |
| `SetGlobalPrivacySettingsRequest` | `account.SetGlobalPrivacySettingsRequest` | `(self, settings: 'TypeGlobalPrivacySettings')` |
| `SetMainProfileTabRequest` | `account.SetMainProfileTabRequest` | `(self, tab: 'TypeProfileTab')` |
| `SetPrivacyRequest` | `account.SetPrivacyRequest` | `(self, key: 'TypeInputPrivacyKey', rules: List[ForwardRef('TypeInputPrivacyRule')])` |
| `SetReactionsNotifySettingsRequest` | `account.SetReactionsNotifySettingsRequest` | `(self, settings: 'TypeReactionsNotifySettings')` |
| `ToggleConnectedBotPausedRequest` | `account.ToggleConnectedBotPausedRequest` | `(self, peer: 'TypeInputPeer', paused: bool)` |
| `ToggleNoPaidMessagesExceptionRequest` | `account.ToggleNoPaidMessagesExceptionRequest` | `(self, user_id: 'TypeInputUser', refund_charged: Optional[bool] = None, require_payment: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `ToggleSponsoredMessagesRequest` | `account.ToggleSponsoredMessagesRequest` | `(self, enabled: bool)` |
| `ToggleUsernameRequest` | `account.ToggleUsernameRequest` | `(self, username: str, active: bool)` |
| `ToggleWebBrowserSettingsExceptionRequest` | `account.ToggleWebBrowserSettingsExceptionRequest` | `(self, url: str, delete: Optional[bool] = None, open_external_browser: Optional[bool] = None)` |
| `UnregisterDeviceRequest` | `account.UnregisterDeviceRequest` | `(self, token_type: int, token: str, other_uids: List[int])` |
| `UpdateBirthdayRequest` | `account.UpdateBirthdayRequest` | `(self, birthday: Optional[ForwardRef('TypeBirthday')] = None)` |
| `UpdateBusinessAwayMessageRequest` | `account.UpdateBusinessAwayMessageRequest` | `(self, message: Optional[ForwardRef('TypeInputBusinessAwayMessage')] = None)` |
| `UpdateBusinessGreetingMessageRequest` | `account.UpdateBusinessGreetingMessageRequest` | `(self, message: Optional[ForwardRef('TypeInputBusinessGreetingMessage')] = None)` |
| `UpdateBusinessIntroRequest` | `account.UpdateBusinessIntroRequest` | `(self, intro: Optional[ForwardRef('TypeInputBusinessIntro')] = None)` |
| `UpdateBusinessLocationRequest` | `account.UpdateBusinessLocationRequest` | `(self, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None, address: Optional[str] = None)` |
| `UpdateBusinessWorkHoursRequest` | `account.UpdateBusinessWorkHoursRequest` | `(self, business_work_hours: Optional[ForwardRef('TypeBusinessWorkHours')] = None)` |
| `UpdateColorRequest` | `account.UpdateColorRequest` | `(self, for_profile: Optional[bool] = None, color: Optional[ForwardRef('TypePeerColor')] = None)` |
| `UpdateConnectedBotRequest` | `account.UpdateConnectedBotRequest` | `(self, bot: 'TypeInputUser', recipients: 'TypeInputBusinessBotRecipients', deleted: Optional[bool] = None, rights: Optional[ForwardRef('TypeBusinessBotRights')] = None)` |
| `UpdateDeviceLockedRequest` | `account.UpdateDeviceLockedRequest` | `(self, period: int)` |
| `UpdateEmojiStatusRequest` | `account.UpdateEmojiStatusRequest` | `(self, emoji_status: 'TypeEmojiStatus')` |
| `UpdateNotifySettingsRequest` | `account.UpdateNotifySettingsRequest` | `(self, peer: 'TypeInputNotifyPeer', settings: 'TypeInputPeerNotifySettings')` |
| `UpdatePasswordSettingsRequest` | `account.UpdatePasswordSettingsRequest` | `(self, password: 'TypeInputCheckPasswordSRP', new_settings: 'TypePasswordInputSettings')` |
| `UpdatePersonalChannelRequest` | `account.UpdatePersonalChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `UpdateProfileRequest` | `account.UpdateProfileRequest` | `(self, first_name: Optional[str] = None, last_name: Optional[str] = None, about: Optional[str] = None)` |
| `UpdateStatusRequest` | `account.UpdateStatusRequest` | `(self, offline: bool)` |
| `UpdateThemeRequest` | `account.UpdateThemeRequest` | `(self, format: str, theme: 'TypeInputTheme', slug: Optional[str] = None, title: Optional[str] = None, document: Optional[ForwardRef('TypeInputDocument')] = None, settings: Optional[List[ForwardRef('TypeInputThemeSettings')]] = None)` |
| `UpdateUsernameRequest` | `account.UpdateUsernameRequest` | `(self, username: str)` |
| `UpdateWebBrowserSettingsRequest` | `account.UpdateWebBrowserSettingsRequest` | `(self, open_external_browser: Optional[bool] = None, display_close_button: Optional[bool] = None)` |
| `UploadRingtoneRequest` | `account.UploadRingtoneRequest` | `(self, file: 'TypeInputFile', file_name: str, mime_type: str)` |
| `UploadThemeRequest` | `account.UploadThemeRequest` | `(self, file: 'TypeInputFile', file_name: str, mime_type: str, thumb: Optional[ForwardRef('TypeInputFile')] = None)` |
| `UploadWallPaperRequest` | `account.UploadWallPaperRequest` | `(self, file: 'TypeInputFile', mime_type: str, settings: 'TypeWallPaperSettings', for_chat: Optional[bool] = None)` |
| `VerifyEmailRequest` | `account.VerifyEmailRequest` | `(self, purpose: 'TypeEmailVerifyPurpose', verification: 'TypeEmailVerification')` |
| `VerifyPhoneRequest` | `account.VerifyPhoneRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: str)` |

### `aicompose`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `CreateToneRequest` | `aicompose.CreateToneRequest` | `(self, emoji_id: int, title: str, prompt: str, display_author: Optional[bool] = None)` |
| `DeleteToneRequest` | `aicompose.DeleteToneRequest` | `(self, tone: 'TypeInputAiComposeTone')` |
| `GetToneExampleRequest` | `aicompose.GetToneExampleRequest` | `(self, tone: 'TypeInputAiComposeTone', num: int)` |
| `GetToneRequest` | `aicompose.GetToneRequest` | `(self, tone: 'TypeInputAiComposeTone')` |
| `GetTonesRequest` | `aicompose.GetTonesRequest` | `(self, hash: int)` |
| `SaveToneRequest` | `aicompose.SaveToneRequest` | `(self, tone: 'TypeInputAiComposeTone', unsave: bool)` |
| `UpdateToneRequest` | `aicompose.UpdateToneRequest` | `(self, tone: 'TypeInputAiComposeTone', display_author: Optional[bool] = None, emoji_id: Optional[int] = None, title: Optional[str] = None, prompt: Optional[str] = None)` |

### `auth`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AcceptLoginTokenRequest` | `auth.AcceptLoginTokenRequest` | `(self, token: bytes)` |
| `BindTempAuthKeyRequest` | `auth.BindTempAuthKeyRequest` | `(self, perm_auth_key_id: int, nonce: int, expires_at: Optional[datetime.datetime], encrypted_message: bytes)` |
| `CancelCodeRequest` | `auth.CancelCodeRequest` | `(self, phone_number: str, phone_code_hash: str)` |
| `CheckPaidAuthRequest` | `auth.CheckPaidAuthRequest` | `(self, phone_number: str, phone_code_hash: str, form_id: int)` |
| `CheckPasswordRequest` | `auth.CheckPasswordRequest` | `(self, password: 'TypeInputCheckPasswordSRP')` |
| `CheckRecoveryPasswordRequest` | `auth.CheckRecoveryPasswordRequest` | `(self, code: str)` |
| `DropTempAuthKeysRequest` | `auth.DropTempAuthKeysRequest` | `(self, except_auth_keys: List[int])` |
| `ExportAuthorizationRequest` | `auth.ExportAuthorizationRequest` | `(self, dc_id: int)` |
| `ExportLoginTokenRequest` | `auth.ExportLoginTokenRequest` | `(self, api_id: int, api_hash: str, except_ids: List[int])` |
| `FinishPasskeyLoginRequest` | `auth.FinishPasskeyLoginRequest` | `(self, credential: 'TypeInputPasskeyCredential', from_dc_id: Optional[int] = None, from_auth_key_id: Optional[int] = None)` |
| `ImportAuthorizationRequest` | `auth.ImportAuthorizationRequest` | `(self, id: int, bytes: bytes)` |
| `ImportBotAuthorizationRequest` | `auth.ImportBotAuthorizationRequest` | `(self, flags: int, api_id: int, api_hash: str, bot_auth_token: str)` |
| `ImportLoginTokenRequest` | `auth.ImportLoginTokenRequest` | `(self, token: bytes)` |
| `ImportWebTokenAuthorizationRequest` | `auth.ImportWebTokenAuthorizationRequest` | `(self, api_id: int, api_hash: str, web_auth_token: str)` |
| `InitPasskeyLoginRequest` | `auth.InitPasskeyLoginRequest` | `(self, api_id: int, api_hash: str)` |
| `LogOutRequest` | `auth.LogOutRequest` | `(self, /, *args, **kwargs)` |
| `RecoverPasswordRequest` | `auth.RecoverPasswordRequest` | `(self, code: str, new_settings: Optional[ForwardRef('TypePasswordInputSettings')] = None)` |
| `ReportMissingCodeRequest` | `auth.ReportMissingCodeRequest` | `(self, phone_number: str, phone_code_hash: str, mnc: str)` |
| `RequestFirebaseSmsRequest` | `auth.RequestFirebaseSmsRequest` | `(self, phone_number: str, phone_code_hash: str, safety_net_token: Optional[str] = None, play_integrity_token: Optional[str] = None, ios_push_secret: Optional[str] = None)` |
| `RequestPasswordRecoveryRequest` | `auth.RequestPasswordRecoveryRequest` | `(self, /, *args, **kwargs)` |
| `ResendCodeRequest` | `auth.ResendCodeRequest` | `(self, phone_number: str, phone_code_hash: str, reason: Optional[str] = None)` |
| `ResetAuthorizationsRequest` | `auth.ResetAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `ResetLoginEmailRequest` | `auth.ResetLoginEmailRequest` | `(self, phone_number: str, phone_code_hash: str)` |
| `SendCodeRequest` | `auth.SendCodeRequest` | `(self, phone_number: str, api_id: int, api_hash: str, settings: 'TypeCodeSettings')` |
| `SignInRequest` | `auth.SignInRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: Optional[str] = None, email_verification: Optional[ForwardRef('TypeEmailVerification')] = None)` |
| `SignUpRequest` | `auth.SignUpRequest` | `(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str, no_joined_notifications: Optional[bool] = None)` |

### `bots`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AddPreviewMediaRequest` | `bots.AddPreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia')` |
| `AllowSendMessageRequest` | `bots.AllowSendMessageRequest` | `(self, bot: 'TypeInputUser')` |
| `AnswerWebhookJSONQueryRequest` | `bots.AnswerWebhookJSONQueryRequest` | `(self, query_id: int, data: 'TypeDataJSON')` |
| `CanSendMessageRequest` | `bots.CanSendMessageRequest` | `(self, bot: 'TypeInputUser')` |
| `CheckDownloadFileParamsRequest` | `bots.CheckDownloadFileParamsRequest` | `(self, bot: 'TypeInputUser', file_name: str, url: str)` |
| `CheckUsernameRequest` | `bots.CheckUsernameRequest` | `(self, username: str)` |
| `CreateBotRequest` | `bots.CreateBotRequest` | `(self, name: str, username: str, manager_id: 'TypeInputUser', via_deeplink: Optional[bool] = None)` |
| `DeletePreviewMediaRequest` | `bots.DeletePreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: List[ForwardRef('TypeInputMedia')])` |
| `EditAccessSettingsRequest` | `bots.EditAccessSettingsRequest` | `(self, bot: 'TypeInputUser', restricted: Optional[bool] = None, add_users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `EditPreviewMediaRequest` | `bots.EditPreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia', new_media: 'TypeInputMedia')` |
| `ExportBotTokenRequest` | `bots.ExportBotTokenRequest` | `(self, bot: 'TypeInputUser', revoke: bool)` |
| `GetAccessSettingsRequest` | `bots.GetAccessSettingsRequest` | `(self, bot: 'TypeInputUser')` |
| `GetAdminedBotsRequest` | `bots.GetAdminedBotsRequest` | `(self, /, *args, **kwargs)` |
| `GetBotCommandsRequest` | `bots.GetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str)` |
| `GetBotInfoRequest` | `bots.GetBotInfoRequest` | `(self, lang_code: str, bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `GetBotMenuButtonRequest` | `bots.GetBotMenuButtonRequest` | `(self, user_id: 'TypeInputUser')` |
| `GetBotRecommendationsRequest` | `bots.GetBotRecommendationsRequest` | `(self, bot: 'TypeInputUser')` |
| `GetPopularAppBotsRequest` | `bots.GetPopularAppBotsRequest` | `(self, offset: str, limit: int)` |
| `GetPreviewInfoRequest` | `bots.GetPreviewInfoRequest` | `(self, bot: 'TypeInputUser', lang_code: str)` |
| `GetPreviewMediasRequest` | `bots.GetPreviewMediasRequest` | `(self, bot: 'TypeInputUser')` |
| `GetRequestedWebViewButtonRequest` | `bots.GetRequestedWebViewButtonRequest` | `(self, bot: 'TypeInputUser', webapp_req_id: str)` |
| `InvokeWebViewCustomMethodRequest` | `bots.InvokeWebViewCustomMethodRequest` | `(self, bot: 'TypeInputUser', custom_method: str, params: 'TypeDataJSON')` |
| `ReorderPreviewMediasRequest` | `bots.ReorderPreviewMediasRequest` | `(self, bot: 'TypeInputUser', lang_code: str, order: List[ForwardRef('TypeInputMedia')])` |
| `ReorderUsernamesRequest` | `bots.ReorderUsernamesRequest` | `(self, bot: 'TypeInputUser', order: List[str])` |
| `RequestWebViewButtonRequest` | `bots.RequestWebViewButtonRequest` | `(self, user_id: 'TypeInputUser', button: 'TypeKeyboardButton')` |
| `ResetBotCommandsRequest` | `bots.ResetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str)` |
| `SendCustomRequestRequest` | `bots.SendCustomRequestRequest` | `(self, custom_method: str, params: 'TypeDataJSON')` |
| `SetBotBroadcastDefaultAdminRightsRequest` | `bots.SetBotBroadcastDefaultAdminRightsRequest` | `(self, admin_rights: 'TypeChatAdminRights')` |
| `SetBotCommandsRequest` | `bots.SetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str, commands: List[ForwardRef('TypeBotCommand')])` |
| `SetBotGroupDefaultAdminRightsRequest` | `bots.SetBotGroupDefaultAdminRightsRequest` | `(self, admin_rights: 'TypeChatAdminRights')` |
| `SetBotInfoRequest` | `bots.SetBotInfoRequest` | `(self, lang_code: str, bot: Optional[ForwardRef('TypeInputUser')] = None, name: Optional[str] = None, about: Optional[str] = None, description: Optional[str] = None)` |
| `SetBotMenuButtonRequest` | `bots.SetBotMenuButtonRequest` | `(self, user_id: 'TypeInputUser', button: 'TypeBotMenuButton')` |
| `SetCustomVerificationRequest` | `bots.SetCustomVerificationRequest` | `(self, peer: 'TypeInputPeer', enabled: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None, custom_description: Optional[str] = None)` |
| `SetJoinChatResultsRequest` | `bots.SetJoinChatResultsRequest` | `(self, query_id: int, result: 'TypeJoinChatBotResult')` |
| `ToggleUserEmojiStatusPermissionRequest` | `bots.ToggleUserEmojiStatusPermissionRequest` | `(self, bot: 'TypeInputUser', enabled: bool)` |
| `ToggleUsernameRequest` | `bots.ToggleUsernameRequest` | `(self, bot: 'TypeInputUser', username: str, active: bool)` |
| `UpdateStarRefProgramRequest` | `bots.UpdateStarRefProgramRequest` | `(self, bot: 'TypeInputUser', commission_permille: int, duration_months: Optional[int] = None)` |
| `UpdateUserEmojiStatusRequest` | `bots.UpdateUserEmojiStatusRequest` | `(self, user_id: 'TypeInputUser', emoji_status: 'TypeEmojiStatus')` |

### `channels`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `CheckSearchPostsFloodRequest` | `channels.CheckSearchPostsFloodRequest` | `(self, query: Optional[str] = None)` |
| `CheckUsernameRequest` | `channels.CheckUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str)` |
| `ConvertToGigagroupRequest` | `channels.ConvertToGigagroupRequest` | `(self, channel: 'TypeInputChannel')` |
| `CreateChannelRequest` | `channels.CreateChannelRequest` | `(self, title: str, about: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, for_import: Optional[bool] = None, forum: Optional[bool] = None, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None, address: Optional[str] = None, ttl_period: Optional[int] = None)` |
| `DeactivateAllUsernamesRequest` | `channels.DeactivateAllUsernamesRequest` | `(self, channel: 'TypeInputChannel')` |
| `DeleteChannelRequest` | `channels.DeleteChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `DeleteHistoryRequest` | `channels.DeleteHistoryRequest` | `(self, channel: 'TypeInputChannel', max_id: int, for_everyone: Optional[bool] = None)` |
| `DeleteMessagesRequest` | `channels.DeleteMessagesRequest` | `(self, channel: 'TypeInputChannel', id: List[int])` |
| `DeleteParticipantHistoryRequest` | `channels.DeleteParticipantHistoryRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer')` |
| `EditAdminRequest` | `channels.EditAdminRequest` | `(self, channel: 'TypeInputChannel', user_id: 'TypeInputUser', admin_rights: 'TypeChatAdminRights', rank: Optional[str] = None)` |
| `EditBannedRequest` | `channels.EditBannedRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer', banned_rights: 'TypeChatBannedRights')` |
| `EditLocationRequest` | `channels.EditLocationRequest` | `(self, channel: 'TypeInputChannel', geo_point: 'TypeInputGeoPoint', address: str)` |
| `EditPhotoRequest` | `channels.EditPhotoRequest` | `(self, channel: 'TypeInputChannel', photo: 'TypeInputChatPhoto')` |
| `EditTitleRequest` | `channels.EditTitleRequest` | `(self, channel: 'TypeInputChannel', title: str)` |
| `ExportMessageLinkRequest` | `channels.ExportMessageLinkRequest` | `(self, channel: 'TypeInputChannel', id: int, grouped: Optional[bool] = None, thread: Optional[bool] = None)` |
| `GetAdminLogRequest` | `channels.GetAdminLogRequest` | `(self, channel: 'TypeInputChannel', q: str, max_id: int, min_id: int, limit: int, events_filter: Optional[ForwardRef('TypeChannelAdminLogEventsFilter')] = None, admins: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `GetAdminedPublicChannelsRequest` | `channels.GetAdminedPublicChannelsRequest` | `(self, by_location: Optional[bool] = None, check_limit: Optional[bool] = None, for_personal: Optional[bool] = None)` |
| `GetChannelRecommendationsRequest` | `channels.GetChannelRecommendationsRequest` | `(self, channel: Optional[ForwardRef('TypeInputChannel')] = None)` |
| `GetChannelsRequest` | `channels.GetChannelsRequest` | `(self, id: List[ForwardRef('TypeInputChannel')])` |
| `GetFullChannelRequest` | `channels.GetFullChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `GetGroupsForDiscussionRequest` | `channels.GetGroupsForDiscussionRequest` | `(self, /, *args, **kwargs)` |
| `GetInactiveChannelsRequest` | `channels.GetInactiveChannelsRequest` | `(self, /, *args, **kwargs)` |
| `GetLeftChannelsRequest` | `channels.GetLeftChannelsRequest` | `(self, offset: int)` |
| `GetMessageAuthorRequest` | `channels.GetMessageAuthorRequest` | `(self, channel: 'TypeInputChannel', id: int)` |
| `GetMessagesRequest` | `channels.GetMessagesRequest` | `(self, channel: 'TypeInputChannel', id: List[ForwardRef('TypeInputMessage')])` |
| `GetParticipantRequest` | `channels.GetParticipantRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer')` |
| `GetParticipantsRequest` | `channels.GetParticipantsRequest` | `(self, channel: 'TypeInputChannel', filter: 'TypeChannelParticipantsFilter', offset: int, limit: int, hash: int)` |
| `GetSendAsRequest` | `channels.GetSendAsRequest` | `(self, peer: 'TypeInputPeer', for_paid_reactions: Optional[bool] = None, for_live_stories: Optional[bool] = None)` |
| `InviteToChannelRequest` | `channels.InviteToChannelRequest` | `(self, channel: 'TypeInputChannel', users: List[ForwardRef('TypeInputUser')])` |
| `JoinChannelRequest` | `channels.JoinChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `LeaveChannelRequest` | `channels.LeaveChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `ReadHistoryRequest` | `channels.ReadHistoryRequest` | `(self, channel: 'TypeInputChannel', max_id: int)` |
| `ReadMessageContentsRequest` | `channels.ReadMessageContentsRequest` | `(self, channel: 'TypeInputChannel', id: List[int])` |
| `ReorderUsernamesRequest` | `channels.ReorderUsernamesRequest` | `(self, channel: 'TypeInputChannel', order: List[str])` |
| `ReportAntiSpamFalsePositiveRequest` | `channels.ReportAntiSpamFalsePositiveRequest` | `(self, channel: 'TypeInputChannel', msg_id: int)` |
| `ReportSpamRequest` | `channels.ReportSpamRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer', id: List[int])` |
| `RestrictSponsoredMessagesRequest` | `channels.RestrictSponsoredMessagesRequest` | `(self, channel: 'TypeInputChannel', restricted: bool)` |
| `SearchPostsRequest` | `channels.SearchPostsRequest` | `(self, offset_rate: int, offset_peer: 'TypeInputPeer', offset_id: int, limit: int, hashtag: Optional[str] = None, query: Optional[str] = None, allow_paid_stars: Optional[int] = None)` |
| `SetBoostsToUnblockRestrictionsRequest` | `channels.SetBoostsToUnblockRestrictionsRequest` | `(self, channel: 'TypeInputChannel', boosts: int)` |
| `SetDiscussionGroupRequest` | `channels.SetDiscussionGroupRequest` | `(self, broadcast: 'TypeInputChannel', group: 'TypeInputChannel')` |
| `SetEmojiStickersRequest` | `channels.SetEmojiStickersRequest` | `(self, channel: 'TypeInputChannel', stickerset: 'TypeInputStickerSet')` |
| `SetMainProfileTabRequest` | `channels.SetMainProfileTabRequest` | `(self, channel: 'TypeInputChannel', tab: 'TypeProfileTab')` |
| `SetStickersRequest` | `channels.SetStickersRequest` | `(self, channel: 'TypeInputChannel', stickerset: 'TypeInputStickerSet')` |
| `ToggleAntiSpamRequest` | `channels.ToggleAntiSpamRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `ToggleAutotranslationRequest` | `channels.ToggleAutotranslationRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `ToggleForumRequest` | `channels.ToggleForumRequest` | `(self, channel: 'TypeInputChannel', enabled: bool, tabs: bool)` |
| `ToggleJoinRequestRequest` | `channels.ToggleJoinRequestRequest` | `(self, channel: 'TypeInputChannel', enabled: bool, apply_to_invites: Optional[bool] = None, guard_bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `ToggleJoinToSendRequest` | `channels.ToggleJoinToSendRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `ToggleParticipantsHiddenRequest` | `channels.ToggleParticipantsHiddenRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `TogglePreHistoryHiddenRequest` | `channels.TogglePreHistoryHiddenRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `ToggleSignaturesRequest` | `channels.ToggleSignaturesRequest` | `(self, channel: 'TypeInputChannel', signatures_enabled: Optional[bool] = None, profiles_enabled: Optional[bool] = None)` |
| `ToggleSlowModeRequest` | `channels.ToggleSlowModeRequest` | `(self, channel: 'TypeInputChannel', seconds: int)` |
| `ToggleUsernameRequest` | `channels.ToggleUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str, active: bool)` |
| `ToggleViewForumAsMessagesRequest` | `channels.ToggleViewForumAsMessagesRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `UpdateColorRequest` | `channels.UpdateColorRequest` | `(self, channel: 'TypeInputChannel', for_profile: Optional[bool] = None, color: Optional[int] = None, background_emoji_id: Optional[int] = None)` |
| `UpdateEmojiStatusRequest` | `channels.UpdateEmojiStatusRequest` | `(self, channel: 'TypeInputChannel', emoji_status: 'TypeEmojiStatus')` |
| `UpdatePaidMessagesPriceRequest` | `channels.UpdatePaidMessagesPriceRequest` | `(self, channel: 'TypeInputChannel', send_paid_messages_stars: int, broadcast_messages_allowed: Optional[bool] = None)` |
| `UpdateUsernameRequest` | `channels.UpdateUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str)` |

### `chatlists`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `CheckChatlistInviteRequest` | `chatlists.CheckChatlistInviteRequest` | `(self, slug: str)` |
| `DeleteExportedInviteRequest` | `chatlists.DeleteExportedInviteRequest` | `(self, chatlist: 'TypeInputChatlist', slug: str)` |
| `EditExportedInviteRequest` | `chatlists.EditExportedInviteRequest` | `(self, chatlist: 'TypeInputChatlist', slug: str, title: Optional[str] = None, peers: Optional[List[ForwardRef('TypeInputPeer')]] = None)` |
| `ExportChatlistInviteRequest` | `chatlists.ExportChatlistInviteRequest` | `(self, chatlist: 'TypeInputChatlist', title: str, peers: List[ForwardRef('TypeInputPeer')])` |
| `GetChatlistUpdatesRequest` | `chatlists.GetChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `GetExportedInvitesRequest` | `chatlists.GetExportedInvitesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `GetLeaveChatlistSuggestionsRequest` | `chatlists.GetLeaveChatlistSuggestionsRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `HideChatlistUpdatesRequest` | `chatlists.HideChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `JoinChatlistInviteRequest` | `chatlists.JoinChatlistInviteRequest` | `(self, slug: str, peers: List[ForwardRef('TypeInputPeer')])` |
| `JoinChatlistUpdatesRequest` | `chatlists.JoinChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist', peers: List[ForwardRef('TypeInputPeer')])` |
| `LeaveChatlistRequest` | `chatlists.LeaveChatlistRequest` | `(self, chatlist: 'TypeInputChatlist', peers: List[ForwardRef('TypeInputPeer')])` |

### `contacts`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AcceptContactRequest` | `contacts.AcceptContactRequest` | `(self, id: 'TypeInputUser')` |
| `AddContactRequest` | `contacts.AddContactRequest` | `(self, id: 'TypeInputUser', first_name: str, last_name: str, phone: str, add_phone_privacy_exception: Optional[bool] = None, note: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `BlockFromRepliesRequest` | `contacts.BlockFromRepliesRequest` | `(self, msg_id: int, delete_message: Optional[bool] = None, delete_history: Optional[bool] = None, report_spam: Optional[bool] = None)` |
| `BlockRequest` | `contacts.BlockRequest` | `(self, id: 'TypeInputPeer', my_stories_from: Optional[bool] = None)` |
| `DeleteByPhonesRequest` | `contacts.DeleteByPhonesRequest` | `(self, phones: List[str])` |
| `DeleteContactsRequest` | `contacts.DeleteContactsRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `EditCloseFriendsRequest` | `contacts.EditCloseFriendsRequest` | `(self, id: List[int])` |
| `ExportContactTokenRequest` | `contacts.ExportContactTokenRequest` | `(self, /, *args, **kwargs)` |
| `GetBirthdaysRequest` | `contacts.GetBirthdaysRequest` | `(self, /, *args, **kwargs)` |
| `GetBlockedRequest` | `contacts.GetBlockedRequest` | `(self, offset: int, limit: int, my_stories_from: Optional[bool] = None)` |
| `GetContactIDsRequest` | `contacts.GetContactIDsRequest` | `(self, hash: int)` |
| `GetContactsRequest` | `contacts.GetContactsRequest` | `(self, hash: int)` |
| `GetLocatedRequest` | `contacts.GetLocatedRequest` | `(self, geo_point: 'TypeInputGeoPoint', background: Optional[bool] = None, self_expires: Optional[int] = None)` |
| `GetSavedRequest` | `contacts.GetSavedRequest` | `(self, /, *args, **kwargs)` |
| `GetSponsoredPeersRequest` | `contacts.GetSponsoredPeersRequest` | `(self, q: str)` |
| `GetStatusesRequest` | `contacts.GetStatusesRequest` | `(self, /, *args, **kwargs)` |
| `GetTopPeersRequest` | `contacts.GetTopPeersRequest` | `(self, offset: int, limit: int, hash: int, correspondents: Optional[bool] = None, bots_pm: Optional[bool] = None, bots_inline: Optional[bool] = None, phone_calls: Optional[bool] = None, forward_users: Optional[bool] = None, forward_chats: Optional[bool] = None, groups: Optional[bool] = None, channels: Optional[bool] = None, bots_app: Optional[bool] = None, bots_guestchat: Optional[bool] = None)` |
| `ImportContactTokenRequest` | `contacts.ImportContactTokenRequest` | `(self, token: str)` |
| `ImportContactsRequest` | `contacts.ImportContactsRequest` | `(self, contacts: List[ForwardRef('TypeInputContact')])` |
| `ResetSavedRequest` | `contacts.ResetSavedRequest` | `(self, /, *args, **kwargs)` |
| `ResetTopPeerRatingRequest` | `contacts.ResetTopPeerRatingRequest` | `(self, category: 'TypeTopPeerCategory', peer: 'TypeInputPeer')` |
| `ResolvePhoneRequest` | `contacts.ResolvePhoneRequest` | `(self, phone: str)` |
| `ResolveUsernameRequest` | `contacts.ResolveUsernameRequest` | `(self, username: str, referer: Optional[str] = None)` |
| `SearchRequest` | `contacts.SearchRequest` | `(self, q: str, limit: int, broadcasts: Optional[bool] = None, bots: Optional[bool] = None)` |
| `SetBlockedRequest` | `contacts.SetBlockedRequest` | `(self, id: List[ForwardRef('TypeInputPeer')], limit: int, my_stories_from: Optional[bool] = None)` |
| `ToggleTopPeersRequest` | `contacts.ToggleTopPeersRequest` | `(self, enabled: bool)` |
| `UnblockRequest` | `contacts.UnblockRequest` | `(self, id: 'TypeInputPeer', my_stories_from: Optional[bool] = None)` |
| `UpdateContactNoteRequest` | `contacts.UpdateContactNoteRequest` | `(self, id: 'TypeInputUser', note: 'TypeTextWithEntities')` |

### `folders`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `EditPeerFoldersRequest` | `folders.EditPeerFoldersRequest` | `(self, folder_peers: List[ForwardRef('TypeInputFolderPeer')])` |

### `fragment`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `GetCollectibleInfoRequest` | `fragment.GetCollectibleInfoRequest` | `(self, collectible: 'TypeInputCollectible')` |

### `help`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AcceptTermsOfServiceRequest` | `help.AcceptTermsOfServiceRequest` | `(self, id: 'TypeDataJSON')` |
| `DismissSuggestionRequest` | `help.DismissSuggestionRequest` | `(self, peer: 'TypeInputPeer', suggestion: str)` |
| `EditUserInfoRequest` | `help.EditUserInfoRequest` | `(self, user_id: 'TypeInputUser', message: str, entities: List[ForwardRef('TypeMessageEntity')])` |
| `GetAppConfigRequest` | `help.GetAppConfigRequest` | `(self, hash: int)` |
| `GetAppUpdateRequest` | `help.GetAppUpdateRequest` | `(self, source: str)` |
| `GetCdnConfigRequest` | `help.GetCdnConfigRequest` | `(self, /, *args, **kwargs)` |
| `GetConfigRequest` | `help.GetConfigRequest` | `(self, /, *args, **kwargs)` |
| `GetCountriesListRequest` | `help.GetCountriesListRequest` | `(self, lang_code: str, hash: int)` |
| `GetDeepLinkInfoRequest` | `help.GetDeepLinkInfoRequest` | `(self, path: str)` |
| `GetInviteTextRequest` | `help.GetInviteTextRequest` | `(self, /, *args, **kwargs)` |
| `GetNearestDcRequest` | `help.GetNearestDcRequest` | `(self, /, *args, **kwargs)` |
| `GetPassportConfigRequest` | `help.GetPassportConfigRequest` | `(self, hash: int)` |
| `GetPeerColorsRequest` | `help.GetPeerColorsRequest` | `(self, hash: int)` |
| `GetPeerProfileColorsRequest` | `help.GetPeerProfileColorsRequest` | `(self, hash: int)` |
| `GetPremiumPromoRequest` | `help.GetPremiumPromoRequest` | `(self, /, *args, **kwargs)` |
| `GetPromoDataRequest` | `help.GetPromoDataRequest` | `(self, /, *args, **kwargs)` |
| `GetRecentMeUrlsRequest` | `help.GetRecentMeUrlsRequest` | `(self, referer: str)` |
| `GetSupportNameRequest` | `help.GetSupportNameRequest` | `(self, /, *args, **kwargs)` |
| `GetSupportRequest` | `help.GetSupportRequest` | `(self, /, *args, **kwargs)` |
| `GetTermsOfServiceUpdateRequest` | `help.GetTermsOfServiceUpdateRequest` | `(self, /, *args, **kwargs)` |
| `GetTimezonesListRequest` | `help.GetTimezonesListRequest` | `(self, hash: int)` |
| `GetUserInfoRequest` | `help.GetUserInfoRequest` | `(self, user_id: 'TypeInputUser')` |
| `HidePromoDataRequest` | `help.HidePromoDataRequest` | `(self, peer: 'TypeInputPeer')` |
| `SaveAppLogRequest` | `help.SaveAppLogRequest` | `(self, events: List[ForwardRef('TypeInputAppEvent')])` |
| `SetBotUpdatesStatusRequest` | `help.SetBotUpdatesStatusRequest` | `(self, pending_updates_count: int, message: str)` |

### `langpack`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `GetDifferenceRequest` | `langpack.GetDifferenceRequest` | `(self, lang_pack: str, lang_code: str, from_version: int)` |
| `GetLangPackRequest` | `langpack.GetLangPackRequest` | `(self, lang_pack: str, lang_code: str)` |
| `GetLanguageRequest` | `langpack.GetLanguageRequest` | `(self, lang_pack: str, lang_code: str)` |
| `GetLanguagesRequest` | `langpack.GetLanguagesRequest` | `(self, lang_pack: str)` |
| `GetStringsRequest` | `langpack.GetStringsRequest` | `(self, lang_pack: str, lang_code: str, keys: List[str])` |

### `messages`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AcceptEncryptionRequest` | `messages.AcceptEncryptionRequest` | `(self, peer: 'TypeInputEncryptedChat', g_b: bytes, key_fingerprint: int)` |
| `AcceptUrlAuthRequest` | `messages.AcceptUrlAuthRequest` | `(self, write_allowed: Optional[bool] = None, share_phone_number: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None, match_code: Optional[str] = None)` |
| `AddChatUserRequest` | `messages.AddChatUserRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', fwd_limit: int)` |
| `AddPollAnswerRequest` | `messages.AddPollAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, answer: 'TypePollAnswer')` |
| `AppendTodoListRequest` | `messages.AppendTodoListRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, list: List[ForwardRef('TypeTodoItem')])` |
| `CheckChatInviteRequest` | `messages.CheckChatInviteRequest` | `(self, hash: str)` |
| `CheckHistoryImportPeerRequest` | `messages.CheckHistoryImportPeerRequest` | `(self, peer: 'TypeInputPeer')` |
| `CheckHistoryImportRequest` | `messages.CheckHistoryImportRequest` | `(self, import_head: str)` |
| `CheckQuickReplyShortcutRequest` | `messages.CheckQuickReplyShortcutRequest` | `(self, shortcut: str)` |
| `CheckUrlAuthMatchCodeRequest` | `messages.CheckUrlAuthMatchCodeRequest` | `(self, url: str, match_code: str)` |
| `ClearAllDraftsRequest` | `messages.ClearAllDraftsRequest` | `(self, /, *args, **kwargs)` |
| `ClearRecentReactionsRequest` | `messages.ClearRecentReactionsRequest` | `(self, /, *args, **kwargs)` |
| `ClearRecentStickersRequest` | `messages.ClearRecentStickersRequest` | `(self, attached: Optional[bool] = None)` |
| `ClickSponsoredMessageRequest` | `messages.ClickSponsoredMessageRequest` | `(self, media: Optional[bool] = None, fullscreen: Optional[bool] = None, random_id: bytes = None)` |
| `ComposeMessageWithAIRequest` | `messages.ComposeMessageWithAIRequest` | `(self, text: 'TypeTextWithEntities', proofread: Optional[bool] = None, emojify: Optional[bool] = None, translate_to_lang: Optional[str] = None, tone: Optional[ForwardRef('TypeInputAiComposeTone')] = None)` |
| `CreateChatRequest` | `messages.CreateChatRequest` | `(self, users: List[ForwardRef('TypeInputUser')], title: str, ttl_period: Optional[int] = None)` |
| `CreateForumTopicRequest` | `messages.CreateForumTopicRequest` | `(self, peer: 'TypeInputPeer', title: str, title_missing: Optional[bool] = None, icon_color: Optional[int] = None, icon_emoji_id: Optional[int] = None, random_id: int = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `DeclineUrlAuthRequest` | `messages.DeclineUrlAuthRequest` | `(self, url: str)` |
| `DeleteChatRequest` | `messages.DeleteChatRequest` | `(self, chat_id: int)` |
| `DeleteChatUserRequest` | `messages.DeleteChatUserRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', revoke_history: Optional[bool] = None)` |
| `DeleteExportedChatInviteRequest` | `messages.DeleteExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str)` |
| `DeleteFactCheckRequest` | `messages.DeleteFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `DeleteHistoryRequest` | `messages.DeleteHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int, just_clear: Optional[bool] = None, revoke: Optional[bool] = None, min_date: Optional[datetime.datetime] = None, max_date: Optional[datetime.datetime] = None)` |
| `DeleteMessagesRequest` | `messages.DeleteMessagesRequest` | `(self, id: List[int], revoke: Optional[bool] = None)` |
| `DeleteParticipantReactionRequest` | `messages.DeleteParticipantReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, participant: 'TypeInputPeer')` |
| `DeleteParticipantReactionsRequest` | `messages.DeleteParticipantReactionsRequest` | `(self, peer: 'TypeInputPeer', participant: 'TypeInputPeer')` |
| `DeletePhoneCallHistoryRequest` | `messages.DeletePhoneCallHistoryRequest` | `(self, revoke: Optional[bool] = None)` |
| `DeletePollAnswerRequest` | `messages.DeletePollAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, option: bytes)` |
| `DeleteQuickReplyMessagesRequest` | `messages.DeleteQuickReplyMessagesRequest` | `(self, shortcut_id: int, id: List[int])` |
| `DeleteQuickReplyShortcutRequest` | `messages.DeleteQuickReplyShortcutRequest` | `(self, shortcut_id: int)` |
| `DeleteRevokedExportedChatInvitesRequest` | `messages.DeleteRevokedExportedChatInvitesRequest` | `(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser')` |
| `DeleteSavedHistoryRequest` | `messages.DeleteSavedHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None, min_date: Optional[datetime.datetime] = None, max_date: Optional[datetime.datetime] = None)` |
| `DeleteScheduledMessagesRequest` | `messages.DeleteScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `DeleteTopicHistoryRequest` | `messages.DeleteTopicHistoryRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: int)` |
| `DiscardEncryptionRequest` | `messages.DiscardEncryptionRequest` | `(self, chat_id: int, delete_history: Optional[bool] = None)` |
| `EditChatAboutRequest` | `messages.EditChatAboutRequest` | `(self, peer: 'TypeInputPeer', about: str)` |
| `EditChatAdminRequest` | `messages.EditChatAdminRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', is_admin: bool)` |
| `EditChatCreatorRequest` | `messages.EditChatCreatorRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser', password: 'TypeInputCheckPasswordSRP')` |
| `EditChatDefaultBannedRightsRequest` | `messages.EditChatDefaultBannedRightsRequest` | `(self, peer: 'TypeInputPeer', banned_rights: 'TypeChatBannedRights')` |
| `EditChatParticipantRankRequest` | `messages.EditChatParticipantRankRequest` | `(self, peer: 'TypeInputPeer', participant: 'TypeInputPeer', rank: str)` |
| `EditChatPhotoRequest` | `messages.EditChatPhotoRequest` | `(self, chat_id: int, photo: 'TypeInputChatPhoto')` |
| `EditChatTitleRequest` | `messages.EditChatTitleRequest` | `(self, chat_id: int, title: str)` |
| `EditExportedChatInviteRequest` | `messages.EditExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str, revoked: Optional[bool] = None, expire_date: Optional[datetime.datetime] = None, usage_limit: Optional[int] = None, request_needed: Optional[bool] = None, title: Optional[str] = None)` |
| `EditFactCheckRequest` | `messages.EditFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, text: 'TypeTextWithEntities')` |
| `EditForumTopicRequest` | `messages.EditForumTopicRequest` | `(self, peer: 'TypeInputPeer', topic_id: int, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None)` |
| `EditInlineBotMessageRequest` | `messages.EditInlineBotMessageRequest` | `(self, id: 'TypeInputBotInlineMessageID', no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `EditMessageRequest` | `messages.EditMessageRequest` | `(self, peer: 'TypeInputPeer', id: int, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, quick_reply_shortcut_id: Optional[int] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `EditQuickReplyShortcutRequest` | `messages.EditQuickReplyShortcutRequest` | `(self, shortcut_id: int, shortcut: str)` |
| `ExportChatInviteRequest` | `messages.ExportChatInviteRequest` | `(self, peer: 'TypeInputPeer', legacy_revoke_permanent: Optional[bool] = None, request_needed: Optional[bool] = None, expire_date: Optional[datetime.datetime] = None, usage_limit: Optional[int] = None, title: Optional[str] = None, subscription_pricing: Optional[ForwardRef('TypeStarsSubscriptionPricing')] = None)` |
| `FaveStickerRequest` | `messages.FaveStickerRequest` | `(self, id: 'TypeInputDocument', unfave: bool)` |
| `ForwardMessagesRequest` | `messages.ForwardMessagesRequest` | `(self, from_peer: 'TypeInputPeer', id: List[int], to_peer: 'TypeInputPeer', silent: Optional[bool] = None, background: Optional[bool] = None, with_my_score: Optional[bool] = None, drop_author: Optional[bool] = None, drop_media_captions: Optional[bool] = None, noforwards: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, random_id: List[int] = None, top_msg_id: Optional[int] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, video_timestamp: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None)` |
| `GetAdminsWithInvitesRequest` | `messages.GetAdminsWithInvitesRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetAllDraftsRequest` | `messages.GetAllDraftsRequest` | `(self, /, *args, **kwargs)` |
| `GetAllStickersRequest` | `messages.GetAllStickersRequest` | `(self, hash: int)` |
| `GetArchivedStickersRequest` | `messages.GetArchivedStickersRequest` | `(self, offset_id: int, limit: int, masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `GetAttachMenuBotRequest` | `messages.GetAttachMenuBotRequest` | `(self, bot: 'TypeInputUser')` |
| `GetAttachMenuBotsRequest` | `messages.GetAttachMenuBotsRequest` | `(self, hash: int)` |
| `GetAttachedStickersRequest` | `messages.GetAttachedStickersRequest` | `(self, media: 'TypeInputStickeredMedia')` |
| `GetAvailableEffectsRequest` | `messages.GetAvailableEffectsRequest` | `(self, hash: int)` |
| `GetAvailableReactionsRequest` | `messages.GetAvailableReactionsRequest` | `(self, hash: int)` |
| `GetBotAppRequest` | `messages.GetBotAppRequest` | `(self, app: 'TypeInputBotApp', hash: int)` |
| `GetBotCallbackAnswerRequest` | `messages.GetBotCallbackAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, game: Optional[bool] = None, data: Optional[bytes] = None, password: Optional[ForwardRef('TypeInputCheckPasswordSRP')] = None)` |
| `GetChatInviteImportersRequest` | `messages.GetChatInviteImportersRequest` | `(self, peer: 'TypeInputPeer', offset_date: Optional[datetime.datetime], offset_user: 'TypeInputUser', limit: int, requested: Optional[bool] = None, subscription_expired: Optional[bool] = None, link: Optional[str] = None, q: Optional[str] = None)` |
| `GetChatsRequest` | `messages.GetChatsRequest` | `(self, id: List[int])` |
| `GetCommonChatsRequest` | `messages.GetCommonChatsRequest` | `(self, user_id: 'TypeInputUser', max_id: int, limit: int)` |
| `GetCustomEmojiDocumentsRequest` | `messages.GetCustomEmojiDocumentsRequest` | `(self, document_id: List[int])` |
| `GetDefaultHistoryTTLRequest` | `messages.GetDefaultHistoryTTLRequest` | `(self, /, *args, **kwargs)` |
| `GetDefaultTagReactionsRequest` | `messages.GetDefaultTagReactionsRequest` | `(self, hash: int)` |
| `GetDhConfigRequest` | `messages.GetDhConfigRequest` | `(self, version: int, random_length: int)` |
| `GetDialogFiltersRequest` | `messages.GetDialogFiltersRequest` | `(self, /, *args, **kwargs)` |
| `GetDialogUnreadMarksRequest` | `messages.GetDialogUnreadMarksRequest` | `(self, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetDialogsRequest` | `messages.GetDialogsRequest` | `(self, offset_date: Optional[datetime.datetime], offset_id: int, offset_peer: 'TypeInputPeer', limit: int, hash: int, exclude_pinned: Optional[bool] = None, folder_id: Optional[int] = None)` |
| `GetDiscussionMessageRequest` | `messages.GetDiscussionMessageRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `GetDocumentByHashRequest` | `messages.GetDocumentByHashRequest` | `(self, sha256: bytes, size: int, mime_type: str)` |
| `GetEmojiGameInfoRequest` | `messages.GetEmojiGameInfoRequest` | `(self, /, *args, **kwargs)` |
| `GetEmojiGroupsRequest` | `messages.GetEmojiGroupsRequest` | `(self, hash: int)` |
| `GetEmojiKeywordsDifferenceRequest` | `messages.GetEmojiKeywordsDifferenceRequest` | `(self, lang_code: str, from_version: int)` |
| `GetEmojiKeywordsLanguagesRequest` | `messages.GetEmojiKeywordsLanguagesRequest` | `(self, lang_codes: List[str])` |
| `GetEmojiKeywordsRequest` | `messages.GetEmojiKeywordsRequest` | `(self, lang_code: str)` |
| `GetEmojiProfilePhotoGroupsRequest` | `messages.GetEmojiProfilePhotoGroupsRequest` | `(self, hash: int)` |
| `GetEmojiStatusGroupsRequest` | `messages.GetEmojiStatusGroupsRequest` | `(self, hash: int)` |
| `GetEmojiStickerGroupsRequest` | `messages.GetEmojiStickerGroupsRequest` | `(self, hash: int)` |
| `GetEmojiStickersRequest` | `messages.GetEmojiStickersRequest` | `(self, hash: int)` |
| `GetEmojiURLRequest` | `messages.GetEmojiURLRequest` | `(self, lang_code: str)` |
| `GetExportedChatInviteRequest` | `messages.GetExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str)` |
| `GetExportedChatInvitesRequest` | `messages.GetExportedChatInvitesRequest` | `(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser', limit: int, revoked: Optional[bool] = None, offset_date: Optional[datetime.datetime] = None, offset_link: Optional[str] = None)` |
| `GetExtendedMediaRequest` | `messages.GetExtendedMediaRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `GetFactCheckRequest` | `messages.GetFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: List[int])` |
| `GetFavedStickersRequest` | `messages.GetFavedStickersRequest` | `(self, hash: int)` |
| `GetFeaturedEmojiStickersRequest` | `messages.GetFeaturedEmojiStickersRequest` | `(self, hash: int)` |
| `GetFeaturedStickersRequest` | `messages.GetFeaturedStickersRequest` | `(self, hash: int)` |
| `GetForumTopicsByIDRequest` | `messages.GetForumTopicsByIDRequest` | `(self, peer: 'TypeInputPeer', topics: List[int])` |
| `GetForumTopicsRequest` | `messages.GetForumTopicsRequest` | `(self, peer: 'TypeInputPeer', offset_date: Optional[datetime.datetime], offset_id: int, offset_topic: int, limit: int, q: Optional[str] = None)` |
| `GetFullChatRequest` | `messages.GetFullChatRequest` | `(self, chat_id: int)` |
| `GetFutureChatCreatorAfterLeaveRequest` | `messages.GetFutureChatCreatorAfterLeaveRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetGameHighScoresRequest` | `messages.GetGameHighScoresRequest` | `(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser')` |
| `GetHistoryRequest` | `messages.GetHistoryRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int)` |
| `GetInlineBotResultsRequest` | `messages.GetInlineBotResultsRequest` | `(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', query: str, offset: str, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None)` |
| `GetInlineGameHighScoresRequest` | `messages.GetInlineGameHighScoresRequest` | `(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser')` |
| `GetMaskStickersRequest` | `messages.GetMaskStickersRequest` | `(self, hash: int)` |
| `GetMessageEditDataRequest` | `messages.GetMessageEditDataRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `GetMessageReactionsListRequest` | `messages.GetMessageReactionsListRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, reaction: Optional[ForwardRef('TypeReaction')] = None, offset: Optional[str] = None)` |
| `GetMessageReadParticipantsRequest` | `messages.GetMessageReadParticipantsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `GetMessagesReactionsRequest` | `messages.GetMessagesReactionsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `GetMessagesRequest` | `messages.GetMessagesRequest` | `(self, id: List[ForwardRef('TypeInputMessage')])` |
| `GetMessagesViewsRequest` | `messages.GetMessagesViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int], increment: bool)` |
| `GetMyStickersRequest` | `messages.GetMyStickersRequest` | `(self, offset_id: int, limit: int)` |
| `GetOldFeaturedStickersRequest` | `messages.GetOldFeaturedStickersRequest` | `(self, offset: int, limit: int, hash: int)` |
| `GetOnlinesRequest` | `messages.GetOnlinesRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetOutboxReadDateRequest` | `messages.GetOutboxReadDateRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `GetPaidReactionPrivacyRequest` | `messages.GetPaidReactionPrivacyRequest` | `(self, /, *args, **kwargs)` |
| `GetPeerDialogsRequest` | `messages.GetPeerDialogsRequest` | `(self, peers: List[ForwardRef('TypeInputDialogPeer')])` |
| `GetPeerSettingsRequest` | `messages.GetPeerSettingsRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetPersonalChannelHistoryRequest` | `messages.GetPersonalChannelHistoryRequest` | `(self, user_id: 'TypeInputUser', limit: int, max_id: int, min_id: int, hash: int)` |
| `GetPinnedDialogsRequest` | `messages.GetPinnedDialogsRequest` | `(self, folder_id: int)` |
| `GetPinnedSavedDialogsRequest` | `messages.GetPinnedSavedDialogsRequest` | `(self, /, *args, **kwargs)` |
| `GetPollResultsRequest` | `messages.GetPollResultsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, poll_hash: int)` |
| `GetPollVotesRequest` | `messages.GetPollVotesRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, option: Optional[bytes] = None, offset: Optional[str] = None)` |
| `GetPreparedInlineMessageRequest` | `messages.GetPreparedInlineMessageRequest` | `(self, bot: 'TypeInputUser', id: str)` |
| `GetQuickRepliesRequest` | `messages.GetQuickRepliesRequest` | `(self, hash: int)` |
| `GetQuickReplyMessagesRequest` | `messages.GetQuickReplyMessagesRequest` | `(self, shortcut_id: int, hash: int, id: Optional[List[int]] = None)` |
| `GetRecentLocationsRequest` | `messages.GetRecentLocationsRequest` | `(self, peer: 'TypeInputPeer', limit: int, hash: int)` |
| `GetRecentReactionsRequest` | `messages.GetRecentReactionsRequest` | `(self, limit: int, hash: int)` |
| `GetRecentStickersRequest` | `messages.GetRecentStickersRequest` | `(self, hash: int, attached: Optional[bool] = None)` |
| `GetRepliesRequest` | `messages.GetRepliesRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int)` |
| `GetRichMessageRequest` | `messages.GetRichMessageRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `GetSavedDialogsByIDRequest` | `messages.GetSavedDialogsByIDRequest` | `(self, ids: List[ForwardRef('TypeInputPeer')], parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetSavedDialogsRequest` | `messages.GetSavedDialogsRequest` | `(self, offset_date: Optional[datetime.datetime], offset_id: int, offset_peer: 'TypeInputPeer', limit: int, hash: int, exclude_pinned: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetSavedGifsRequest` | `messages.GetSavedGifsRequest` | `(self, hash: int)` |
| `GetSavedHistoryRequest` | `messages.GetSavedHistoryRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetSavedReactionTagsRequest` | `messages.GetSavedReactionTagsRequest` | `(self, hash: int, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetScheduledHistoryRequest` | `messages.GetScheduledHistoryRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `GetScheduledMessagesRequest` | `messages.GetScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `GetSearchCountersRequest` | `messages.GetSearchCountersRequest` | `(self, peer: 'TypeInputPeer', filters: List[ForwardRef('TypeMessagesFilter')], saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, top_msg_id: Optional[int] = None)` |
| `GetSearchResultsCalendarRequest` | `messages.GetSearchResultsCalendarRequest` | `(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, offset_date: Optional[datetime.datetime], saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetSearchResultsPositionsRequest` | `messages.GetSearchResultsPositionsRequest` | `(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, limit: int, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetSplitRangesRequest` | `messages.GetSplitRangesRequest` | `(self, /, *args, **kwargs)` |
| `GetSponsoredMessagesRequest` | `messages.GetSponsoredMessagesRequest` | `(self, peer: 'TypeInputPeer', msg_id: Optional[int] = None)` |
| `GetStickerSetRequest` | `messages.GetStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', hash: int)` |
| `GetStickersRequest` | `messages.GetStickersRequest` | `(self, emoticon: str, hash: int)` |
| `GetSuggestedDialogFiltersRequest` | `messages.GetSuggestedDialogFiltersRequest` | `(self, /, *args, **kwargs)` |
| `GetTopReactionsRequest` | `messages.GetTopReactionsRequest` | `(self, limit: int, hash: int)` |
| `GetUnreadMentionsRequest` | `messages.GetUnreadMentionsRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None)` |
| `GetUnreadPollVotesRequest` | `messages.GetUnreadPollVotesRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None)` |
| `GetUnreadReactionsRequest` | `messages.GetUnreadReactionsRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetWebPagePreviewRequest` | `messages.GetWebPagePreviewRequest` | `(self, message: str, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None)` |
| `GetWebPageRequest` | `messages.GetWebPageRequest` | `(self, url: str, hash: int)` |
| `HideAllChatJoinRequestsRequest` | `messages.HideAllChatJoinRequestsRequest` | `(self, peer: 'TypeInputPeer', approved: Optional[bool] = None, link: Optional[str] = None)` |
| `HideChatJoinRequestRequest` | `messages.HideChatJoinRequestRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser', approved: Optional[bool] = None)` |
| `HidePeerSettingsBarRequest` | `messages.HidePeerSettingsBarRequest` | `(self, peer: 'TypeInputPeer')` |
| `ImportChatInviteRequest` | `messages.ImportChatInviteRequest` | `(self, hash: str)` |
| `InitHistoryImportRequest` | `messages.InitHistoryImportRequest` | `(self, peer: 'TypeInputPeer', file: 'TypeInputFile', media_count: int)` |
| `InstallStickerSetRequest` | `messages.InstallStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', archived: bool)` |
| `MarkDialogUnreadRequest` | `messages.MarkDialogUnreadRequest` | `(self, peer: 'TypeInputDialogPeer', unread: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `MigrateChatRequest` | `messages.MigrateChatRequest` | `(self, chat_id: int)` |
| `ProlongWebViewRequest` | `messages.ProlongWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', query_id: int, silent: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `RateTranscribedAudioRequest` | `messages.RateTranscribedAudioRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, transcription_id: int, good: bool)` |
| `ReadDiscussionRequest` | `messages.ReadDiscussionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, read_max_id: int)` |
| `ReadEncryptedHistoryRequest` | `messages.ReadEncryptedHistoryRequest` | `(self, peer: 'TypeInputEncryptedChat', max_date: Optional[datetime.datetime])` |
| `ReadFeaturedStickersRequest` | `messages.ReadFeaturedStickersRequest` | `(self, id: List[int])` |
| `ReadHistoryRequest` | `messages.ReadHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int)` |
| `ReadMentionsRequest` | `messages.ReadMentionsRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None)` |
| `ReadMessageContentsRequest` | `messages.ReadMessageContentsRequest` | `(self, id: List[int])` |
| `ReadPollVotesRequest` | `messages.ReadPollVotesRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None)` |
| `ReadReactionsRequest` | `messages.ReadReactionsRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `ReadSavedHistoryRequest` | `messages.ReadSavedHistoryRequest` | `(self, parent_peer: 'TypeInputPeer', peer: 'TypeInputPeer', max_id: int)` |
| `ReceivedMessagesRequest` | `messages.ReceivedMessagesRequest` | `(self, max_id: int)` |
| `ReceivedQueueRequest` | `messages.ReceivedQueueRequest` | `(self, max_qts: int)` |
| `ReorderPinnedDialogsRequest` | `messages.ReorderPinnedDialogsRequest` | `(self, folder_id: int, order: List[ForwardRef('TypeInputDialogPeer')], force: Optional[bool] = None)` |
| `ReorderPinnedForumTopicsRequest` | `messages.ReorderPinnedForumTopicsRequest` | `(self, peer: 'TypeInputPeer', order: List[int], force: Optional[bool] = None)` |
| `ReorderPinnedSavedDialogsRequest` | `messages.ReorderPinnedSavedDialogsRequest` | `(self, order: List[ForwardRef('TypeInputDialogPeer')], force: Optional[bool] = None)` |
| `ReorderQuickRepliesRequest` | `messages.ReorderQuickRepliesRequest` | `(self, order: List[int])` |
| `ReorderStickerSetsRequest` | `messages.ReorderStickerSetsRequest` | `(self, order: List[int], masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `ReportEncryptedSpamRequest` | `messages.ReportEncryptedSpamRequest` | `(self, peer: 'TypeInputEncryptedChat')` |
| `ReportMessagesDeliveryRequest` | `messages.ReportMessagesDeliveryRequest` | `(self, peer: 'TypeInputPeer', id: List[int], push: Optional[bool] = None)` |
| `ReportMusicListenRequest` | `messages.ReportMusicListenRequest` | `(self, id: 'TypeInputDocument', listened_duration: int)` |
| `ReportReactionRequest` | `messages.ReportReactionRequest` | `(self, peer: 'TypeInputPeer', id: int, reaction_peer: 'TypeInputPeer')` |
| `ReportReadMetricsRequest` | `messages.ReportReadMetricsRequest` | `(self, peer: 'TypeInputPeer', metrics: List[ForwardRef('TypeInputMessageReadMetric')])` |
| `ReportRequest` | `messages.ReportRequest` | `(self, peer: 'TypeInputPeer', id: List[int], option: bytes, message: str)` |
| `ReportSpamRequest` | `messages.ReportSpamRequest` | `(self, peer: 'TypeInputPeer')` |
| `ReportSponsoredMessageRequest` | `messages.ReportSponsoredMessageRequest` | `(self, option: bytes, random_id: bytes = None)` |
| `RequestAppWebViewRequest` | `messages.RequestAppWebViewRequest` | `(self, peer: 'TypeInputPeer', app: 'TypeInputBotApp', platform: str, write_allowed: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `RequestEncryptionRequest` | `messages.RequestEncryptionRequest` | `(self, user_id: 'TypeInputUser', g_a: bytes, random_id: int = None)` |
| `RequestMainWebViewRequest` | `messages.RequestMainWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', platform: str, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `RequestSimpleWebViewRequest` | `messages.RequestSimpleWebViewRequest` | `(self, bot: 'TypeInputUser', platform: str, from_switch_webview: Optional[bool] = None, from_side_menu: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `RequestUrlAuthRequest` | `messages.RequestUrlAuthRequest` | `(self, peer: Optional[ForwardRef('TypeInputPeer')] = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None, in_app_origin: Optional[str] = None)` |
| `RequestWebViewRequest` | `messages.RequestWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', platform: str, from_bot_menu: Optional[bool] = None, silent: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `SaveDefaultSendAsRequest` | `messages.SaveDefaultSendAsRequest` | `(self, peer: 'TypeInputPeer', send_as: 'TypeInputPeer')` |
| `SaveDraftRequest` | `messages.SaveDraftRequest` | `(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, effect: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `SaveGifRequest` | `messages.SaveGifRequest` | `(self, id: 'TypeInputDocument', unsave: bool)` |
| `SavePreparedInlineMessageRequest` | `messages.SavePreparedInlineMessageRequest` | `(self, result: 'TypeInputBotInlineResult', user_id: 'TypeInputUser', peer_types: Optional[List[ForwardRef('TypeInlineQueryPeerType')]] = None)` |
| `SaveRecentStickerRequest` | `messages.SaveRecentStickerRequest` | `(self, id: 'TypeInputDocument', unsave: bool, attached: Optional[bool] = None)` |
| `SearchCustomEmojiRequest` | `messages.SearchCustomEmojiRequest` | `(self, emoticon: str, hash: int)` |
| `SearchEmojiStickerSetsRequest` | `messages.SearchEmojiStickerSetsRequest` | `(self, q: str, hash: int, exclude_featured: Optional[bool] = None)` |
| `SearchGlobalRequest` | `messages.SearchGlobalRequest` | `(self, q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime], offset_rate: int, offset_peer: 'TypeInputPeer', offset_id: int, limit: int, broadcasts_only: Optional[bool] = None, groups_only: Optional[bool] = None, users_only: Optional[bool] = None, folder_id: Optional[int] = None)` |
| `SearchRequest` | `messages.SearchRequest` | `(self, peer: 'TypeInputPeer', q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime], offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, from_id: Optional[ForwardRef('TypeInputPeer')] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, saved_reaction: Optional[List[ForwardRef('TypeReaction')]] = None, top_msg_id: Optional[int] = None)` |
| `SearchSentMediaRequest` | `messages.SearchSentMediaRequest` | `(self, q: str, filter: 'TypeMessagesFilter', limit: int)` |
| `SearchStickerSetsRequest` | `messages.SearchStickerSetsRequest` | `(self, q: str, hash: int, exclude_featured: Optional[bool] = None)` |
| `SearchStickersRequest` | `messages.SearchStickersRequest` | `(self, q: str, emoticon: str, lang_code: List[str], offset: int, limit: int, hash: int, emojis: Optional[bool] = None)` |
| `SendBotRequestedPeerRequest` | `messages.SendBotRequestedPeerRequest` | `(self, peer: 'TypeInputPeer', button_id: int, requested_peers: List[ForwardRef('TypeInputPeer')], msg_id: Optional[int] = None, webapp_req_id: Optional[str] = None)` |
| `SendEncryptedFileRequest` | `messages.SendEncryptedFileRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, file: 'TypeInputEncryptedFile', silent: Optional[bool] = None, random_id: int = None)` |
| `SendEncryptedRequest` | `messages.SendEncryptedRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, silent: Optional[bool] = None, random_id: int = None)` |
| `SendEncryptedServiceRequest` | `messages.SendEncryptedServiceRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, random_id: int = None)` |
| `SendInlineBotResultRequest` | `messages.SendInlineBotResultRequest` | `(self, peer: 'TypeInputPeer', query_id: int, id: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, hide_via: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, schedule_date: Optional[datetime.datetime] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, allow_paid_stars: Optional[int] = None)` |
| `SendMediaRequest` | `messages.SendMediaRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', message: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None)` |
| `SendMessageRequest` | `messages.SendMessageRequest` | `(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool] = None, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `SendMultiMediaRequest` | `messages.SendMultiMediaRequest` | `(self, peer: 'TypeInputPeer', multi_media: List[ForwardRef('TypeInputSingleMedia')], silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, schedule_date: Optional[datetime.datetime] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None)` |
| `SendPaidReactionRequest` | `messages.SendPaidReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, count: int, random_id: int = None, private: Optional[ForwardRef('TypePaidReactionPrivacy')] = None)` |
| `SendQuickReplyMessagesRequest` | `messages.SendQuickReplyMessagesRequest` | `(self, peer: 'TypeInputPeer', shortcut_id: int, id: List[int], random_id: List[int] = None)` |
| `SendReactionRequest` | `messages.SendReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, big: Optional[bool] = None, add_to_recent: Optional[bool] = None, reaction: Optional[List[ForwardRef('TypeReaction')]] = None)` |
| `SendScheduledMessagesRequest` | `messages.SendScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `SendScreenshotNotificationRequest` | `messages.SendScreenshotNotificationRequest` | `(self, peer: 'TypeInputPeer', reply_to: 'TypeInputReplyTo', random_id: int = None)` |
| `SendVoteRequest` | `messages.SendVoteRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, options: List[bytes])` |
| `SendWebViewDataRequest` | `messages.SendWebViewDataRequest` | `(self, bot: 'TypeInputUser', button_text: str, data: str, random_id: int = None)` |
| `SendWebViewResultMessageRequest` | `messages.SendWebViewResultMessageRequest` | `(self, bot_query_id: str, result: 'TypeInputBotInlineResult')` |
| `SetBotCallbackAnswerRequest` | `messages.SetBotCallbackAnswerRequest` | `(self, query_id: int, cache_time: int, alert: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None)` |
| `SetBotGuestChatResultRequest` | `messages.SetBotGuestChatResultRequest` | `(self, query_id: int, result: 'TypeInputBotInlineResult')` |
| `SetBotPrecheckoutResultsRequest` | `messages.SetBotPrecheckoutResultsRequest` | `(self, query_id: int, success: Optional[bool] = None, error: Optional[str] = None)` |
| `SetBotShippingResultsRequest` | `messages.SetBotShippingResultsRequest` | `(self, query_id: int, error: Optional[str] = None, shipping_options: Optional[List[ForwardRef('TypeShippingOption')]] = None)` |
| `SetChatAvailableReactionsRequest` | `messages.SetChatAvailableReactionsRequest` | `(self, peer: 'TypeInputPeer', available_reactions: 'TypeChatReactions', reactions_limit: Optional[int] = None, paid_enabled: Optional[bool] = None)` |
| `SetChatThemeRequest` | `messages.SetChatThemeRequest` | `(self, peer: 'TypeInputPeer', theme: 'TypeInputChatTheme')` |
| `SetChatWallPaperRequest` | `messages.SetChatWallPaperRequest` | `(self, peer: 'TypeInputPeer', for_both: Optional[bool] = None, revert: Optional[bool] = None, wallpaper: Optional[ForwardRef('TypeInputWallPaper')] = None, settings: Optional[ForwardRef('TypeWallPaperSettings')] = None, id: Optional[int] = None)` |
| `SetDefaultHistoryTTLRequest` | `messages.SetDefaultHistoryTTLRequest` | `(self, period: int)` |
| `SetDefaultReactionRequest` | `messages.SetDefaultReactionRequest` | `(self, reaction: 'TypeReaction')` |
| `SetEncryptedTypingRequest` | `messages.SetEncryptedTypingRequest` | `(self, peer: 'TypeInputEncryptedChat', typing: bool)` |
| `SetGameScoreRequest` | `messages.SetGameScoreRequest` | `(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser', score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None)` |
| `SetHistoryTTLRequest` | `messages.SetHistoryTTLRequest` | `(self, peer: 'TypeInputPeer', period: int)` |
| `SetInlineBotResultsRequest` | `messages.SetInlineBotResultsRequest` | `(self, query_id: int, results: List[ForwardRef('TypeInputBotInlineResult')], cache_time: int, gallery: Optional[bool] = None, private: Optional[bool] = None, next_offset: Optional[str] = None, switch_pm: Optional[ForwardRef('TypeInlineBotSwitchPM')] = None, switch_webview: Optional[ForwardRef('TypeInlineBotWebView')] = None)` |
| `SetInlineGameScoreRequest` | `messages.SetInlineGameScoreRequest` | `(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser', score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None)` |
| `SetTypingRequest` | `messages.SetTypingRequest` | `(self, peer: 'TypeInputPeer', action: 'TypeSendMessageAction', top_msg_id: Optional[int] = None)` |
| `StartBotRequest` | `messages.StartBotRequest` | `(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', start_param: str, random_id: int = None)` |
| `StartHistoryImportRequest` | `messages.StartHistoryImportRequest` | `(self, peer: 'TypeInputPeer', import_id: int)` |
| `SummarizeTextRequest` | `messages.SummarizeTextRequest` | `(self, peer: 'TypeInputPeer', id: int, to_lang: Optional[str] = None, tone: Optional[str] = None)` |
| `ToggleBotInAttachMenuRequest` | `messages.ToggleBotInAttachMenuRequest` | `(self, bot: 'TypeInputUser', enabled: bool, write_allowed: Optional[bool] = None)` |
| `ToggleDialogFilterTagsRequest` | `messages.ToggleDialogFilterTagsRequest` | `(self, enabled: bool)` |
| `ToggleDialogPinRequest` | `messages.ToggleDialogPinRequest` | `(self, peer: 'TypeInputDialogPeer', pinned: Optional[bool] = None)` |
| `ToggleNoForwardsRequest` | `messages.ToggleNoForwardsRequest` | `(self, peer: 'TypeInputPeer', enabled: bool, request_msg_id: Optional[int] = None)` |
| `TogglePaidReactionPrivacyRequest` | `messages.TogglePaidReactionPrivacyRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, private: 'TypePaidReactionPrivacy')` |
| `TogglePeerTranslationsRequest` | `messages.TogglePeerTranslationsRequest` | `(self, peer: 'TypeInputPeer', disabled: Optional[bool] = None)` |
| `ToggleSavedDialogPinRequest` | `messages.ToggleSavedDialogPinRequest` | `(self, peer: 'TypeInputDialogPeer', pinned: Optional[bool] = None)` |
| `ToggleStickerSetsRequest` | `messages.ToggleStickerSetsRequest` | `(self, stickersets: List[ForwardRef('TypeInputStickerSet')], uninstall: Optional[bool] = None, archive: Optional[bool] = None, unarchive: Optional[bool] = None)` |
| `ToggleSuggestedPostApprovalRequest` | `messages.ToggleSuggestedPostApprovalRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, reject: Optional[bool] = None, schedule_date: Optional[datetime.datetime] = None, reject_comment: Optional[str] = None)` |
| `ToggleTodoCompletedRequest` | `messages.ToggleTodoCompletedRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, completed: List[int], incompleted: List[int])` |
| `TranscribeAudioRequest` | `messages.TranscribeAudioRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `TranslateTextRequest` | `messages.TranslateTextRequest` | `(self, to_lang: str, peer: Optional[ForwardRef('TypeInputPeer')] = None, id: Optional[List[int]] = None, text: Optional[List[ForwardRef('TypeTextWithEntities')]] = None, tone: Optional[str] = None)` |
| `UninstallStickerSetRequest` | `messages.UninstallStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet')` |
| `UnpinAllMessagesRequest` | `messages.UnpinAllMessagesRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `UpdateDialogFilterRequest` | `messages.UpdateDialogFilterRequest` | `(self, id: int, filter: Optional[ForwardRef('TypeDialogFilter')] = None)` |
| `UpdateDialogFiltersOrderRequest` | `messages.UpdateDialogFiltersOrderRequest` | `(self, order: List[int])` |
| `UpdatePinnedForumTopicRequest` | `messages.UpdatePinnedForumTopicRequest` | `(self, peer: 'TypeInputPeer', topic_id: int, pinned: bool)` |
| `UpdatePinnedMessageRequest` | `messages.UpdatePinnedMessageRequest` | `(self, peer: 'TypeInputPeer', id: int, silent: Optional[bool] = None, unpin: Optional[bool] = None, pm_oneside: Optional[bool] = None)` |
| `UpdateSavedReactionTagRequest` | `messages.UpdateSavedReactionTagRequest` | `(self, reaction: 'TypeReaction', title: Optional[str] = None)` |
| `UploadEncryptedFileRequest` | `messages.UploadEncryptedFileRequest` | `(self, peer: 'TypeInputEncryptedChat', file: 'TypeInputEncryptedFile')` |
| `UploadImportedMediaRequest` | `messages.UploadImportedMediaRequest` | `(self, peer: 'TypeInputPeer', import_id: int, file_name: str, media: 'TypeInputMedia')` |
| `UploadMediaRequest` | `messages.UploadMediaRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', business_connection_id: Optional[str] = None)` |
| `ViewSponsoredMessageRequest` | `messages.ViewSponsoredMessageRequest` | `(self, random_id: bytes = None)` |

### `payments`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `ApplyGiftCodeRequest` | `payments.ApplyGiftCodeRequest` | `(self, slug: str)` |
| `AssignAppStoreTransactionRequest` | `payments.AssignAppStoreTransactionRequest` | `(self, receipt: bytes, purpose: 'TypeInputStorePaymentPurpose')` |
| `AssignPlayMarketTransactionRequest` | `payments.AssignPlayMarketTransactionRequest` | `(self, receipt: 'TypeDataJSON', purpose: 'TypeInputStorePaymentPurpose')` |
| `BotCancelStarsSubscriptionRequest` | `payments.BotCancelStarsSubscriptionRequest` | `(self, user_id: 'TypeInputUser', charge_id: str, restore: Optional[bool] = None)` |
| `CanPurchaseStoreRequest` | `payments.CanPurchaseStoreRequest` | `(self, purpose: 'TypeInputStorePaymentPurpose')` |
| `ChangeStarsSubscriptionRequest` | `payments.ChangeStarsSubscriptionRequest` | `(self, peer: 'TypeInputPeer', subscription_id: str, canceled: Optional[bool] = None)` |
| `CheckCanSendGiftRequest` | `payments.CheckCanSendGiftRequest` | `(self, gift_id: int)` |
| `CheckGiftCodeRequest` | `payments.CheckGiftCodeRequest` | `(self, slug: str)` |
| `ClearSavedInfoRequest` | `payments.ClearSavedInfoRequest` | `(self, credentials: Optional[bool] = None, info: Optional[bool] = None)` |
| `ConnectStarRefBotRequest` | `payments.ConnectStarRefBotRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser')` |
| `ConvertStarGiftRequest` | `payments.ConvertStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift')` |
| `CraftStarGiftRequest` | `payments.CraftStarGiftRequest` | `(self, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `CreateStarGiftCollectionRequest` | `payments.CreateStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', title: str, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `DeleteStarGiftCollectionRequest` | `payments.DeleteStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', collection_id: int)` |
| `EditConnectedStarRefBotRequest` | `payments.EditConnectedStarRefBotRequest` | `(self, peer: 'TypeInputPeer', link: str, revoked: Optional[bool] = None)` |
| `ExportInvoiceRequest` | `payments.ExportInvoiceRequest` | `(self, invoice_media: 'TypeInputMedia')` |
| `FulfillStarsSubscriptionRequest` | `payments.FulfillStarsSubscriptionRequest` | `(self, peer: 'TypeInputPeer', subscription_id: str)` |
| `GetBankCardDataRequest` | `payments.GetBankCardDataRequest` | `(self, number: str)` |
| `GetConnectedStarRefBotRequest` | `payments.GetConnectedStarRefBotRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser')` |
| `GetConnectedStarRefBotsRequest` | `payments.GetConnectedStarRefBotsRequest` | `(self, peer: 'TypeInputPeer', limit: int, offset_date: Optional[datetime.datetime] = None, offset_link: Optional[str] = None)` |
| `GetCraftStarGiftsRequest` | `payments.GetCraftStarGiftsRequest` | `(self, gift_id: int, offset: str, limit: int)` |
| `GetGiveawayInfoRequest` | `payments.GetGiveawayInfoRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `GetPaymentFormRequest` | `payments.GetPaymentFormRequest` | `(self, invoice: 'TypeInputInvoice', theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `GetPaymentReceiptRequest` | `payments.GetPaymentReceiptRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `GetPremiumGiftCodeOptionsRequest` | `payments.GetPremiumGiftCodeOptionsRequest` | `(self, boost_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `GetResaleStarGiftsRequest` | `payments.GetResaleStarGiftsRequest` | `(self, gift_id: int, offset: str, limit: int, sort_by_price: Optional[bool] = None, sort_by_num: Optional[bool] = None, for_craft: Optional[bool] = None, stars_only: Optional[bool] = None, attributes_hash: Optional[int] = None, attributes: Optional[List[ForwardRef('TypeStarGiftAttributeId')]] = None)` |
| `GetSavedInfoRequest` | `payments.GetSavedInfoRequest` | `(self, /, *args, **kwargs)` |
| `GetSavedStarGiftRequest` | `payments.GetSavedStarGiftRequest` | `(self, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `GetSavedStarGiftsRequest` | `payments.GetSavedStarGiftsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, exclude_unsaved: Optional[bool] = None, exclude_saved: Optional[bool] = None, exclude_unlimited: Optional[bool] = None, exclude_unique: Optional[bool] = None, sort_by_value: Optional[bool] = None, exclude_upgradable: Optional[bool] = None, exclude_unupgradable: Optional[bool] = None, peer_color_available: Optional[bool] = None, exclude_hosted: Optional[bool] = None, collection_id: Optional[int] = None)` |
| `GetStarGiftActiveAuctionsRequest` | `payments.GetStarGiftActiveAuctionsRequest` | `(self, hash: int)` |
| `GetStarGiftAuctionAcquiredGiftsRequest` | `payments.GetStarGiftAuctionAcquiredGiftsRequest` | `(self, gift_id: int)` |
| `GetStarGiftAuctionStateRequest` | `payments.GetStarGiftAuctionStateRequest` | `(self, auction: 'TypeInputStarGiftAuction', version: int)` |
| `GetStarGiftCollectionsRequest` | `payments.GetStarGiftCollectionsRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `GetStarGiftUpgradeAttributesRequest` | `payments.GetStarGiftUpgradeAttributesRequest` | `(self, gift_id: int)` |
| `GetStarGiftUpgradePreviewRequest` | `payments.GetStarGiftUpgradePreviewRequest` | `(self, gift_id: int)` |
| `GetStarGiftWithdrawalUrlRequest` | `payments.GetStarGiftWithdrawalUrlRequest` | `(self, stargift: 'TypeInputSavedStarGift', password: 'TypeInputCheckPasswordSRP')` |
| `GetStarGiftsRequest` | `payments.GetStarGiftsRequest` | `(self, hash: int)` |
| `GetStarsGiftOptionsRequest` | `payments.GetStarsGiftOptionsRequest` | `(self, user_id: Optional[ForwardRef('TypeInputUser')] = None)` |
| `GetStarsGiveawayOptionsRequest` | `payments.GetStarsGiveawayOptionsRequest` | `(self, /, *args, **kwargs)` |
| `GetStarsRevenueAdsAccountUrlRequest` | `payments.GetStarsRevenueAdsAccountUrlRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetStarsRevenueStatsRequest` | `payments.GetStarsRevenueStatsRequest` | `(self, peer: 'TypeInputPeer', dark: Optional[bool] = None, ton: Optional[bool] = None)` |
| `GetStarsRevenueWithdrawalUrlRequest` | `payments.GetStarsRevenueWithdrawalUrlRequest` | `(self, peer: 'TypeInputPeer', password: 'TypeInputCheckPasswordSRP', ton: Optional[bool] = None, amount: Optional[int] = None)` |
| `GetStarsStatusRequest` | `payments.GetStarsStatusRequest` | `(self, peer: 'TypeInputPeer', ton: Optional[bool] = None)` |
| `GetStarsSubscriptionsRequest` | `payments.GetStarsSubscriptionsRequest` | `(self, peer: 'TypeInputPeer', offset: str, missing_balance: Optional[bool] = None)` |
| `GetStarsTopupOptionsRequest` | `payments.GetStarsTopupOptionsRequest` | `(self, /, *args, **kwargs)` |
| `GetStarsTransactionsByIDRequest` | `payments.GetStarsTransactionsByIDRequest` | `(self, peer: 'TypeInputPeer', id: List[ForwardRef('TypeInputStarsTransaction')], ton: Optional[bool] = None)` |
| `GetStarsTransactionsRequest` | `payments.GetStarsTransactionsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, inbound: Optional[bool] = None, outbound: Optional[bool] = None, ascending: Optional[bool] = None, ton: Optional[bool] = None, subscription_id: Optional[str] = None)` |
| `GetSuggestedStarRefBotsRequest` | `payments.GetSuggestedStarRefBotsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, order_by_revenue: Optional[bool] = None, order_by_date: Optional[bool] = None)` |
| `GetUniqueStarGiftRequest` | `payments.GetUniqueStarGiftRequest` | `(self, slug: str)` |
| `GetUniqueStarGiftValueInfoRequest` | `payments.GetUniqueStarGiftValueInfoRequest` | `(self, slug: str)` |
| `LaunchPrepaidGiveawayRequest` | `payments.LaunchPrepaidGiveawayRequest` | `(self, peer: 'TypeInputPeer', giveaway_id: int, purpose: 'TypeInputStorePaymentPurpose')` |
| `RefundStarsChargeRequest` | `payments.RefundStarsChargeRequest` | `(self, user_id: 'TypeInputUser', charge_id: str)` |
| `ReorderStarGiftCollectionsRequest` | `payments.ReorderStarGiftCollectionsRequest` | `(self, peer: 'TypeInputPeer', order: List[int])` |
| `ResolveStarGiftOfferRequest` | `payments.ResolveStarGiftOfferRequest` | `(self, offer_msg_id: int, decline: Optional[bool] = None)` |
| `SaveStarGiftRequest` | `payments.SaveStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', unsave: Optional[bool] = None)` |
| `SendPaymentFormRequest` | `payments.SendPaymentFormRequest` | `(self, form_id: int, invoice: 'TypeInputInvoice', credentials: 'TypeInputPaymentCredentials', requested_info_id: Optional[str] = None, shipping_option_id: Optional[str] = None, tip_amount: Optional[int] = None)` |
| `SendStarGiftOfferRequest` | `payments.SendStarGiftOfferRequest` | `(self, peer: 'TypeInputPeer', slug: str, price: 'TypeStarsAmount', duration: int, random_id: int = None, allow_paid_stars: Optional[int] = None)` |
| `SendStarsFormRequest` | `payments.SendStarsFormRequest` | `(self, form_id: int, invoice: 'TypeInputInvoice')` |
| `ToggleChatStarGiftNotificationsRequest` | `payments.ToggleChatStarGiftNotificationsRequest` | `(self, peer: 'TypeInputPeer', enabled: Optional[bool] = None)` |
| `ToggleStarGiftsPinnedToTopRequest` | `payments.ToggleStarGiftsPinnedToTopRequest` | `(self, peer: 'TypeInputPeer', stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `TransferStarGiftRequest` | `payments.TransferStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', to_id: 'TypeInputPeer')` |
| `UpdateStarGiftCollectionRequest` | `payments.UpdateStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', collection_id: int, title: Optional[str] = None, delete_stargift: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None, add_stargift: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None, order: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None)` |
| `UpdateStarGiftPriceRequest` | `payments.UpdateStarGiftPriceRequest` | `(self, stargift: 'TypeInputSavedStarGift', resell_amount: 'TypeStarsAmount')` |
| `UpgradeStarGiftRequest` | `payments.UpgradeStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', keep_original_details: Optional[bool] = None)` |
| `ValidateRequestedInfoRequest` | `payments.ValidateRequestedInfoRequest` | `(self, invoice: 'TypeInputInvoice', info: 'TypePaymentRequestedInfo', save: Optional[bool] = None)` |

### `phone`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AcceptCallRequest` | `phone.AcceptCallRequest` | `(self, peer: 'TypeInputPhoneCall', g_b: bytes, protocol: 'TypePhoneCallProtocol')` |
| `CheckGroupCallRequest` | `phone.CheckGroupCallRequest` | `(self, call: 'TypeInputGroupCall', sources: List[int])` |
| `ConfirmCallRequest` | `phone.ConfirmCallRequest` | `(self, peer: 'TypeInputPhoneCall', g_a: bytes, key_fingerprint: int, protocol: 'TypePhoneCallProtocol')` |
| `CreateConferenceCallRequest` | `phone.CreateConferenceCallRequest` | `(self, muted: Optional[bool] = None, video_stopped: Optional[bool] = None, join: Optional[bool] = None, random_id: int = None, public_key: Optional[int] = None, block: Optional[bytes] = None, params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `CreateGroupCallRequest` | `phone.CreateGroupCallRequest` | `(self, peer: 'TypeInputPeer', rtmp_stream: Optional[bool] = None, random_id: int = None, title: Optional[str] = None, schedule_date: Optional[datetime.datetime] = None)` |
| `DeclineConferenceCallInviteRequest` | `phone.DeclineConferenceCallInviteRequest` | `(self, msg_id: int)` |
| `DeleteConferenceCallParticipantsRequest` | `phone.DeleteConferenceCallParticipantsRequest` | `(self, call: 'TypeInputGroupCall', ids: List[int], block: bytes, only_left: Optional[bool] = None, kick: Optional[bool] = None)` |
| `DeleteGroupCallMessagesRequest` | `phone.DeleteGroupCallMessagesRequest` | `(self, call: 'TypeInputGroupCall', messages: List[int], report_spam: Optional[bool] = None)` |
| `DeleteGroupCallParticipantMessagesRequest` | `phone.DeleteGroupCallParticipantMessagesRequest` | `(self, call: 'TypeInputGroupCall', participant: 'TypeInputPeer', report_spam: Optional[bool] = None)` |
| `DiscardCallRequest` | `phone.DiscardCallRequest` | `(self, peer: 'TypeInputPhoneCall', duration: int, reason: 'TypePhoneCallDiscardReason', connection_id: int, video: Optional[bool] = None)` |
| `DiscardGroupCallRequest` | `phone.DiscardGroupCallRequest` | `(self, call: 'TypeInputGroupCall')` |
| `EditGroupCallParticipantRequest` | `phone.EditGroupCallParticipantRequest` | `(self, call: 'TypeInputGroupCall', participant: 'TypeInputPeer', muted: Optional[bool] = None, volume: Optional[int] = None, raise_hand: Optional[bool] = None, video_stopped: Optional[bool] = None, video_paused: Optional[bool] = None, presentation_paused: Optional[bool] = None)` |
| `EditGroupCallTitleRequest` | `phone.EditGroupCallTitleRequest` | `(self, call: 'TypeInputGroupCall', title: str)` |
| `ExportGroupCallInviteRequest` | `phone.ExportGroupCallInviteRequest` | `(self, call: 'TypeInputGroupCall', can_self_unmute: Optional[bool] = None)` |
| `GetCallConfigRequest` | `phone.GetCallConfigRequest` | `(self, /, *args, **kwargs)` |
| `GetGroupCallChainBlocksRequest` | `phone.GetGroupCallChainBlocksRequest` | `(self, call: 'TypeInputGroupCall', sub_chain_id: int, offset: int, limit: int)` |
| `GetGroupCallJoinAsRequest` | `phone.GetGroupCallJoinAsRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetGroupCallRequest` | `phone.GetGroupCallRequest` | `(self, call: 'TypeInputGroupCall', limit: int)` |
| `GetGroupCallStarsRequest` | `phone.GetGroupCallStarsRequest` | `(self, call: 'TypeInputGroupCall')` |
| `GetGroupCallStreamChannelsRequest` | `phone.GetGroupCallStreamChannelsRequest` | `(self, call: 'TypeInputGroupCall')` |
| `GetGroupCallStreamRtmpUrlRequest` | `phone.GetGroupCallStreamRtmpUrlRequest` | `(self, peer: 'TypeInputPeer', revoke: bool, live_story: Optional[bool] = None)` |
| `GetGroupParticipantsRequest` | `phone.GetGroupParticipantsRequest` | `(self, call: 'TypeInputGroupCall', ids: List[ForwardRef('TypeInputPeer')], sources: List[int], offset: str, limit: int)` |
| `InviteConferenceCallParticipantRequest` | `phone.InviteConferenceCallParticipantRequest` | `(self, call: 'TypeInputGroupCall', user_id: 'TypeInputUser', video: Optional[bool] = None)` |
| `InviteToGroupCallRequest` | `phone.InviteToGroupCallRequest` | `(self, call: 'TypeInputGroupCall', users: List[ForwardRef('TypeInputUser')])` |
| `JoinGroupCallPresentationRequest` | `phone.JoinGroupCallPresentationRequest` | `(self, call: 'TypeInputGroupCall', params: 'TypeDataJSON')` |
| `JoinGroupCallRequest` | `phone.JoinGroupCallRequest` | `(self, call: 'TypeInputGroupCall', join_as: 'TypeInputPeer', params: 'TypeDataJSON', muted: Optional[bool] = None, video_stopped: Optional[bool] = None, invite_hash: Optional[str] = None, public_key: Optional[int] = None, block: Optional[bytes] = None)` |
| `LeaveGroupCallPresentationRequest` | `phone.LeaveGroupCallPresentationRequest` | `(self, call: 'TypeInputGroupCall')` |
| `LeaveGroupCallRequest` | `phone.LeaveGroupCallRequest` | `(self, call: 'TypeInputGroupCall', source: int)` |
| `ReceivedCallRequest` | `phone.ReceivedCallRequest` | `(self, peer: 'TypeInputPhoneCall')` |
| `RequestCallRequest` | `phone.RequestCallRequest` | `(self, user_id: 'TypeInputUser', g_a_hash: bytes, protocol: 'TypePhoneCallProtocol', video: Optional[bool] = None, random_id: int = None)` |
| `SaveCallDebugRequest` | `phone.SaveCallDebugRequest` | `(self, peer: 'TypeInputPhoneCall', debug: 'TypeDataJSON')` |
| `SaveCallLogRequest` | `phone.SaveCallLogRequest` | `(self, peer: 'TypeInputPhoneCall', file: 'TypeInputFile')` |
| `SaveDefaultGroupCallJoinAsRequest` | `phone.SaveDefaultGroupCallJoinAsRequest` | `(self, peer: 'TypeInputPeer', join_as: 'TypeInputPeer')` |
| `SaveDefaultSendAsRequest` | `phone.SaveDefaultSendAsRequest` | `(self, call: 'TypeInputGroupCall', send_as: 'TypeInputPeer')` |
| `SendConferenceCallBroadcastRequest` | `phone.SendConferenceCallBroadcastRequest` | `(self, call: 'TypeInputGroupCall', block: bytes)` |
| `SendGroupCallEncryptedMessageRequest` | `phone.SendGroupCallEncryptedMessageRequest` | `(self, call: 'TypeInputGroupCall', encrypted_message: bytes)` |
| `SendGroupCallMessageRequest` | `phone.SendGroupCallMessageRequest` | `(self, call: 'TypeInputGroupCall', message: 'TypeTextWithEntities', random_id: int = None, allow_paid_stars: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `SendSignalingDataRequest` | `phone.SendSignalingDataRequest` | `(self, peer: 'TypeInputPhoneCall', data: bytes)` |
| `SetCallRatingRequest` | `phone.SetCallRatingRequest` | `(self, peer: 'TypeInputPhoneCall', rating: int, comment: str, user_initiative: Optional[bool] = None)` |
| `StartScheduledGroupCallRequest` | `phone.StartScheduledGroupCallRequest` | `(self, call: 'TypeInputGroupCall')` |
| `ToggleGroupCallRecordRequest` | `phone.ToggleGroupCallRecordRequest` | `(self, call: 'TypeInputGroupCall', start: Optional[bool] = None, video: Optional[bool] = None, title: Optional[str] = None, video_portrait: Optional[bool] = None)` |
| `ToggleGroupCallSettingsRequest` | `phone.ToggleGroupCallSettingsRequest` | `(self, call: 'TypeInputGroupCall', reset_invite_hash: Optional[bool] = None, join_muted: Optional[bool] = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None)` |
| `ToggleGroupCallStartSubscriptionRequest` | `phone.ToggleGroupCallStartSubscriptionRequest` | `(self, call: 'TypeInputGroupCall', subscribed: bool)` |

### `photos`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `DeletePhotosRequest` | `photos.DeletePhotosRequest` | `(self, id: List[ForwardRef('TypeInputPhoto')])` |
| `GetUserPhotosRequest` | `photos.GetUserPhotosRequest` | `(self, user_id: 'TypeInputUser', offset: int, max_id: int, limit: int)` |
| `UpdateProfilePhotoRequest` | `photos.UpdateProfilePhotoRequest` | `(self, id: 'TypeInputPhoto', fallback: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `UploadContactProfilePhotoRequest` | `photos.UploadContactProfilePhotoRequest` | `(self, user_id: 'TypeInputUser', suggest: Optional[bool] = None, save: Optional[bool] = None, file: Optional[ForwardRef('TypeInputFile')] = None, video: Optional[ForwardRef('TypeInputFile')] = None, video_start_ts: Optional[float] = None, video_emoji_markup: Optional[ForwardRef('TypeVideoSize')] = None)` |
| `UploadProfilePhotoRequest` | `photos.UploadProfilePhotoRequest` | `(self, fallback: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None, file: Optional[ForwardRef('TypeInputFile')] = None, video: Optional[ForwardRef('TypeInputFile')] = None, video_start_ts: Optional[float] = None, video_emoji_markup: Optional[ForwardRef('TypeVideoSize')] = None)` |

### `premium`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `ApplyBoostRequest` | `premium.ApplyBoostRequest` | `(self, peer: 'TypeInputPeer', slots: Optional[List[int]] = None)` |
| `GetBoostsListRequest` | `premium.GetBoostsListRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, gifts: Optional[bool] = None)` |
| `GetBoostsStatusRequest` | `premium.GetBoostsStatusRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetMyBoostsRequest` | `premium.GetMyBoostsRequest` | `(self, /, *args, **kwargs)` |
| `GetUserBoostsRequest` | `premium.GetUserBoostsRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser')` |

### `smsjobs`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `FinishJobRequest` | `smsjobs.FinishJobRequest` | `(self, job_id: str, error: Optional[str] = None)` |
| `GetSmsJobRequest` | `smsjobs.GetSmsJobRequest` | `(self, job_id: str)` |
| `GetStatusRequest` | `smsjobs.GetStatusRequest` | `(self, /, *args, **kwargs)` |
| `IsEligibleToJoinRequest` | `smsjobs.IsEligibleToJoinRequest` | `(self, /, *args, **kwargs)` |
| `JoinRequest` | `smsjobs.JoinRequest` | `(self, /, *args, **kwargs)` |
| `LeaveRequest` | `smsjobs.LeaveRequest` | `(self, /, *args, **kwargs)` |
| `UpdateSettingsRequest` | `smsjobs.UpdateSettingsRequest` | `(self, allow_international: Optional[bool] = None)` |

### `stats`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `GetBroadcastStatsRequest` | `stats.GetBroadcastStatsRequest` | `(self, channel: 'TypeInputChannel', dark: Optional[bool] = None)` |
| `GetMegagroupStatsRequest` | `stats.GetMegagroupStatsRequest` | `(self, channel: 'TypeInputChannel', dark: Optional[bool] = None)` |
| `GetMessagePublicForwardsRequest` | `stats.GetMessagePublicForwardsRequest` | `(self, channel: 'TypeInputChannel', msg_id: int, offset: str, limit: int)` |
| `GetMessageStatsRequest` | `stats.GetMessageStatsRequest` | `(self, channel: 'TypeInputChannel', msg_id: int, dark: Optional[bool] = None)` |
| `GetPollStatsRequest` | `stats.GetPollStatsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, dark: Optional[bool] = None)` |
| `GetStoryPublicForwardsRequest` | `stats.GetStoryPublicForwardsRequest` | `(self, peer: 'TypeInputPeer', id: int, offset: str, limit: int)` |
| `GetStoryStatsRequest` | `stats.GetStoryStatsRequest` | `(self, peer: 'TypeInputPeer', id: int, dark: Optional[bool] = None)` |
| `LoadAsyncGraphRequest` | `stats.LoadAsyncGraphRequest` | `(self, token: str, x: Optional[int] = None)` |

### `stickers`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `AddStickerToSetRequest` | `stickers.AddStickerToSetRequest` | `(self, stickerset: 'TypeInputStickerSet', sticker: 'TypeInputStickerSetItem')` |
| `ChangeStickerPositionRequest` | `stickers.ChangeStickerPositionRequest` | `(self, sticker: 'TypeInputDocument', position: int)` |
| `ChangeStickerRequest` | `stickers.ChangeStickerRequest` | `(self, sticker: 'TypeInputDocument', emoji: Optional[str] = None, mask_coords: Optional[ForwardRef('TypeMaskCoords')] = None, keywords: Optional[str] = None)` |
| `CheckShortNameRequest` | `stickers.CheckShortNameRequest` | `(self, short_name: str)` |
| `CreateStickerSetRequest` | `stickers.CreateStickerSetRequest` | `(self, user_id: 'TypeInputUser', title: str, short_name: str, stickers: List[ForwardRef('TypeInputStickerSetItem')], masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, thumb: Optional[ForwardRef('TypeInputDocument')] = None, software: Optional[str] = None)` |
| `DeleteStickerSetRequest` | `stickers.DeleteStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet')` |
| `RemoveStickerFromSetRequest` | `stickers.RemoveStickerFromSetRequest` | `(self, sticker: 'TypeInputDocument')` |
| `RenameStickerSetRequest` | `stickers.RenameStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', title: str)` |
| `ReplaceStickerRequest` | `stickers.ReplaceStickerRequest` | `(self, sticker: 'TypeInputDocument', new_sticker: 'TypeInputStickerSetItem')` |
| `SetStickerSetThumbRequest` | `stickers.SetStickerSetThumbRequest` | `(self, stickerset: 'TypeInputStickerSet', thumb: Optional[ForwardRef('TypeInputDocument')] = None, thumb_document_id: Optional[int] = None)` |
| `SuggestShortNameRequest` | `stickers.SuggestShortNameRequest` | `(self, title: str)` |

### `stories`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `ActivateStealthModeRequest` | `stories.ActivateStealthModeRequest` | `(self, past: Optional[bool] = None, future: Optional[bool] = None)` |
| `CanSendStoryRequest` | `stories.CanSendStoryRequest` | `(self, peer: 'TypeInputPeer')` |
| `CreateAlbumRequest` | `stories.CreateAlbumRequest` | `(self, peer: 'TypeInputPeer', title: str, stories: List[int])` |
| `DeleteAlbumRequest` | `stories.DeleteAlbumRequest` | `(self, peer: 'TypeInputPeer', album_id: int)` |
| `DeleteStoriesRequest` | `stories.DeleteStoriesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `EditStoryRequest` | `stories.EditStoryRequest` | `(self, peer: 'TypeInputPeer', id: int, media: Optional[ForwardRef('TypeInputMedia')] = None, media_areas: Optional[List[ForwardRef('TypeMediaArea')]] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, privacy_rules: Optional[List[ForwardRef('TypeInputPrivacyRule')]] = None, music: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `ExportStoryLinkRequest` | `stories.ExportStoryLinkRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `GetAlbumStoriesRequest` | `stories.GetAlbumStoriesRequest` | `(self, peer: 'TypeInputPeer', album_id: int, offset: int, limit: int)` |
| `GetAlbumsRequest` | `stories.GetAlbumsRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `GetAllReadPeerStoriesRequest` | `stories.GetAllReadPeerStoriesRequest` | `(self, /, *args, **kwargs)` |
| `GetAllStoriesRequest` | `stories.GetAllStoriesRequest` | `(self, next: Optional[bool] = None, hidden: Optional[bool] = None, state: Optional[str] = None)` |
| `GetChatsToSendRequest` | `stories.GetChatsToSendRequest` | `(self, /, *args, **kwargs)` |
| `GetPeerMaxIDsRequest` | `stories.GetPeerMaxIDsRequest` | `(self, id: List[ForwardRef('TypeInputPeer')])` |
| `GetPeerStoriesRequest` | `stories.GetPeerStoriesRequest` | `(self, peer: 'TypeInputPeer')` |
| `GetPinnedStoriesRequest` | `stories.GetPinnedStoriesRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, limit: int)` |
| `GetStoriesArchiveRequest` | `stories.GetStoriesArchiveRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, limit: int)` |
| `GetStoriesByIDRequest` | `stories.GetStoriesByIDRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `GetStoriesViewsRequest` | `stories.GetStoriesViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `GetStoryReactionsListRequest` | `stories.GetStoryReactionsListRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, forwards_first: Optional[bool] = None, reaction: Optional[ForwardRef('TypeReaction')] = None, offset: Optional[str] = None)` |
| `GetStoryViewsListRequest` | `stories.GetStoryViewsListRequest` | `(self, peer: 'TypeInputPeer', id: int, offset: str, limit: int, just_contacts: Optional[bool] = None, reactions_first: Optional[bool] = None, forwards_first: Optional[bool] = None, q: Optional[str] = None)` |
| `IncrementStoryViewsRequest` | `stories.IncrementStoryViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `ReadStoriesRequest` | `stories.ReadStoriesRequest` | `(self, peer: 'TypeInputPeer', max_id: int)` |
| `ReorderAlbumsRequest` | `stories.ReorderAlbumsRequest` | `(self, peer: 'TypeInputPeer', order: List[int])` |
| `ReportRequest` | `stories.ReportRequest` | `(self, peer: 'TypeInputPeer', id: List[int], option: bytes, message: str)` |
| `SearchPostsRequest` | `stories.SearchPostsRequest` | `(self, offset: str, limit: int, hashtag: Optional[str] = None, area: Optional[ForwardRef('TypeMediaArea')] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `SendReactionRequest` | `stories.SendReactionRequest` | `(self, peer: 'TypeInputPeer', story_id: int, reaction: 'TypeReaction', add_to_recent: Optional[bool] = None)` |
| `SendStoryRequest` | `stories.SendStoryRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', privacy_rules: List[ForwardRef('TypeInputPrivacyRule')], pinned: Optional[bool] = None, noforwards: Optional[bool] = None, fwd_modified: Optional[bool] = None, media_areas: Optional[List[ForwardRef('TypeMediaArea')]] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, random_id: int = None, period: Optional[int] = None, fwd_from_id: Optional[ForwardRef('TypeInputPeer')] = None, fwd_from_story: Optional[int] = None, albums: Optional[List[int]] = None, music: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `StartLiveRequest` | `stories.StartLiveRequest` | `(self, peer: 'TypeInputPeer', privacy_rules: List[ForwardRef('TypeInputPrivacyRule')], pinned: Optional[bool] = None, noforwards: Optional[bool] = None, rtmp_stream: Optional[bool] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, random_id: int = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None)` |
| `ToggleAllStoriesHiddenRequest` | `stories.ToggleAllStoriesHiddenRequest` | `(self, hidden: bool)` |
| `TogglePeerStoriesHiddenRequest` | `stories.TogglePeerStoriesHiddenRequest` | `(self, peer: 'TypeInputPeer', hidden: bool)` |
| `TogglePinnedRequest` | `stories.TogglePinnedRequest` | `(self, peer: 'TypeInputPeer', id: List[int], pinned: bool)` |
| `TogglePinnedToTopRequest` | `stories.TogglePinnedToTopRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `UpdateAlbumRequest` | `stories.UpdateAlbumRequest` | `(self, peer: 'TypeInputPeer', album_id: int, title: Optional[str] = None, delete_stories: Optional[List[int]] = None, add_stories: Optional[List[int]] = None, order: Optional[List[int]] = None)` |

### `updates`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `GetChannelDifferenceRequest` | `updates.GetChannelDifferenceRequest` | `(self, channel: 'TypeInputChannel', filter: 'TypeChannelMessagesFilter', pts: int, limit: int, force: Optional[bool] = None)` |
| `GetDifferenceRequest` | `updates.GetDifferenceRequest` | `(self, pts: int, date: Optional[datetime.datetime], qts: int, pts_limit: Optional[int] = None, pts_total_limit: Optional[int] = None, qts_limit: Optional[int] = None)` |
| `GetStateRequest` | `updates.GetStateRequest` | `(self, /, *args, **kwargs)` |

### `upload`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `GetCdnFileHashesRequest` | `upload.GetCdnFileHashesRequest` | `(self, file_token: bytes, offset: int)` |
| `GetCdnFileRequest` | `upload.GetCdnFileRequest` | `(self, file_token: bytes, offset: int, limit: int)` |
| `GetFileHashesRequest` | `upload.GetFileHashesRequest` | `(self, location: 'TypeInputFileLocation', offset: int)` |
| `GetFileRequest` | `upload.GetFileRequest` | `(self, location: 'TypeInputFileLocation', offset: int, limit: int, precise: Optional[bool] = None, cdn_supported: Optional[bool] = None)` |
| `GetWebFileRequest` | `upload.GetWebFileRequest` | `(self, location: 'TypeInputWebFileLocation', offset: int, limit: int)` |
| `ReuploadCdnFileRequest` | `upload.ReuploadCdnFileRequest` | `(self, file_token: bytes, request_token: bytes)` |
| `SaveBigFilePartRequest` | `upload.SaveBigFilePartRequest` | `(self, file_id: int, file_part: int, file_total_parts: int, bytes: bytes)` |
| `SaveFilePartRequest` | `upload.SaveFilePartRequest` | `(self, file_id: int, file_part: int, bytes: bytes)` |

### `users`

| Function | Callable Path | Constructor Signature |
|---|---|---|
| `GetFullUserRequest` | `users.GetFullUserRequest` | `(self, id: 'TypeInputUser')` |
| `GetRequirementsToContactRequest` | `users.GetRequirementsToContactRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `GetSavedMusicByIDRequest` | `users.GetSavedMusicByIDRequest` | `(self, id: 'TypeInputUser', documents: List[ForwardRef('TypeInputDocument')])` |
| `GetSavedMusicRequest` | `users.GetSavedMusicRequest` | `(self, id: 'TypeInputUser', offset: int, limit: int, hash: int)` |
| `GetUsersRequest` | `users.GetUsersRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `SetSecureValueErrorsRequest` | `users.SetSecureValueErrorsRequest` | `(self, id: 'TypeInputUser', errors: List[ForwardRef('TypeSecureValueError')])` |
| `SuggestBirthdayRequest` | `users.SuggestBirthdayRequest` | `(self, id: 'TypeInputUser', birthday: 'TypeBirthday')` |
