# Implemented MTProto Layer Functions

Source: `docs/mtproto-importance-layers.json`.
Layers: `1-10`.
Implemented functions: `779` / `779`.

All request-functions from importance layers 1-10 are implemented through the dynamic MTProto layer dispatcher. Individual functions are executed by callable_path with kwargs.

## Counts By Layer

| Layer | Implemented Functions |
|---:|---:|
| 1 | 248 |
| 2 | 189 |
| 3 | 104 |
| 4 | 49 |
| 5 | 26 |
| 6 | 72 |
| 7 | 54 |
| 8 | 24 |
| 9 | 0 |
| 10 | 13 |

## Endpoints

- `GET /mtproto/layers/{layer}/functions`
- `POST /mtproto/layers/{layer}/invoke`
- `POST /raw/invoke`
- `POST /rpc` with `method=raw.invoke`

## Functions

| Layer | Implemented | Namespace | Function | Callable Path | Signature |
|---:|---|---|---|---|---|
| `1` | `True` | `account` | `AcceptAuthorizationRequest` | `account.AcceptAuthorizationRequest` | `(self, bot_id: int, scope: str, public_key: str, value_hashes: List[ForwardRef('TypeSecureValueHash')], credentials: 'TypeSecureCredentialsEncrypted')` |
| `1` | `True` | `account` | `ChangeAuthorizationSettingsRequest` | `account.ChangeAuthorizationSettingsRequest` | `(self, hash: int, confirmed: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None)` |
| `1` | `True` | `account` | `CheckUsernameRequest` | `account.CheckUsernameRequest` | `(self, username: str)` |
| `1` | `True` | `account` | `CreateBusinessChatLinkRequest` | `account.CreateBusinessChatLinkRequest` | `(self, link: 'TypeInputBusinessChatLink')` |
| `1` | `True` | `account` | `DeleteBusinessChatLinkRequest` | `account.DeleteBusinessChatLinkRequest` | `(self, slug: str)` |
| `1` | `True` | `account` | `DisablePeerConnectedBotRequest` | `account.DisablePeerConnectedBotRequest` | `(self, peer: 'TypeInputPeer')` |
| `1` | `True` | `account` | `EditBusinessChatLinkRequest` | `account.EditBusinessChatLinkRequest` | `(self, slug: str, link: 'TypeInputBusinessChatLink')` |
| `1` | `True` | `account` | `GetAuthorizationFormRequest` | `account.GetAuthorizationFormRequest` | `(self, bot_id: int, scope: str, public_key: str)` |
| `1` | `True` | `account` | `GetAuthorizationsRequest` | `account.GetAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `account` | `GetBusinessChatLinksRequest` | `account.GetBusinessChatLinksRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `account` | `GetChannelDefaultEmojiStatusesRequest` | `account.GetChannelDefaultEmojiStatusesRequest` | `(self, hash: int)` |
| `1` | `True` | `account` | `GetChannelRestrictedStatusEmojisRequest` | `account.GetChannelRestrictedStatusEmojisRequest` | `(self, hash: int)` |
| `1` | `True` | `account` | `GetChatThemesRequest` | `account.GetChatThemesRequest` | `(self, hash: int)` |
| `1` | `True` | `account` | `GetPaidMessagesRevenueRequest` | `account.GetPaidMessagesRevenueRequest` | `(self, user_id: 'TypeInputUser', parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `account` | `GetUniqueGiftChatThemesRequest` | `account.GetUniqueGiftChatThemesRequest` | `(self, offset: str, limit: int, hash: int)` |
| `1` | `True` | `account` | `GetWebAuthorizationsRequest` | `account.GetWebAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `account` | `ReorderUsernamesRequest` | `account.ReorderUsernamesRequest` | `(self, order: List[str])` |
| `1` | `True` | `account` | `ReportPeerRequest` | `account.ReportPeerRequest` | `(self, peer: 'TypeInputPeer', reason: 'TypeReportReason', message: str)` |
| `1` | `True` | `account` | `ResetAuthorizationRequest` | `account.ResetAuthorizationRequest` | `(self, hash: int)` |
| `1` | `True` | `account` | `ResetWebAuthorizationRequest` | `account.ResetWebAuthorizationRequest` | `(self, hash: int)` |
| `1` | `True` | `account` | `ResetWebAuthorizationsRequest` | `account.ResetWebAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `account` | `ResolveBusinessChatLinkRequest` | `account.ResolveBusinessChatLinkRequest` | `(self, slug: str)` |
| `1` | `True` | `account` | `SetAuthorizationTTLRequest` | `account.SetAuthorizationTTLRequest` | `(self, authorization_ttl_days: int)` |
| `1` | `True` | `account` | `ToggleNoPaidMessagesExceptionRequest` | `account.ToggleNoPaidMessagesExceptionRequest` | `(self, user_id: 'TypeInputUser', refund_charged: Optional[bool] = None, require_payment: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `account` | `ToggleSponsoredMessagesRequest` | `account.ToggleSponsoredMessagesRequest` | `(self, enabled: bool)` |
| `1` | `True` | `account` | `ToggleUsernameRequest` | `account.ToggleUsernameRequest` | `(self, username: str, active: bool)` |
| `1` | `True` | `account` | `UpdateBirthdayRequest` | `account.UpdateBirthdayRequest` | `(self, birthday: Optional[ForwardRef('TypeBirthday')] = None)` |
| `1` | `True` | `account` | `UpdateBusinessAwayMessageRequest` | `account.UpdateBusinessAwayMessageRequest` | `(self, message: Optional[ForwardRef('TypeInputBusinessAwayMessage')] = None)` |
| `1` | `True` | `account` | `UpdateBusinessGreetingMessageRequest` | `account.UpdateBusinessGreetingMessageRequest` | `(self, message: Optional[ForwardRef('TypeInputBusinessGreetingMessage')] = None)` |
| `1` | `True` | `account` | `UpdateBusinessIntroRequest` | `account.UpdateBusinessIntroRequest` | `(self, intro: Optional[ForwardRef('TypeInputBusinessIntro')] = None)` |
| `1` | `True` | `account` | `UpdateBusinessLocationRequest` | `account.UpdateBusinessLocationRequest` | `(self, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None, address: Optional[str] = None)` |
| `1` | `True` | `account` | `UpdateBusinessWorkHoursRequest` | `account.UpdateBusinessWorkHoursRequest` | `(self, business_work_hours: Optional[ForwardRef('TypeBusinessWorkHours')] = None)` |
| `1` | `True` | `account` | `UpdateColorRequest` | `account.UpdateColorRequest` | `(self, for_profile: Optional[bool] = None, color: Optional[ForwardRef('TypePeerColor')] = None)` |
| `1` | `True` | `account` | `UpdateConnectedBotRequest` | `account.UpdateConnectedBotRequest` | `(self, bot: 'TypeInputUser', recipients: 'TypeInputBusinessBotRecipients', deleted: Optional[bool] = None, rights: Optional[ForwardRef('TypeBusinessBotRights')] = None)` |
| `1` | `True` | `account` | `UpdateDeviceLockedRequest` | `account.UpdateDeviceLockedRequest` | `(self, period: int)` |
| `1` | `True` | `account` | `UpdateEmojiStatusRequest` | `account.UpdateEmojiStatusRequest` | `(self, emoji_status: 'TypeEmojiStatus')` |
| `1` | `True` | `account` | `UpdateNotifySettingsRequest` | `account.UpdateNotifySettingsRequest` | `(self, peer: 'TypeInputNotifyPeer', settings: 'TypeInputPeerNotifySettings')` |
| `1` | `True` | `account` | `UpdatePasswordSettingsRequest` | `account.UpdatePasswordSettingsRequest` | `(self, password: 'TypeInputCheckPasswordSRP', new_settings: 'TypePasswordInputSettings')` |
| `1` | `True` | `account` | `UpdatePersonalChannelRequest` | `account.UpdatePersonalChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `1` | `True` | `account` | `UpdateProfileRequest` | `account.UpdateProfileRequest` | `(self, first_name: Optional[str] = None, last_name: Optional[str] = None, about: Optional[str] = None)` |
| `1` | `True` | `account` | `UpdateStatusRequest` | `account.UpdateStatusRequest` | `(self, offline: bool)` |
| `1` | `True` | `account` | `UpdateThemeRequest` | `account.UpdateThemeRequest` | `(self, format: str, theme: 'TypeInputTheme', slug: Optional[str] = None, title: Optional[str] = None, document: Optional[ForwardRef('TypeInputDocument')] = None, settings: Optional[List[ForwardRef('TypeInputThemeSettings')]] = None)` |
| `1` | `True` | `account` | `UpdateUsernameRequest` | `account.UpdateUsernameRequest` | `(self, username: str)` |
| `1` | `True` | `account` | `UpdateWebBrowserSettingsRequest` | `account.UpdateWebBrowserSettingsRequest` | `(self, open_external_browser: Optional[bool] = None, display_close_button: Optional[bool] = None)` |
| `1` | `True` | `aicompose` | `UpdateToneRequest` | `aicompose.UpdateToneRequest` | `(self, tone: 'TypeInputAiComposeTone', display_author: Optional[bool] = None, emoji_id: Optional[int] = None, title: Optional[str] = None, prompt: Optional[str] = None)` |
| `1` | `True` | `auth` | `AcceptLoginTokenRequest` | `auth.AcceptLoginTokenRequest` | `(self, token: bytes)` |
| `1` | `True` | `auth` | `BindTempAuthKeyRequest` | `auth.BindTempAuthKeyRequest` | `(self, perm_auth_key_id: int, nonce: int, expires_at: Optional[datetime.datetime], encrypted_message: bytes)` |
| `1` | `True` | `auth` | `CancelCodeRequest` | `auth.CancelCodeRequest` | `(self, phone_number: str, phone_code_hash: str)` |
| `1` | `True` | `auth` | `CheckPaidAuthRequest` | `auth.CheckPaidAuthRequest` | `(self, phone_number: str, phone_code_hash: str, form_id: int)` |
| `1` | `True` | `auth` | `CheckPasswordRequest` | `auth.CheckPasswordRequest` | `(self, password: 'TypeInputCheckPasswordSRP')` |
| `1` | `True` | `auth` | `CheckRecoveryPasswordRequest` | `auth.CheckRecoveryPasswordRequest` | `(self, code: str)` |
| `1` | `True` | `auth` | `DropTempAuthKeysRequest` | `auth.DropTempAuthKeysRequest` | `(self, except_auth_keys: List[int])` |
| `1` | `True` | `auth` | `ExportAuthorizationRequest` | `auth.ExportAuthorizationRequest` | `(self, dc_id: int)` |
| `1` | `True` | `auth` | `ExportLoginTokenRequest` | `auth.ExportLoginTokenRequest` | `(self, api_id: int, api_hash: str, except_ids: List[int])` |
| `1` | `True` | `auth` | `FinishPasskeyLoginRequest` | `auth.FinishPasskeyLoginRequest` | `(self, credential: 'TypeInputPasskeyCredential', from_dc_id: Optional[int] = None, from_auth_key_id: Optional[int] = None)` |
| `1` | `True` | `auth` | `ImportAuthorizationRequest` | `auth.ImportAuthorizationRequest` | `(self, id: int, bytes: bytes)` |
| `1` | `True` | `auth` | `ImportBotAuthorizationRequest` | `auth.ImportBotAuthorizationRequest` | `(self, flags: int, api_id: int, api_hash: str, bot_auth_token: str)` |
| `1` | `True` | `auth` | `ImportLoginTokenRequest` | `auth.ImportLoginTokenRequest` | `(self, token: bytes)` |
| `1` | `True` | `auth` | `ImportWebTokenAuthorizationRequest` | `auth.ImportWebTokenAuthorizationRequest` | `(self, api_id: int, api_hash: str, web_auth_token: str)` |
| `1` | `True` | `auth` | `InitPasskeyLoginRequest` | `auth.InitPasskeyLoginRequest` | `(self, api_id: int, api_hash: str)` |
| `1` | `True` | `auth` | `LogOutRequest` | `auth.LogOutRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `auth` | `RecoverPasswordRequest` | `auth.RecoverPasswordRequest` | `(self, code: str, new_settings: Optional[ForwardRef('TypePasswordInputSettings')] = None)` |
| `1` | `True` | `auth` | `ReportMissingCodeRequest` | `auth.ReportMissingCodeRequest` | `(self, phone_number: str, phone_code_hash: str, mnc: str)` |
| `1` | `True` | `auth` | `RequestFirebaseSmsRequest` | `auth.RequestFirebaseSmsRequest` | `(self, phone_number: str, phone_code_hash: str, safety_net_token: Optional[str] = None, play_integrity_token: Optional[str] = None, ios_push_secret: Optional[str] = None)` |
| `1` | `True` | `auth` | `RequestPasswordRecoveryRequest` | `auth.RequestPasswordRecoveryRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `auth` | `ResendCodeRequest` | `auth.ResendCodeRequest` | `(self, phone_number: str, phone_code_hash: str, reason: Optional[str] = None)` |
| `1` | `True` | `auth` | `ResetAuthorizationsRequest` | `auth.ResetAuthorizationsRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `auth` | `ResetLoginEmailRequest` | `auth.ResetLoginEmailRequest` | `(self, phone_number: str, phone_code_hash: str)` |
| `1` | `True` | `auth` | `SendCodeRequest` | `auth.SendCodeRequest` | `(self, phone_number: str, api_id: int, api_hash: str, settings: 'TypeCodeSettings')` |
| `1` | `True` | `auth` | `SignInRequest` | `auth.SignInRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: Optional[str] = None, email_verification: Optional[ForwardRef('TypeEmailVerification')] = None)` |
| `1` | `True` | `auth` | `SignUpRequest` | `auth.SignUpRequest` | `(self, phone_number: str, phone_code_hash: str, first_name: str, last_name: str, no_joined_notifications: Optional[bool] = None)` |
| `1` | `True` | `bots` | `AllowSendMessageRequest` | `bots.AllowSendMessageRequest` | `(self, bot: 'TypeInputUser')` |
| `1` | `True` | `bots` | `CanSendMessageRequest` | `bots.CanSendMessageRequest` | `(self, bot: 'TypeInputUser')` |
| `1` | `True` | `bots` | `CheckUsernameRequest` | `bots.CheckUsernameRequest` | `(self, username: str)` |
| `1` | `True` | `bots` | `ReorderUsernamesRequest` | `bots.ReorderUsernamesRequest` | `(self, bot: 'TypeInputUser', order: List[str])` |
| `1` | `True` | `bots` | `SetJoinChatResultsRequest` | `bots.SetJoinChatResultsRequest` | `(self, query_id: int, result: 'TypeJoinChatBotResult')` |
| `1` | `True` | `bots` | `ToggleUserEmojiStatusPermissionRequest` | `bots.ToggleUserEmojiStatusPermissionRequest` | `(self, bot: 'TypeInputUser', enabled: bool)` |
| `1` | `True` | `bots` | `ToggleUsernameRequest` | `bots.ToggleUsernameRequest` | `(self, bot: 'TypeInputUser', username: str, active: bool)` |
| `1` | `True` | `bots` | `UpdateStarRefProgramRequest` | `bots.UpdateStarRefProgramRequest` | `(self, bot: 'TypeInputUser', commission_permille: int, duration_months: Optional[int] = None)` |
| `1` | `True` | `bots` | `UpdateUserEmojiStatusRequest` | `bots.UpdateUserEmojiStatusRequest` | `(self, user_id: 'TypeInputUser', emoji_status: 'TypeEmojiStatus')` |
| `1` | `True` | `channels` | `CheckUsernameRequest` | `channels.CheckUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str)` |
| `1` | `True` | `channels` | `CreateChannelRequest` | `channels.CreateChannelRequest` | `(self, title: str, about: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, for_import: Optional[bool] = None, forum: Optional[bool] = None, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None, address: Optional[str] = None, ttl_period: Optional[int] = None)` |
| `1` | `True` | `channels` | `DeactivateAllUsernamesRequest` | `channels.DeactivateAllUsernamesRequest` | `(self, channel: 'TypeInputChannel')` |
| `1` | `True` | `channels` | `DeleteChannelRequest` | `channels.DeleteChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `1` | `True` | `channels` | `DeleteMessagesRequest` | `channels.DeleteMessagesRequest` | `(self, channel: 'TypeInputChannel', id: List[int])` |
| `1` | `True` | `channels` | `ExportMessageLinkRequest` | `channels.ExportMessageLinkRequest` | `(self, channel: 'TypeInputChannel', id: int, grouped: Optional[bool] = None, thread: Optional[bool] = None)` |
| `1` | `True` | `channels` | `GetAdminedPublicChannelsRequest` | `channels.GetAdminedPublicChannelsRequest` | `(self, by_location: Optional[bool] = None, check_limit: Optional[bool] = None, for_personal: Optional[bool] = None)` |
| `1` | `True` | `channels` | `GetChannelRecommendationsRequest` | `channels.GetChannelRecommendationsRequest` | `(self, channel: Optional[ForwardRef('TypeInputChannel')] = None)` |
| `1` | `True` | `channels` | `GetChannelsRequest` | `channels.GetChannelsRequest` | `(self, id: List[ForwardRef('TypeInputChannel')])` |
| `1` | `True` | `channels` | `GetFullChannelRequest` | `channels.GetFullChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `1` | `True` | `channels` | `GetInactiveChannelsRequest` | `channels.GetInactiveChannelsRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `channels` | `GetLeftChannelsRequest` | `channels.GetLeftChannelsRequest` | `(self, offset: int)` |
| `1` | `True` | `channels` | `GetMessageAuthorRequest` | `channels.GetMessageAuthorRequest` | `(self, channel: 'TypeInputChannel', id: int)` |
| `1` | `True` | `channels` | `GetMessagesRequest` | `channels.GetMessagesRequest` | `(self, channel: 'TypeInputChannel', id: List[ForwardRef('TypeInputMessage')])` |
| `1` | `True` | `channels` | `InviteToChannelRequest` | `channels.InviteToChannelRequest` | `(self, channel: 'TypeInputChannel', users: List[ForwardRef('TypeInputUser')])` |
| `1` | `True` | `channels` | `JoinChannelRequest` | `channels.JoinChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `1` | `True` | `channels` | `LeaveChannelRequest` | `channels.LeaveChannelRequest` | `(self, channel: 'TypeInputChannel')` |
| `1` | `True` | `channels` | `ReadMessageContentsRequest` | `channels.ReadMessageContentsRequest` | `(self, channel: 'TypeInputChannel', id: List[int])` |
| `1` | `True` | `channels` | `ReorderUsernamesRequest` | `channels.ReorderUsernamesRequest` | `(self, channel: 'TypeInputChannel', order: List[str])` |
| `1` | `True` | `channels` | `RestrictSponsoredMessagesRequest` | `channels.RestrictSponsoredMessagesRequest` | `(self, channel: 'TypeInputChannel', restricted: bool)` |
| `1` | `True` | `channels` | `ToggleUsernameRequest` | `channels.ToggleUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str, active: bool)` |
| `1` | `True` | `channels` | `ToggleViewForumAsMessagesRequest` | `channels.ToggleViewForumAsMessagesRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `1` | `True` | `channels` | `UpdateColorRequest` | `channels.UpdateColorRequest` | `(self, channel: 'TypeInputChannel', for_profile: Optional[bool] = None, color: Optional[int] = None, background_emoji_id: Optional[int] = None)` |
| `1` | `True` | `channels` | `UpdateEmojiStatusRequest` | `channels.UpdateEmojiStatusRequest` | `(self, channel: 'TypeInputChannel', emoji_status: 'TypeEmojiStatus')` |
| `1` | `True` | `channels` | `UpdatePaidMessagesPriceRequest` | `channels.UpdatePaidMessagesPriceRequest` | `(self, channel: 'TypeInputChannel', send_paid_messages_stars: int, broadcast_messages_allowed: Optional[bool] = None)` |
| `1` | `True` | `channels` | `UpdateUsernameRequest` | `channels.UpdateUsernameRequest` | `(self, channel: 'TypeInputChannel', username: str)` |
| `1` | `True` | `chatlists` | `CheckChatlistInviteRequest` | `chatlists.CheckChatlistInviteRequest` | `(self, slug: str)` |
| `1` | `True` | `chatlists` | `ExportChatlistInviteRequest` | `chatlists.ExportChatlistInviteRequest` | `(self, chatlist: 'TypeInputChatlist', title: str, peers: List[ForwardRef('TypeInputPeer')])` |
| `1` | `True` | `chatlists` | `GetChatlistUpdatesRequest` | `chatlists.GetChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `1` | `True` | `chatlists` | `GetLeaveChatlistSuggestionsRequest` | `chatlists.GetLeaveChatlistSuggestionsRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `1` | `True` | `chatlists` | `HideChatlistUpdatesRequest` | `chatlists.HideChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `1` | `True` | `chatlists` | `JoinChatlistInviteRequest` | `chatlists.JoinChatlistInviteRequest` | `(self, slug: str, peers: List[ForwardRef('TypeInputPeer')])` |
| `1` | `True` | `chatlists` | `JoinChatlistUpdatesRequest` | `chatlists.JoinChatlistUpdatesRequest` | `(self, chatlist: 'TypeInputChatlist', peers: List[ForwardRef('TypeInputPeer')])` |
| `1` | `True` | `chatlists` | `LeaveChatlistRequest` | `chatlists.LeaveChatlistRequest` | `(self, chatlist: 'TypeInputChatlist', peers: List[ForwardRef('TypeInputPeer')])` |
| `1` | `True` | `contacts` | `GetSponsoredPeersRequest` | `contacts.GetSponsoredPeersRequest` | `(self, q: str)` |
| `1` | `True` | `contacts` | `GetTopPeersRequest` | `contacts.GetTopPeersRequest` | `(self, offset: int, limit: int, hash: int, correspondents: Optional[bool] = None, bots_pm: Optional[bool] = None, bots_inline: Optional[bool] = None, phone_calls: Optional[bool] = None, forward_users: Optional[bool] = None, forward_chats: Optional[bool] = None, groups: Optional[bool] = None, channels: Optional[bool] = None, bots_app: Optional[bool] = None, bots_guestchat: Optional[bool] = None)` |
| `1` | `True` | `contacts` | `ResetTopPeerRatingRequest` | `contacts.ResetTopPeerRatingRequest` | `(self, category: 'TypeTopPeerCategory', peer: 'TypeInputPeer')` |
| `1` | `True` | `contacts` | `ResolveUsernameRequest` | `contacts.ResolveUsernameRequest` | `(self, username: str, referer: Optional[str] = None)` |
| `1` | `True` | `contacts` | `ToggleTopPeersRequest` | `contacts.ToggleTopPeersRequest` | `(self, enabled: bool)` |
| `1` | `True` | `contacts` | `UpdateContactNoteRequest` | `contacts.UpdateContactNoteRequest` | `(self, id: 'TypeInputUser', note: 'TypeTextWithEntities')` |
| `1` | `True` | `folders` | `EditPeerFoldersRequest` | `folders.EditPeerFoldersRequest` | `(self, folder_peers: List[ForwardRef('TypeInputFolderPeer')])` |
| `1` | `True` | `help` | `EditUserInfoRequest` | `help.EditUserInfoRequest` | `(self, user_id: 'TypeInputUser', message: str, entities: List[ForwardRef('TypeMessageEntity')])` |
| `1` | `True` | `help` | `GetAppUpdateRequest` | `help.GetAppUpdateRequest` | `(self, source: str)` |
| `1` | `True` | `help` | `GetPeerColorsRequest` | `help.GetPeerColorsRequest` | `(self, hash: int)` |
| `1` | `True` | `help` | `GetPeerProfileColorsRequest` | `help.GetPeerProfileColorsRequest` | `(self, hash: int)` |
| `1` | `True` | `help` | `GetTermsOfServiceUpdateRequest` | `help.GetTermsOfServiceUpdateRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `help` | `GetUserInfoRequest` | `help.GetUserInfoRequest` | `(self, user_id: 'TypeInputUser')` |
| `1` | `True` | `help` | `SetBotUpdatesStatusRequest` | `help.SetBotUpdatesStatusRequest` | `(self, pending_updates_count: int, message: str)` |
| `1` | `True` | `messages` | `AddChatUserRequest` | `messages.AddChatUserRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', fwd_limit: int)` |
| `1` | `True` | `messages` | `CheckChatInviteRequest` | `messages.CheckChatInviteRequest` | `(self, hash: str)` |
| `1` | `True` | `messages` | `CheckHistoryImportPeerRequest` | `messages.CheckHistoryImportPeerRequest` | `(self, peer: 'TypeInputPeer')` |
| `1` | `True` | `messages` | `ClickSponsoredMessageRequest` | `messages.ClickSponsoredMessageRequest` | `(self, media: Optional[bool] = None, fullscreen: Optional[bool] = None, random_id: bytes = None)` |
| `1` | `True` | `messages` | `ComposeMessageWithAIRequest` | `messages.ComposeMessageWithAIRequest` | `(self, text: 'TypeTextWithEntities', proofread: Optional[bool] = None, emojify: Optional[bool] = None, translate_to_lang: Optional[str] = None, tone: Optional[ForwardRef('TypeInputAiComposeTone')] = None)` |
| `1` | `True` | `messages` | `CreateChatRequest` | `messages.CreateChatRequest` | `(self, users: List[ForwardRef('TypeInputUser')], title: str, ttl_period: Optional[int] = None)` |
| `1` | `True` | `messages` | `DeleteChatRequest` | `messages.DeleteChatRequest` | `(self, chat_id: int)` |
| `1` | `True` | `messages` | `DeleteChatUserRequest` | `messages.DeleteChatUserRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', revoke_history: Optional[bool] = None)` |
| `1` | `True` | `messages` | `DeleteExportedChatInviteRequest` | `messages.DeleteExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str)` |
| `1` | `True` | `messages` | `DeleteMessagesRequest` | `messages.DeleteMessagesRequest` | `(self, id: List[int], revoke: Optional[bool] = None)` |
| `1` | `True` | `messages` | `DeleteQuickReplyMessagesRequest` | `messages.DeleteQuickReplyMessagesRequest` | `(self, shortcut_id: int, id: List[int])` |
| `1` | `True` | `messages` | `DeleteRevokedExportedChatInvitesRequest` | `messages.DeleteRevokedExportedChatInvitesRequest` | `(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser')` |
| `1` | `True` | `messages` | `DeleteScheduledMessagesRequest` | `messages.DeleteScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `1` | `True` | `messages` | `EditChatAboutRequest` | `messages.EditChatAboutRequest` | `(self, peer: 'TypeInputPeer', about: str)` |
| `1` | `True` | `messages` | `EditChatAdminRequest` | `messages.EditChatAdminRequest` | `(self, chat_id: int, user_id: 'TypeInputUser', is_admin: bool)` |
| `1` | `True` | `messages` | `EditChatCreatorRequest` | `messages.EditChatCreatorRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser', password: 'TypeInputCheckPasswordSRP')` |
| `1` | `True` | `messages` | `EditChatDefaultBannedRightsRequest` | `messages.EditChatDefaultBannedRightsRequest` | `(self, peer: 'TypeInputPeer', banned_rights: 'TypeChatBannedRights')` |
| `1` | `True` | `messages` | `EditChatParticipantRankRequest` | `messages.EditChatParticipantRankRequest` | `(self, peer: 'TypeInputPeer', participant: 'TypeInputPeer', rank: str)` |
| `1` | `True` | `messages` | `EditChatPhotoRequest` | `messages.EditChatPhotoRequest` | `(self, chat_id: int, photo: 'TypeInputChatPhoto')` |
| `1` | `True` | `messages` | `EditChatTitleRequest` | `messages.EditChatTitleRequest` | `(self, chat_id: int, title: str)` |
| `1` | `True` | `messages` | `EditExportedChatInviteRequest` | `messages.EditExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str, revoked: Optional[bool] = None, expire_date: Optional[datetime.datetime] = None, usage_limit: Optional[int] = None, request_needed: Optional[bool] = None, title: Optional[str] = None)` |
| `1` | `True` | `messages` | `EditInlineBotMessageRequest` | `messages.EditInlineBotMessageRequest` | `(self, id: 'TypeInputBotInlineMessageID', no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `1` | `True` | `messages` | `EditMessageRequest` | `messages.EditMessageRequest` | `(self, peer: 'TypeInputPeer', id: int, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, message: Optional[str] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, quick_reply_shortcut_id: Optional[int] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `1` | `True` | `messages` | `ExportChatInviteRequest` | `messages.ExportChatInviteRequest` | `(self, peer: 'TypeInputPeer', legacy_revoke_permanent: Optional[bool] = None, request_needed: Optional[bool] = None, expire_date: Optional[datetime.datetime] = None, usage_limit: Optional[int] = None, title: Optional[str] = None, subscription_pricing: Optional[ForwardRef('TypeStarsSubscriptionPricing')] = None)` |
| `1` | `True` | `messages` | `ForwardMessagesRequest` | `messages.ForwardMessagesRequest` | `(self, from_peer: 'TypeInputPeer', id: List[int], to_peer: 'TypeInputPeer', silent: Optional[bool] = None, background: Optional[bool] = None, with_my_score: Optional[bool] = None, drop_author: Optional[bool] = None, drop_media_captions: Optional[bool] = None, noforwards: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, random_id: List[int] = None, top_msg_id: Optional[int] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, video_timestamp: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None)` |
| `1` | `True` | `messages` | `GetChatInviteImportersRequest` | `messages.GetChatInviteImportersRequest` | `(self, peer: 'TypeInputPeer', offset_date: Optional[datetime.datetime], offset_user: 'TypeInputUser', limit: int, requested: Optional[bool] = None, subscription_expired: Optional[bool] = None, link: Optional[str] = None, q: Optional[str] = None)` |
| `1` | `True` | `messages` | `GetChatsRequest` | `messages.GetChatsRequest` | `(self, id: List[int])` |
| `1` | `True` | `messages` | `GetCommonChatsRequest` | `messages.GetCommonChatsRequest` | `(self, user_id: 'TypeInputUser', max_id: int, limit: int)` |
| `1` | `True` | `messages` | `GetDialogFiltersRequest` | `messages.GetDialogFiltersRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `messages` | `GetDialogUnreadMarksRequest` | `messages.GetDialogUnreadMarksRequest` | `(self, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `messages` | `GetDialogsRequest` | `messages.GetDialogsRequest` | `(self, offset_date: Optional[datetime.datetime], offset_id: int, offset_peer: 'TypeInputPeer', limit: int, hash: int, exclude_pinned: Optional[bool] = None, folder_id: Optional[int] = None)` |
| `1` | `True` | `messages` | `GetDiscussionMessageRequest` | `messages.GetDiscussionMessageRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `1` | `True` | `messages` | `GetExportedChatInviteRequest` | `messages.GetExportedChatInviteRequest` | `(self, peer: 'TypeInputPeer', link: str)` |
| `1` | `True` | `messages` | `GetExportedChatInvitesRequest` | `messages.GetExportedChatInvitesRequest` | `(self, peer: 'TypeInputPeer', admin_id: 'TypeInputUser', limit: int, revoked: Optional[bool] = None, offset_date: Optional[datetime.datetime] = None, offset_link: Optional[str] = None)` |
| `1` | `True` | `messages` | `GetFullChatRequest` | `messages.GetFullChatRequest` | `(self, chat_id: int)` |
| `1` | `True` | `messages` | `GetFutureChatCreatorAfterLeaveRequest` | `messages.GetFutureChatCreatorAfterLeaveRequest` | `(self, peer: 'TypeInputPeer')` |
| `1` | `True` | `messages` | `GetHistoryRequest` | `messages.GetHistoryRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int)` |
| `1` | `True` | `messages` | `GetMessageEditDataRequest` | `messages.GetMessageEditDataRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `1` | `True` | `messages` | `GetMessageReactionsListRequest` | `messages.GetMessageReactionsListRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, reaction: Optional[ForwardRef('TypeReaction')] = None, offset: Optional[str] = None)` |
| `1` | `True` | `messages` | `GetMessageReadParticipantsRequest` | `messages.GetMessageReadParticipantsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `1` | `True` | `messages` | `GetMessagesReactionsRequest` | `messages.GetMessagesReactionsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `1` | `True` | `messages` | `GetMessagesRequest` | `messages.GetMessagesRequest` | `(self, id: List[ForwardRef('TypeInputMessage')])` |
| `1` | `True` | `messages` | `GetMessagesViewsRequest` | `messages.GetMessagesViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int], increment: bool)` |
| `1` | `True` | `messages` | `GetPeerDialogsRequest` | `messages.GetPeerDialogsRequest` | `(self, peers: List[ForwardRef('TypeInputDialogPeer')])` |
| `1` | `True` | `messages` | `GetPeerSettingsRequest` | `messages.GetPeerSettingsRequest` | `(self, peer: 'TypeInputPeer')` |
| `1` | `True` | `messages` | `GetPersonalChannelHistoryRequest` | `messages.GetPersonalChannelHistoryRequest` | `(self, user_id: 'TypeInputUser', limit: int, max_id: int, min_id: int, hash: int)` |
| `1` | `True` | `messages` | `GetPinnedDialogsRequest` | `messages.GetPinnedDialogsRequest` | `(self, folder_id: int)` |
| `1` | `True` | `messages` | `GetPinnedSavedDialogsRequest` | `messages.GetPinnedSavedDialogsRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `messages` | `GetPreparedInlineMessageRequest` | `messages.GetPreparedInlineMessageRequest` | `(self, bot: 'TypeInputUser', id: str)` |
| `1` | `True` | `messages` | `GetQuickReplyMessagesRequest` | `messages.GetQuickReplyMessagesRequest` | `(self, shortcut_id: int, hash: int, id: Optional[List[int]] = None)` |
| `1` | `True` | `messages` | `GetRichMessageRequest` | `messages.GetRichMessageRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `1` | `True` | `messages` | `GetSavedDialogsByIDRequest` | `messages.GetSavedDialogsByIDRequest` | `(self, ids: List[ForwardRef('TypeInputPeer')], parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `messages` | `GetSavedDialogsRequest` | `messages.GetSavedDialogsRequest` | `(self, offset_date: Optional[datetime.datetime], offset_id: int, offset_peer: 'TypeInputPeer', limit: int, hash: int, exclude_pinned: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `messages` | `GetScheduledMessagesRequest` | `messages.GetScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `1` | `True` | `messages` | `GetSponsoredMessagesRequest` | `messages.GetSponsoredMessagesRequest` | `(self, peer: 'TypeInputPeer', msg_id: Optional[int] = None)` |
| `1` | `True` | `messages` | `GetSuggestedDialogFiltersRequest` | `messages.GetSuggestedDialogFiltersRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `messages` | `HideAllChatJoinRequestsRequest` | `messages.HideAllChatJoinRequestsRequest` | `(self, peer: 'TypeInputPeer', approved: Optional[bool] = None, link: Optional[str] = None)` |
| `1` | `True` | `messages` | `HideChatJoinRequestRequest` | `messages.HideChatJoinRequestRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser', approved: Optional[bool] = None)` |
| `1` | `True` | `messages` | `HidePeerSettingsBarRequest` | `messages.HidePeerSettingsBarRequest` | `(self, peer: 'TypeInputPeer')` |
| `1` | `True` | `messages` | `ImportChatInviteRequest` | `messages.ImportChatInviteRequest` | `(self, hash: str)` |
| `1` | `True` | `messages` | `MarkDialogUnreadRequest` | `messages.MarkDialogUnreadRequest` | `(self, peer: 'TypeInputDialogPeer', unread: Optional[bool] = None, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `messages` | `MigrateChatRequest` | `messages.MigrateChatRequest` | `(self, chat_id: int)` |
| `1` | `True` | `messages` | `ReadHistoryRequest` | `messages.ReadHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int)` |
| `1` | `True` | `messages` | `ReadMessageContentsRequest` | `messages.ReadMessageContentsRequest` | `(self, id: List[int])` |
| `1` | `True` | `messages` | `ReceivedMessagesRequest` | `messages.ReceivedMessagesRequest` | `(self, max_id: int)` |
| `1` | `True` | `messages` | `ReorderPinnedDialogsRequest` | `messages.ReorderPinnedDialogsRequest` | `(self, folder_id: int, order: List[ForwardRef('TypeInputDialogPeer')], force: Optional[bool] = None)` |
| `1` | `True` | `messages` | `ReorderPinnedSavedDialogsRequest` | `messages.ReorderPinnedSavedDialogsRequest` | `(self, order: List[ForwardRef('TypeInputDialogPeer')], force: Optional[bool] = None)` |
| `1` | `True` | `messages` | `ReportMessagesDeliveryRequest` | `messages.ReportMessagesDeliveryRequest` | `(self, peer: 'TypeInputPeer', id: List[int], push: Optional[bool] = None)` |
| `1` | `True` | `messages` | `ReportSponsoredMessageRequest` | `messages.ReportSponsoredMessageRequest` | `(self, option: bytes, random_id: bytes = None)` |
| `1` | `True` | `messages` | `SavePreparedInlineMessageRequest` | `messages.SavePreparedInlineMessageRequest` | `(self, result: 'TypeInputBotInlineResult', user_id: 'TypeInputUser', peer_types: Optional[List[ForwardRef('TypeInlineQueryPeerType')]] = None)` |
| `1` | `True` | `messages` | `SendBotRequestedPeerRequest` | `messages.SendBotRequestedPeerRequest` | `(self, peer: 'TypeInputPeer', button_id: int, requested_peers: List[ForwardRef('TypeInputPeer')], msg_id: Optional[int] = None, webapp_req_id: Optional[str] = None)` |
| `1` | `True` | `messages` | `SendMessageRequest` | `messages.SendMessageRequest` | `(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool] = None, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `1` | `True` | `messages` | `SendQuickReplyMessagesRequest` | `messages.SendQuickReplyMessagesRequest` | `(self, peer: 'TypeInputPeer', shortcut_id: int, id: List[int], random_id: List[int] = None)` |
| `1` | `True` | `messages` | `SendScheduledMessagesRequest` | `messages.SendScheduledMessagesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `1` | `True` | `messages` | `SendWebViewResultMessageRequest` | `messages.SendWebViewResultMessageRequest` | `(self, bot_query_id: str, result: 'TypeInputBotInlineResult')` |
| `1` | `True` | `messages` | `SetBotGuestChatResultRequest` | `messages.SetBotGuestChatResultRequest` | `(self, query_id: int, result: 'TypeInputBotInlineResult')` |
| `1` | `True` | `messages` | `SetChatAvailableReactionsRequest` | `messages.SetChatAvailableReactionsRequest` | `(self, peer: 'TypeInputPeer', available_reactions: 'TypeChatReactions', reactions_limit: Optional[int] = None, paid_enabled: Optional[bool] = None)` |
| `1` | `True` | `messages` | `SetChatThemeRequest` | `messages.SetChatThemeRequest` | `(self, peer: 'TypeInputPeer', theme: 'TypeInputChatTheme')` |
| `1` | `True` | `messages` | `SetChatWallPaperRequest` | `messages.SetChatWallPaperRequest` | `(self, peer: 'TypeInputPeer', for_both: Optional[bool] = None, revert: Optional[bool] = None, wallpaper: Optional[ForwardRef('TypeInputWallPaper')] = None, settings: Optional[ForwardRef('TypeWallPaperSettings')] = None, id: Optional[int] = None)` |
| `1` | `True` | `messages` | `ToggleDialogFilterTagsRequest` | `messages.ToggleDialogFilterTagsRequest` | `(self, enabled: bool)` |
| `1` | `True` | `messages` | `ToggleDialogPinRequest` | `messages.ToggleDialogPinRequest` | `(self, peer: 'TypeInputDialogPeer', pinned: Optional[bool] = None)` |
| `1` | `True` | `messages` | `TogglePeerTranslationsRequest` | `messages.TogglePeerTranslationsRequest` | `(self, peer: 'TypeInputPeer', disabled: Optional[bool] = None)` |
| `1` | `True` | `messages` | `ToggleSavedDialogPinRequest` | `messages.ToggleSavedDialogPinRequest` | `(self, peer: 'TypeInputDialogPeer', pinned: Optional[bool] = None)` |
| `1` | `True` | `messages` | `UnpinAllMessagesRequest` | `messages.UnpinAllMessagesRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `messages` | `UpdateDialogFilterRequest` | `messages.UpdateDialogFilterRequest` | `(self, id: int, filter: Optional[ForwardRef('TypeDialogFilter')] = None)` |
| `1` | `True` | `messages` | `UpdateDialogFiltersOrderRequest` | `messages.UpdateDialogFiltersOrderRequest` | `(self, order: List[int])` |
| `1` | `True` | `messages` | `UpdatePinnedForumTopicRequest` | `messages.UpdatePinnedForumTopicRequest` | `(self, peer: 'TypeInputPeer', topic_id: int, pinned: bool)` |
| `1` | `True` | `messages` | `UpdatePinnedMessageRequest` | `messages.UpdatePinnedMessageRequest` | `(self, peer: 'TypeInputPeer', id: int, silent: Optional[bool] = None, unpin: Optional[bool] = None, pm_oneside: Optional[bool] = None)` |
| `1` | `True` | `messages` | `UpdateSavedReactionTagRequest` | `messages.UpdateSavedReactionTagRequest` | `(self, reaction: 'TypeReaction', title: Optional[str] = None)` |
| `1` | `True` | `messages` | `ViewSponsoredMessageRequest` | `messages.ViewSponsoredMessageRequest` | `(self, random_id: bytes = None)` |
| `1` | `True` | `payments` | `ToggleChatStarGiftNotificationsRequest` | `payments.ToggleChatStarGiftNotificationsRequest` | `(self, peer: 'TypeInputPeer', enabled: Optional[bool] = None)` |
| `1` | `True` | `payments` | `UpdateStarGiftCollectionRequest` | `payments.UpdateStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', collection_id: int, title: Optional[str] = None, delete_stargift: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None, add_stargift: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None, order: Optional[List[ForwardRef('TypeInputSavedStarGift')]] = None)` |
| `1` | `True` | `payments` | `UpdateStarGiftPriceRequest` | `payments.UpdateStarGiftPriceRequest` | `(self, stargift: 'TypeInputSavedStarGift', resell_amount: 'TypeStarsAmount')` |
| `1` | `True` | `phone` | `DeleteGroupCallMessagesRequest` | `phone.DeleteGroupCallMessagesRequest` | `(self, call: 'TypeInputGroupCall', messages: List[int], report_spam: Optional[bool] = None)` |
| `1` | `True` | `phone` | `DeleteGroupCallParticipantMessagesRequest` | `phone.DeleteGroupCallParticipantMessagesRequest` | `(self, call: 'TypeInputGroupCall', participant: 'TypeInputPeer', report_spam: Optional[bool] = None)` |
| `1` | `True` | `phone` | `GetGroupCallStreamChannelsRequest` | `phone.GetGroupCallStreamChannelsRequest` | `(self, call: 'TypeInputGroupCall')` |
| `1` | `True` | `phone` | `SendGroupCallEncryptedMessageRequest` | `phone.SendGroupCallEncryptedMessageRequest` | `(self, call: 'TypeInputGroupCall', encrypted_message: bytes)` |
| `1` | `True` | `phone` | `SendGroupCallMessageRequest` | `phone.SendGroupCallMessageRequest` | `(self, call: 'TypeInputGroupCall', message: 'TypeTextWithEntities', random_id: int = None, allow_paid_stars: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `1` | `True` | `photos` | `GetUserPhotosRequest` | `photos.GetUserPhotosRequest` | `(self, user_id: 'TypeInputUser', offset: int, max_id: int, limit: int)` |
| `1` | `True` | `photos` | `UpdateProfilePhotoRequest` | `photos.UpdateProfilePhotoRequest` | `(self, id: 'TypeInputPhoto', fallback: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `1` | `True` | `premium` | `GetUserBoostsRequest` | `premium.GetUserBoostsRequest` | `(self, peer: 'TypeInputPeer', user_id: 'TypeInputUser')` |
| `1` | `True` | `smsjobs` | `UpdateSettingsRequest` | `smsjobs.UpdateSettingsRequest` | `(self, allow_international: Optional[bool] = None)` |
| `1` | `True` | `stats` | `GetMessagePublicForwardsRequest` | `stats.GetMessagePublicForwardsRequest` | `(self, channel: 'TypeInputChannel', msg_id: int, offset: str, limit: int)` |
| `1` | `True` | `stats` | `GetMessageStatsRequest` | `stats.GetMessageStatsRequest` | `(self, channel: 'TypeInputChannel', msg_id: int, dark: Optional[bool] = None)` |
| `1` | `True` | `stories` | `GetAllReadPeerStoriesRequest` | `stories.GetAllReadPeerStoriesRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `stories` | `GetChatsToSendRequest` | `stories.GetChatsToSendRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `stories` | `GetPeerMaxIDsRequest` | `stories.GetPeerMaxIDsRequest` | `(self, id: List[ForwardRef('TypeInputPeer')])` |
| `1` | `True` | `stories` | `GetPeerStoriesRequest` | `stories.GetPeerStoriesRequest` | `(self, peer: 'TypeInputPeer')` |
| `1` | `True` | `stories` | `TogglePeerStoriesHiddenRequest` | `stories.TogglePeerStoriesHiddenRequest` | `(self, peer: 'TypeInputPeer', hidden: bool)` |
| `1` | `True` | `stories` | `UpdateAlbumRequest` | `stories.UpdateAlbumRequest` | `(self, peer: 'TypeInputPeer', album_id: int, title: Optional[str] = None, delete_stories: Optional[List[int]] = None, add_stories: Optional[List[int]] = None, order: Optional[List[int]] = None)` |
| `1` | `True` | `updates` | `GetChannelDifferenceRequest` | `updates.GetChannelDifferenceRequest` | `(self, channel: 'TypeInputChannel', filter: 'TypeChannelMessagesFilter', pts: int, limit: int, force: Optional[bool] = None)` |
| `1` | `True` | `updates` | `GetDifferenceRequest` | `updates.GetDifferenceRequest` | `(self, pts: int, date: Optional[datetime.datetime], qts: int, pts_limit: Optional[int] = None, pts_total_limit: Optional[int] = None, qts_limit: Optional[int] = None)` |
| `1` | `True` | `updates` | `GetStateRequest` | `updates.GetStateRequest` | `(self, /, *args, **kwargs)` |
| `1` | `True` | `users` | `GetFullUserRequest` | `users.GetFullUserRequest` | `(self, id: 'TypeInputUser')` |
| `1` | `True` | `users` | `GetRequirementsToContactRequest` | `users.GetRequirementsToContactRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `1` | `True` | `users` | `GetSavedMusicByIDRequest` | `users.GetSavedMusicByIDRequest` | `(self, id: 'TypeInputUser', documents: List[ForwardRef('TypeInputDocument')])` |
| `1` | `True` | `users` | `GetSavedMusicRequest` | `users.GetSavedMusicRequest` | `(self, id: 'TypeInputUser', offset: int, limit: int, hash: int)` |
| `1` | `True` | `users` | `GetUsersRequest` | `users.GetUsersRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `1` | `True` | `users` | `SetSecureValueErrorsRequest` | `users.SetSecureValueErrorsRequest` | `(self, id: 'TypeInputUser', errors: List[ForwardRef('TypeSecureValueError')])` |
| `1` | `True` | `users` | `SuggestBirthdayRequest` | `users.SuggestBirthdayRequest` | `(self, id: 'TypeInputUser', birthday: 'TypeBirthday')` |
| `2` | `True` | `account` | `GetDefaultGroupPhotoEmojisRequest` | `account.GetDefaultGroupPhotoEmojisRequest` | `(self, hash: int)` |
| `2` | `True` | `account` | `GetDefaultProfilePhotoEmojisRequest` | `account.GetDefaultProfilePhotoEmojisRequest` | `(self, hash: int)` |
| `2` | `True` | `account` | `ReportProfilePhotoRequest` | `account.ReportProfilePhotoRequest` | `(self, peer: 'TypeInputPeer', photo_id: 'TypeInputPhoto', reason: 'TypeReportReason', message: str)` |
| `2` | `True` | `bots` | `AddPreviewMediaRequest` | `bots.AddPreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia')` |
| `2` | `True` | `bots` | `CheckDownloadFileParamsRequest` | `bots.CheckDownloadFileParamsRequest` | `(self, bot: 'TypeInputUser', file_name: str, url: str)` |
| `2` | `True` | `bots` | `DeletePreviewMediaRequest` | `bots.DeletePreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: List[ForwardRef('TypeInputMedia')])` |
| `2` | `True` | `bots` | `EditPreviewMediaRequest` | `bots.EditPreviewMediaRequest` | `(self, bot: 'TypeInputUser', lang_code: str, media: 'TypeInputMedia', new_media: 'TypeInputMedia')` |
| `2` | `True` | `bots` | `GetPreviewMediasRequest` | `bots.GetPreviewMediasRequest` | `(self, bot: 'TypeInputUser')` |
| `2` | `True` | `bots` | `ReorderPreviewMediasRequest` | `bots.ReorderPreviewMediasRequest` | `(self, bot: 'TypeInputUser', lang_code: str, order: List[ForwardRef('TypeInputMedia')])` |
| `2` | `True` | `channels` | `EditPhotoRequest` | `channels.EditPhotoRequest` | `(self, channel: 'TypeInputChannel', photo: 'TypeInputChatPhoto')` |
| `2` | `True` | `messages` | `AcceptEncryptionRequest` | `messages.AcceptEncryptionRequest` | `(self, peer: 'TypeInputEncryptedChat', g_b: bytes, key_fingerprint: int)` |
| `2` | `True` | `messages` | `AcceptUrlAuthRequest` | `messages.AcceptUrlAuthRequest` | `(self, write_allowed: Optional[bool] = None, share_phone_number: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None, match_code: Optional[str] = None)` |
| `2` | `True` | `messages` | `AddPollAnswerRequest` | `messages.AddPollAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, answer: 'TypePollAnswer')` |
| `2` | `True` | `messages` | `AppendTodoListRequest` | `messages.AppendTodoListRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, list: List[ForwardRef('TypeTodoItem')])` |
| `2` | `True` | `messages` | `CheckHistoryImportRequest` | `messages.CheckHistoryImportRequest` | `(self, import_head: str)` |
| `2` | `True` | `messages` | `CheckQuickReplyShortcutRequest` | `messages.CheckQuickReplyShortcutRequest` | `(self, shortcut: str)` |
| `2` | `True` | `messages` | `CheckUrlAuthMatchCodeRequest` | `messages.CheckUrlAuthMatchCodeRequest` | `(self, url: str, match_code: str)` |
| `2` | `True` | `messages` | `ClearAllDraftsRequest` | `messages.ClearAllDraftsRequest` | `(self, /, *args, **kwargs)` |
| `2` | `True` | `messages` | `ClearRecentReactionsRequest` | `messages.ClearRecentReactionsRequest` | `(self, /, *args, **kwargs)` |
| `2` | `True` | `messages` | `ClearRecentStickersRequest` | `messages.ClearRecentStickersRequest` | `(self, attached: Optional[bool] = None)` |
| `2` | `True` | `messages` | `CreateForumTopicRequest` | `messages.CreateForumTopicRequest` | `(self, peer: 'TypeInputPeer', title: str, title_missing: Optional[bool] = None, icon_color: Optional[int] = None, icon_emoji_id: Optional[int] = None, random_id: int = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `DeclineUrlAuthRequest` | `messages.DeclineUrlAuthRequest` | `(self, url: str)` |
| `2` | `True` | `messages` | `DeleteFactCheckRequest` | `messages.DeleteFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `2` | `True` | `messages` | `DeleteHistoryRequest` | `messages.DeleteHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int, just_clear: Optional[bool] = None, revoke: Optional[bool] = None, min_date: Optional[datetime.datetime] = None, max_date: Optional[datetime.datetime] = None)` |
| `2` | `True` | `messages` | `DeleteParticipantReactionRequest` | `messages.DeleteParticipantReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, participant: 'TypeInputPeer')` |
| `2` | `True` | `messages` | `DeleteParticipantReactionsRequest` | `messages.DeleteParticipantReactionsRequest` | `(self, peer: 'TypeInputPeer', participant: 'TypeInputPeer')` |
| `2` | `True` | `messages` | `DeletePhoneCallHistoryRequest` | `messages.DeletePhoneCallHistoryRequest` | `(self, revoke: Optional[bool] = None)` |
| `2` | `True` | `messages` | `DeletePollAnswerRequest` | `messages.DeletePollAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, option: bytes)` |
| `2` | `True` | `messages` | `DeleteQuickReplyShortcutRequest` | `messages.DeleteQuickReplyShortcutRequest` | `(self, shortcut_id: int)` |
| `2` | `True` | `messages` | `DeleteSavedHistoryRequest` | `messages.DeleteSavedHistoryRequest` | `(self, peer: 'TypeInputPeer', max_id: int, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None, min_date: Optional[datetime.datetime] = None, max_date: Optional[datetime.datetime] = None)` |
| `2` | `True` | `messages` | `DeleteTopicHistoryRequest` | `messages.DeleteTopicHistoryRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: int)` |
| `2` | `True` | `messages` | `DiscardEncryptionRequest` | `messages.DiscardEncryptionRequest` | `(self, chat_id: int, delete_history: Optional[bool] = None)` |
| `2` | `True` | `messages` | `EditFactCheckRequest` | `messages.EditFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, text: 'TypeTextWithEntities')` |
| `2` | `True` | `messages` | `EditForumTopicRequest` | `messages.EditForumTopicRequest` | `(self, peer: 'TypeInputPeer', topic_id: int, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None)` |
| `2` | `True` | `messages` | `EditQuickReplyShortcutRequest` | `messages.EditQuickReplyShortcutRequest` | `(self, shortcut_id: int, shortcut: str)` |
| `2` | `True` | `messages` | `FaveStickerRequest` | `messages.FaveStickerRequest` | `(self, id: 'TypeInputDocument', unfave: bool)` |
| `2` | `True` | `messages` | `GetAdminsWithInvitesRequest` | `messages.GetAdminsWithInvitesRequest` | `(self, peer: 'TypeInputPeer')` |
| `2` | `True` | `messages` | `GetAllDraftsRequest` | `messages.GetAllDraftsRequest` | `(self, /, *args, **kwargs)` |
| `2` | `True` | `messages` | `GetAllStickersRequest` | `messages.GetAllStickersRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetArchivedStickersRequest` | `messages.GetArchivedStickersRequest` | `(self, offset_id: int, limit: int, masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `2` | `True` | `messages` | `GetAttachMenuBotRequest` | `messages.GetAttachMenuBotRequest` | `(self, bot: 'TypeInputUser')` |
| `2` | `True` | `messages` | `GetAttachMenuBotsRequest` | `messages.GetAttachMenuBotsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetAttachedStickersRequest` | `messages.GetAttachedStickersRequest` | `(self, media: 'TypeInputStickeredMedia')` |
| `2` | `True` | `messages` | `GetAvailableEffectsRequest` | `messages.GetAvailableEffectsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetAvailableReactionsRequest` | `messages.GetAvailableReactionsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetBotAppRequest` | `messages.GetBotAppRequest` | `(self, app: 'TypeInputBotApp', hash: int)` |
| `2` | `True` | `messages` | `GetBotCallbackAnswerRequest` | `messages.GetBotCallbackAnswerRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, game: Optional[bool] = None, data: Optional[bytes] = None, password: Optional[ForwardRef('TypeInputCheckPasswordSRP')] = None)` |
| `2` | `True` | `messages` | `GetCustomEmojiDocumentsRequest` | `messages.GetCustomEmojiDocumentsRequest` | `(self, document_id: List[int])` |
| `2` | `True` | `messages` | `GetDefaultHistoryTTLRequest` | `messages.GetDefaultHistoryTTLRequest` | `(self, /, *args, **kwargs)` |
| `2` | `True` | `messages` | `GetDefaultTagReactionsRequest` | `messages.GetDefaultTagReactionsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetDhConfigRequest` | `messages.GetDhConfigRequest` | `(self, version: int, random_length: int)` |
| `2` | `True` | `messages` | `GetDocumentByHashRequest` | `messages.GetDocumentByHashRequest` | `(self, sha256: bytes, size: int, mime_type: str)` |
| `2` | `True` | `messages` | `GetEmojiGameInfoRequest` | `messages.GetEmojiGameInfoRequest` | `(self, /, *args, **kwargs)` |
| `2` | `True` | `messages` | `GetEmojiGroupsRequest` | `messages.GetEmojiGroupsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetEmojiKeywordsDifferenceRequest` | `messages.GetEmojiKeywordsDifferenceRequest` | `(self, lang_code: str, from_version: int)` |
| `2` | `True` | `messages` | `GetEmojiKeywordsLanguagesRequest` | `messages.GetEmojiKeywordsLanguagesRequest` | `(self, lang_codes: List[str])` |
| `2` | `True` | `messages` | `GetEmojiKeywordsRequest` | `messages.GetEmojiKeywordsRequest` | `(self, lang_code: str)` |
| `2` | `True` | `messages` | `GetEmojiProfilePhotoGroupsRequest` | `messages.GetEmojiProfilePhotoGroupsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetEmojiStatusGroupsRequest` | `messages.GetEmojiStatusGroupsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetEmojiStickerGroupsRequest` | `messages.GetEmojiStickerGroupsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetEmojiStickersRequest` | `messages.GetEmojiStickersRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetEmojiURLRequest` | `messages.GetEmojiURLRequest` | `(self, lang_code: str)` |
| `2` | `True` | `messages` | `GetExtendedMediaRequest` | `messages.GetExtendedMediaRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `2` | `True` | `messages` | `GetFactCheckRequest` | `messages.GetFactCheckRequest` | `(self, peer: 'TypeInputPeer', msg_id: List[int])` |
| `2` | `True` | `messages` | `GetFavedStickersRequest` | `messages.GetFavedStickersRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetFeaturedEmojiStickersRequest` | `messages.GetFeaturedEmojiStickersRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetFeaturedStickersRequest` | `messages.GetFeaturedStickersRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetForumTopicsByIDRequest` | `messages.GetForumTopicsByIDRequest` | `(self, peer: 'TypeInputPeer', topics: List[int])` |
| `2` | `True` | `messages` | `GetForumTopicsRequest` | `messages.GetForumTopicsRequest` | `(self, peer: 'TypeInputPeer', offset_date: Optional[datetime.datetime], offset_id: int, offset_topic: int, limit: int, q: Optional[str] = None)` |
| `2` | `True` | `messages` | `GetGameHighScoresRequest` | `messages.GetGameHighScoresRequest` | `(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser')` |
| `2` | `True` | `messages` | `GetInlineBotResultsRequest` | `messages.GetInlineBotResultsRequest` | `(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', query: str, offset: str, geo_point: Optional[ForwardRef('TypeInputGeoPoint')] = None)` |
| `2` | `True` | `messages` | `GetInlineGameHighScoresRequest` | `messages.GetInlineGameHighScoresRequest` | `(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser')` |
| `2` | `True` | `messages` | `GetMaskStickersRequest` | `messages.GetMaskStickersRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetMyStickersRequest` | `messages.GetMyStickersRequest` | `(self, offset_id: int, limit: int)` |
| `2` | `True` | `messages` | `GetOldFeaturedStickersRequest` | `messages.GetOldFeaturedStickersRequest` | `(self, offset: int, limit: int, hash: int)` |
| `2` | `True` | `messages` | `GetOnlinesRequest` | `messages.GetOnlinesRequest` | `(self, peer: 'TypeInputPeer')` |
| `2` | `True` | `messages` | `GetOutboxReadDateRequest` | `messages.GetOutboxReadDateRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `2` | `True` | `messages` | `GetPaidReactionPrivacyRequest` | `messages.GetPaidReactionPrivacyRequest` | `(self, /, *args, **kwargs)` |
| `2` | `True` | `messages` | `GetPollResultsRequest` | `messages.GetPollResultsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, poll_hash: int)` |
| `2` | `True` | `messages` | `GetPollVotesRequest` | `messages.GetPollVotesRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, option: Optional[bytes] = None, offset: Optional[str] = None)` |
| `2` | `True` | `messages` | `GetQuickRepliesRequest` | `messages.GetQuickRepliesRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetRecentLocationsRequest` | `messages.GetRecentLocationsRequest` | `(self, peer: 'TypeInputPeer', limit: int, hash: int)` |
| `2` | `True` | `messages` | `GetRecentReactionsRequest` | `messages.GetRecentReactionsRequest` | `(self, limit: int, hash: int)` |
| `2` | `True` | `messages` | `GetRecentStickersRequest` | `messages.GetRecentStickersRequest` | `(self, hash: int, attached: Optional[bool] = None)` |
| `2` | `True` | `messages` | `GetRepliesRequest` | `messages.GetRepliesRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int)` |
| `2` | `True` | `messages` | `GetSavedGifsRequest` | `messages.GetSavedGifsRequest` | `(self, hash: int)` |
| `2` | `True` | `messages` | `GetSavedHistoryRequest` | `messages.GetSavedHistoryRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, offset_date: Optional[datetime.datetime], add_offset: int, limit: int, max_id: int, min_id: int, hash: int, parent_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `GetSavedReactionTagsRequest` | `messages.GetSavedReactionTagsRequest` | `(self, hash: int, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `GetScheduledHistoryRequest` | `messages.GetScheduledHistoryRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `2` | `True` | `messages` | `GetSearchCountersRequest` | `messages.GetSearchCountersRequest` | `(self, peer: 'TypeInputPeer', filters: List[ForwardRef('TypeMessagesFilter')], saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, top_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `GetSearchResultsCalendarRequest` | `messages.GetSearchResultsCalendarRequest` | `(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, offset_date: Optional[datetime.datetime], saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `GetSearchResultsPositionsRequest` | `messages.GetSearchResultsPositionsRequest` | `(self, peer: 'TypeInputPeer', filter: 'TypeMessagesFilter', offset_id: int, limit: int, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `GetSplitRangesRequest` | `messages.GetSplitRangesRequest` | `(self, /, *args, **kwargs)` |
| `2` | `True` | `messages` | `GetStickerSetRequest` | `messages.GetStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', hash: int)` |
| `2` | `True` | `messages` | `GetStickersRequest` | `messages.GetStickersRequest` | `(self, emoticon: str, hash: int)` |
| `2` | `True` | `messages` | `GetTopReactionsRequest` | `messages.GetTopReactionsRequest` | `(self, limit: int, hash: int)` |
| `2` | `True` | `messages` | `GetUnreadMentionsRequest` | `messages.GetUnreadMentionsRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `GetUnreadPollVotesRequest` | `messages.GetUnreadPollVotesRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `GetUnreadReactionsRequest` | `messages.GetUnreadReactionsRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `GetWebPagePreviewRequest` | `messages.GetWebPagePreviewRequest` | `(self, message: str, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None)` |
| `2` | `True` | `messages` | `GetWebPageRequest` | `messages.GetWebPageRequest` | `(self, url: str, hash: int)` |
| `2` | `True` | `messages` | `InitHistoryImportRequest` | `messages.InitHistoryImportRequest` | `(self, peer: 'TypeInputPeer', file: 'TypeInputFile', media_count: int)` |
| `2` | `True` | `messages` | `InstallStickerSetRequest` | `messages.InstallStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', archived: bool)` |
| `2` | `True` | `messages` | `ProlongWebViewRequest` | `messages.ProlongWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', query_id: int, silent: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `RateTranscribedAudioRequest` | `messages.RateTranscribedAudioRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, transcription_id: int, good: bool)` |
| `2` | `True` | `messages` | `ReadDiscussionRequest` | `messages.ReadDiscussionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, read_max_id: int)` |
| `2` | `True` | `messages` | `ReadEncryptedHistoryRequest` | `messages.ReadEncryptedHistoryRequest` | `(self, peer: 'TypeInputEncryptedChat', max_date: Optional[datetime.datetime])` |
| `2` | `True` | `messages` | `ReadFeaturedStickersRequest` | `messages.ReadFeaturedStickersRequest` | `(self, id: List[int])` |
| `2` | `True` | `messages` | `ReadMentionsRequest` | `messages.ReadMentionsRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `ReadPollVotesRequest` | `messages.ReadPollVotesRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `ReadReactionsRequest` | `messages.ReadReactionsRequest` | `(self, peer: 'TypeInputPeer', top_msg_id: Optional[int] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `ReadSavedHistoryRequest` | `messages.ReadSavedHistoryRequest` | `(self, parent_peer: 'TypeInputPeer', peer: 'TypeInputPeer', max_id: int)` |
| `2` | `True` | `messages` | `ReceivedQueueRequest` | `messages.ReceivedQueueRequest` | `(self, max_qts: int)` |
| `2` | `True` | `messages` | `ReorderPinnedForumTopicsRequest` | `messages.ReorderPinnedForumTopicsRequest` | `(self, peer: 'TypeInputPeer', order: List[int], force: Optional[bool] = None)` |
| `2` | `True` | `messages` | `ReorderQuickRepliesRequest` | `messages.ReorderQuickRepliesRequest` | `(self, order: List[int])` |
| `2` | `True` | `messages` | `ReorderStickerSetsRequest` | `messages.ReorderStickerSetsRequest` | `(self, order: List[int], masks: Optional[bool] = None, emojis: Optional[bool] = None)` |
| `2` | `True` | `messages` | `ReportEncryptedSpamRequest` | `messages.ReportEncryptedSpamRequest` | `(self, peer: 'TypeInputEncryptedChat')` |
| `2` | `True` | `messages` | `ReportMusicListenRequest` | `messages.ReportMusicListenRequest` | `(self, id: 'TypeInputDocument', listened_duration: int)` |
| `2` | `True` | `messages` | `ReportReactionRequest` | `messages.ReportReactionRequest` | `(self, peer: 'TypeInputPeer', id: int, reaction_peer: 'TypeInputPeer')` |
| `2` | `True` | `messages` | `ReportReadMetricsRequest` | `messages.ReportReadMetricsRequest` | `(self, peer: 'TypeInputPeer', metrics: List[ForwardRef('TypeInputMessageReadMetric')])` |
| `2` | `True` | `messages` | `ReportRequest` | `messages.ReportRequest` | `(self, peer: 'TypeInputPeer', id: List[int], option: bytes, message: str)` |
| `2` | `True` | `messages` | `ReportSpamRequest` | `messages.ReportSpamRequest` | `(self, peer: 'TypeInputPeer')` |
| `2` | `True` | `messages` | `RequestAppWebViewRequest` | `messages.RequestAppWebViewRequest` | `(self, peer: 'TypeInputPeer', app: 'TypeInputBotApp', platform: str, write_allowed: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `2` | `True` | `messages` | `RequestEncryptionRequest` | `messages.RequestEncryptionRequest` | `(self, user_id: 'TypeInputUser', g_a: bytes, random_id: int = None)` |
| `2` | `True` | `messages` | `RequestMainWebViewRequest` | `messages.RequestMainWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', platform: str, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `2` | `True` | `messages` | `RequestSimpleWebViewRequest` | `messages.RequestSimpleWebViewRequest` | `(self, bot: 'TypeInputUser', platform: str, from_switch_webview: Optional[bool] = None, from_side_menu: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `2` | `True` | `messages` | `RequestUrlAuthRequest` | `messages.RequestUrlAuthRequest` | `(self, peer: Optional[ForwardRef('TypeInputPeer')] = None, msg_id: Optional[int] = None, button_id: Optional[int] = None, url: Optional[str] = None, in_app_origin: Optional[str] = None)` |
| `2` | `True` | `messages` | `RequestWebViewRequest` | `messages.RequestWebViewRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser', platform: str, from_bot_menu: Optional[bool] = None, silent: Optional[bool] = None, compact: Optional[bool] = None, fullscreen: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: Optional[ForwardRef('TypeDataJSON')] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `2` | `True` | `messages` | `SaveDefaultSendAsRequest` | `messages.SaveDefaultSendAsRequest` | `(self, peer: 'TypeInputPeer', send_as: 'TypeInputPeer')` |
| `2` | `True` | `messages` | `SaveDraftRequest` | `messages.SaveDraftRequest` | `(self, peer: 'TypeInputPeer', message: str, no_webpage: Optional[bool] = None, invert_media: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, media: Optional[ForwardRef('TypeInputMedia')] = None, effect: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None, rich_message: Optional[ForwardRef('TypeInputRichMessage')] = None)` |
| `2` | `True` | `messages` | `SaveGifRequest` | `messages.SaveGifRequest` | `(self, id: 'TypeInputDocument', unsave: bool)` |
| `2` | `True` | `messages` | `SaveRecentStickerRequest` | `messages.SaveRecentStickerRequest` | `(self, id: 'TypeInputDocument', unsave: bool, attached: Optional[bool] = None)` |
| `2` | `True` | `messages` | `SearchCustomEmojiRequest` | `messages.SearchCustomEmojiRequest` | `(self, emoticon: str, hash: int)` |
| `2` | `True` | `messages` | `SearchEmojiStickerSetsRequest` | `messages.SearchEmojiStickerSetsRequest` | `(self, q: str, hash: int, exclude_featured: Optional[bool] = None)` |
| `2` | `True` | `messages` | `SearchGlobalRequest` | `messages.SearchGlobalRequest` | `(self, q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime], offset_rate: int, offset_peer: 'TypeInputPeer', offset_id: int, limit: int, broadcasts_only: Optional[bool] = None, groups_only: Optional[bool] = None, users_only: Optional[bool] = None, folder_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `SearchRequest` | `messages.SearchRequest` | `(self, peer: 'TypeInputPeer', q: str, filter: 'TypeMessagesFilter', min_date: Optional[datetime.datetime], max_date: Optional[datetime.datetime], offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int, from_id: Optional[ForwardRef('TypeInputPeer')] = None, saved_peer_id: Optional[ForwardRef('TypeInputPeer')] = None, saved_reaction: Optional[List[ForwardRef('TypeReaction')]] = None, top_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `SearchSentMediaRequest` | `messages.SearchSentMediaRequest` | `(self, q: str, filter: 'TypeMessagesFilter', limit: int)` |
| `2` | `True` | `messages` | `SearchStickerSetsRequest` | `messages.SearchStickerSetsRequest` | `(self, q: str, hash: int, exclude_featured: Optional[bool] = None)` |
| `2` | `True` | `messages` | `SearchStickersRequest` | `messages.SearchStickersRequest` | `(self, q: str, emoticon: str, lang_code: List[str], offset: int, limit: int, hash: int, emojis: Optional[bool] = None)` |
| `2` | `True` | `messages` | `SendEncryptedFileRequest` | `messages.SendEncryptedFileRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, file: 'TypeInputEncryptedFile', silent: Optional[bool] = None, random_id: int = None)` |
| `2` | `True` | `messages` | `SendEncryptedRequest` | `messages.SendEncryptedRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, silent: Optional[bool] = None, random_id: int = None)` |
| `2` | `True` | `messages` | `SendEncryptedServiceRequest` | `messages.SendEncryptedServiceRequest` | `(self, peer: 'TypeInputEncryptedChat', data: bytes, random_id: int = None)` |
| `2` | `True` | `messages` | `SendInlineBotResultRequest` | `messages.SendInlineBotResultRequest` | `(self, peer: 'TypeInputPeer', query_id: int, id: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, hide_via: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, schedule_date: Optional[datetime.datetime] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, allow_paid_stars: Optional[int] = None)` |
| `2` | `True` | `messages` | `SendMediaRequest` | `messages.SendMediaRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', message: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, random_id: int = None, reply_markup: Optional[ForwardRef('TypeReplyMarkup')] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, schedule_date: Optional[datetime.datetime] = None, schedule_repeat_period: Optional[int] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None, suggested_post: Optional[ForwardRef('TypeSuggestedPost')] = None)` |
| `2` | `True` | `messages` | `SendMultiMediaRequest` | `messages.SendMultiMediaRequest` | `(self, peer: 'TypeInputPeer', multi_media: List[ForwardRef('TypeInputSingleMedia')], silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, noforwards: Optional[bool] = None, update_stickersets_order: Optional[bool] = None, invert_media: Optional[bool] = None, allow_paid_floodskip: Optional[bool] = None, reply_to: Optional[ForwardRef('TypeInputReplyTo')] = None, schedule_date: Optional[datetime.datetime] = None, send_as: Optional[ForwardRef('TypeInputPeer')] = None, quick_reply_shortcut: Optional[ForwardRef('TypeInputQuickReplyShortcut')] = None, effect: Optional[int] = None, allow_paid_stars: Optional[int] = None)` |
| `2` | `True` | `messages` | `SendPaidReactionRequest` | `messages.SendPaidReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, count: int, random_id: int = None, private: Optional[ForwardRef('TypePaidReactionPrivacy')] = None)` |
| `2` | `True` | `messages` | `SendReactionRequest` | `messages.SendReactionRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, big: Optional[bool] = None, add_to_recent: Optional[bool] = None, reaction: Optional[List[ForwardRef('TypeReaction')]] = None)` |
| `2` | `True` | `messages` | `SendScreenshotNotificationRequest` | `messages.SendScreenshotNotificationRequest` | `(self, peer: 'TypeInputPeer', reply_to: 'TypeInputReplyTo', random_id: int = None)` |
| `2` | `True` | `messages` | `SendVoteRequest` | `messages.SendVoteRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, options: List[bytes])` |
| `2` | `True` | `messages` | `SendWebViewDataRequest` | `messages.SendWebViewDataRequest` | `(self, bot: 'TypeInputUser', button_text: str, data: str, random_id: int = None)` |
| `2` | `True` | `messages` | `SetBotCallbackAnswerRequest` | `messages.SetBotCallbackAnswerRequest` | `(self, query_id: int, cache_time: int, alert: Optional[bool] = None, message: Optional[str] = None, url: Optional[str] = None)` |
| `2` | `True` | `messages` | `SetBotPrecheckoutResultsRequest` | `messages.SetBotPrecheckoutResultsRequest` | `(self, query_id: int, success: Optional[bool] = None, error: Optional[str] = None)` |
| `2` | `True` | `messages` | `SetBotShippingResultsRequest` | `messages.SetBotShippingResultsRequest` | `(self, query_id: int, error: Optional[str] = None, shipping_options: Optional[List[ForwardRef('TypeShippingOption')]] = None)` |
| `2` | `True` | `messages` | `SetDefaultHistoryTTLRequest` | `messages.SetDefaultHistoryTTLRequest` | `(self, period: int)` |
| `2` | `True` | `messages` | `SetDefaultReactionRequest` | `messages.SetDefaultReactionRequest` | `(self, reaction: 'TypeReaction')` |
| `2` | `True` | `messages` | `SetEncryptedTypingRequest` | `messages.SetEncryptedTypingRequest` | `(self, peer: 'TypeInputEncryptedChat', typing: bool)` |
| `2` | `True` | `messages` | `SetGameScoreRequest` | `messages.SetGameScoreRequest` | `(self, peer: 'TypeInputPeer', id: int, user_id: 'TypeInputUser', score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None)` |
| `2` | `True` | `messages` | `SetHistoryTTLRequest` | `messages.SetHistoryTTLRequest` | `(self, peer: 'TypeInputPeer', period: int)` |
| `2` | `True` | `messages` | `SetInlineBotResultsRequest` | `messages.SetInlineBotResultsRequest` | `(self, query_id: int, results: List[ForwardRef('TypeInputBotInlineResult')], cache_time: int, gallery: Optional[bool] = None, private: Optional[bool] = None, next_offset: Optional[str] = None, switch_pm: Optional[ForwardRef('TypeInlineBotSwitchPM')] = None, switch_webview: Optional[ForwardRef('TypeInlineBotWebView')] = None)` |
| `2` | `True` | `messages` | `SetInlineGameScoreRequest` | `messages.SetInlineGameScoreRequest` | `(self, id: 'TypeInputBotInlineMessageID', user_id: 'TypeInputUser', score: int, edit_message: Optional[bool] = None, force: Optional[bool] = None)` |
| `2` | `True` | `messages` | `SetTypingRequest` | `messages.SetTypingRequest` | `(self, peer: 'TypeInputPeer', action: 'TypeSendMessageAction', top_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `StartBotRequest` | `messages.StartBotRequest` | `(self, bot: 'TypeInputUser', peer: 'TypeInputPeer', start_param: str, random_id: int = None)` |
| `2` | `True` | `messages` | `StartHistoryImportRequest` | `messages.StartHistoryImportRequest` | `(self, peer: 'TypeInputPeer', import_id: int)` |
| `2` | `True` | `messages` | `SummarizeTextRequest` | `messages.SummarizeTextRequest` | `(self, peer: 'TypeInputPeer', id: int, to_lang: Optional[str] = None, tone: Optional[str] = None)` |
| `2` | `True` | `messages` | `ToggleBotInAttachMenuRequest` | `messages.ToggleBotInAttachMenuRequest` | `(self, bot: 'TypeInputUser', enabled: bool, write_allowed: Optional[bool] = None)` |
| `2` | `True` | `messages` | `ToggleNoForwardsRequest` | `messages.ToggleNoForwardsRequest` | `(self, peer: 'TypeInputPeer', enabled: bool, request_msg_id: Optional[int] = None)` |
| `2` | `True` | `messages` | `TogglePaidReactionPrivacyRequest` | `messages.TogglePaidReactionPrivacyRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, private: 'TypePaidReactionPrivacy')` |
| `2` | `True` | `messages` | `ToggleStickerSetsRequest` | `messages.ToggleStickerSetsRequest` | `(self, stickersets: List[ForwardRef('TypeInputStickerSet')], uninstall: Optional[bool] = None, archive: Optional[bool] = None, unarchive: Optional[bool] = None)` |
| `2` | `True` | `messages` | `ToggleSuggestedPostApprovalRequest` | `messages.ToggleSuggestedPostApprovalRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, reject: Optional[bool] = None, schedule_date: Optional[datetime.datetime] = None, reject_comment: Optional[str] = None)` |
| `2` | `True` | `messages` | `ToggleTodoCompletedRequest` | `messages.ToggleTodoCompletedRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, completed: List[int], incompleted: List[int])` |
| `2` | `True` | `messages` | `TranscribeAudioRequest` | `messages.TranscribeAudioRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `2` | `True` | `messages` | `TranslateTextRequest` | `messages.TranslateTextRequest` | `(self, to_lang: str, peer: Optional[ForwardRef('TypeInputPeer')] = None, id: Optional[List[int]] = None, text: Optional[List[ForwardRef('TypeTextWithEntities')]] = None, tone: Optional[str] = None)` |
| `2` | `True` | `messages` | `UninstallStickerSetRequest` | `messages.UninstallStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet')` |
| `2` | `True` | `messages` | `UploadEncryptedFileRequest` | `messages.UploadEncryptedFileRequest` | `(self, peer: 'TypeInputEncryptedChat', file: 'TypeInputEncryptedFile')` |
| `2` | `True` | `messages` | `UploadImportedMediaRequest` | `messages.UploadImportedMediaRequest` | `(self, peer: 'TypeInputPeer', import_id: int, file_name: str, media: 'TypeInputMedia')` |
| `2` | `True` | `messages` | `UploadMediaRequest` | `messages.UploadMediaRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', business_connection_id: Optional[str] = None)` |
| `2` | `True` | `photos` | `DeletePhotosRequest` | `photos.DeletePhotosRequest` | `(self, id: List[ForwardRef('TypeInputPhoto')])` |
| `2` | `True` | `photos` | `UploadContactProfilePhotoRequest` | `photos.UploadContactProfilePhotoRequest` | `(self, user_id: 'TypeInputUser', suggest: Optional[bool] = None, save: Optional[bool] = None, file: Optional[ForwardRef('TypeInputFile')] = None, video: Optional[ForwardRef('TypeInputFile')] = None, video_start_ts: Optional[float] = None, video_emoji_markup: Optional[ForwardRef('TypeVideoSize')] = None)` |
| `2` | `True` | `photos` | `UploadProfilePhotoRequest` | `photos.UploadProfilePhotoRequest` | `(self, fallback: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None, file: Optional[ForwardRef('TypeInputFile')] = None, video: Optional[ForwardRef('TypeInputFile')] = None, video_start_ts: Optional[float] = None, video_emoji_markup: Optional[ForwardRef('TypeVideoSize')] = None)` |
| `2` | `True` | `stats` | `GetPollStatsRequest` | `stats.GetPollStatsRequest` | `(self, peer: 'TypeInputPeer', msg_id: int, dark: Optional[bool] = None)` |
| `2` | `True` | `stats` | `GetStoryPublicForwardsRequest` | `stats.GetStoryPublicForwardsRequest` | `(self, peer: 'TypeInputPeer', id: int, offset: str, limit: int)` |
| `2` | `True` | `upload` | `GetCdnFileHashesRequest` | `upload.GetCdnFileHashesRequest` | `(self, file_token: bytes, offset: int)` |
| `2` | `True` | `upload` | `GetCdnFileRequest` | `upload.GetCdnFileRequest` | `(self, file_token: bytes, offset: int, limit: int)` |
| `2` | `True` | `upload` | `GetFileHashesRequest` | `upload.GetFileHashesRequest` | `(self, location: 'TypeInputFileLocation', offset: int)` |
| `2` | `True` | `upload` | `GetFileRequest` | `upload.GetFileRequest` | `(self, location: 'TypeInputFileLocation', offset: int, limit: int, precise: Optional[bool] = None, cdn_supported: Optional[bool] = None)` |
| `2` | `True` | `upload` | `GetWebFileRequest` | `upload.GetWebFileRequest` | `(self, location: 'TypeInputWebFileLocation', offset: int, limit: int)` |
| `2` | `True` | `upload` | `ReuploadCdnFileRequest` | `upload.ReuploadCdnFileRequest` | `(self, file_token: bytes, request_token: bytes)` |
| `2` | `True` | `upload` | `SaveBigFilePartRequest` | `upload.SaveBigFilePartRequest` | `(self, file_id: int, file_part: int, file_total_parts: int, bytes: bytes)` |
| `2` | `True` | `upload` | `SaveFilePartRequest` | `upload.SaveFilePartRequest` | `(self, file_id: int, file_part: int, bytes: bytes)` |
| `3` | `True` | `account` | `CancelPasswordEmailRequest` | `account.CancelPasswordEmailRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `ChangePhoneRequest` | `account.ChangePhoneRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: str)` |
| `3` | `True` | `account` | `ClearRecentEmojiStatusesRequest` | `account.ClearRecentEmojiStatusesRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `ConfirmBotConnectionRequest` | `account.ConfirmBotConnectionRequest` | `(self, bot_id: 'TypeInputUser')` |
| `3` | `True` | `account` | `ConfirmPasswordEmailRequest` | `account.ConfirmPasswordEmailRequest` | `(self, code: str)` |
| `3` | `True` | `account` | `ConfirmPhoneRequest` | `account.ConfirmPhoneRequest` | `(self, phone_code_hash: str, phone_code: str)` |
| `3` | `True` | `account` | `CreateThemeRequest` | `account.CreateThemeRequest` | `(self, slug: str, title: str, document: Optional[ForwardRef('TypeInputDocument')] = None, settings: Optional[List[ForwardRef('TypeInputThemeSettings')]] = None)` |
| `3` | `True` | `account` | `DeclinePasswordResetRequest` | `account.DeclinePasswordResetRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `DeleteAccountRequest` | `account.DeleteAccountRequest` | `(self, reason: str, password: Optional[ForwardRef('TypeInputCheckPasswordSRP')] = None)` |
| `3` | `True` | `account` | `DeleteAutoSaveExceptionsRequest` | `account.DeleteAutoSaveExceptionsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `DeletePasskeyRequest` | `account.DeletePasskeyRequest` | `(self, id: str)` |
| `3` | `True` | `account` | `DeleteSecureValueRequest` | `account.DeleteSecureValueRequest` | `(self, types: List[ForwardRef('TypeSecureValueType')])` |
| `3` | `True` | `account` | `DeleteWebBrowserSettingsExceptionsRequest` | `account.DeleteWebBrowserSettingsExceptionsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `FinishTakeoutSessionRequest` | `account.FinishTakeoutSessionRequest` | `(self, success: Optional[bool] = None)` |
| `3` | `True` | `account` | `GetAccountTTLRequest` | `account.GetAccountTTLRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetAllSecureValuesRequest` | `account.GetAllSecureValuesRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetAutoDownloadSettingsRequest` | `account.GetAutoDownloadSettingsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetAutoSaveSettingsRequest` | `account.GetAutoSaveSettingsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetBotBusinessConnectionRequest` | `account.GetBotBusinessConnectionRequest` | `(self, connection_id: str)` |
| `3` | `True` | `account` | `GetCollectibleEmojiStatusesRequest` | `account.GetCollectibleEmojiStatusesRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `GetConnectedBotsRequest` | `account.GetConnectedBotsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetContactSignUpNotificationRequest` | `account.GetContactSignUpNotificationRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetContentSettingsRequest` | `account.GetContentSettingsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetDefaultBackgroundEmojisRequest` | `account.GetDefaultBackgroundEmojisRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `GetDefaultEmojiStatusesRequest` | `account.GetDefaultEmojiStatusesRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `GetGlobalPrivacySettingsRequest` | `account.GetGlobalPrivacySettingsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetMultiWallPapersRequest` | `account.GetMultiWallPapersRequest` | `(self, wallpapers: List[ForwardRef('TypeInputWallPaper')])` |
| `3` | `True` | `account` | `GetNotifyExceptionsRequest` | `account.GetNotifyExceptionsRequest` | `(self, compare_sound: Optional[bool] = None, compare_stories: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputNotifyPeer')] = None)` |
| `3` | `True` | `account` | `GetNotifySettingsRequest` | `account.GetNotifySettingsRequest` | `(self, peer: 'TypeInputNotifyPeer')` |
| `3` | `True` | `account` | `GetPasskeysRequest` | `account.GetPasskeysRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetPasswordRequest` | `account.GetPasswordRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetPasswordSettingsRequest` | `account.GetPasswordSettingsRequest` | `(self, password: 'TypeInputCheckPasswordSRP')` |
| `3` | `True` | `account` | `GetPrivacyRequest` | `account.GetPrivacyRequest` | `(self, key: 'TypeInputPrivacyKey')` |
| `3` | `True` | `account` | `GetReactionsNotifySettingsRequest` | `account.GetReactionsNotifySettingsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `GetRecentEmojiStatusesRequest` | `account.GetRecentEmojiStatusesRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `GetSavedMusicIdsRequest` | `account.GetSavedMusicIdsRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `GetSavedRingtonesRequest` | `account.GetSavedRingtonesRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `GetSecureValueRequest` | `account.GetSecureValueRequest` | `(self, types: List[ForwardRef('TypeSecureValueType')])` |
| `3` | `True` | `account` | `GetThemeRequest` | `account.GetThemeRequest` | `(self, format: str, theme: 'TypeInputTheme')` |
| `3` | `True` | `account` | `GetThemesRequest` | `account.GetThemesRequest` | `(self, format: str, hash: int)` |
| `3` | `True` | `account` | `GetTmpPasswordRequest` | `account.GetTmpPasswordRequest` | `(self, password: 'TypeInputCheckPasswordSRP', period: int)` |
| `3` | `True` | `account` | `GetWallPaperRequest` | `account.GetWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper')` |
| `3` | `True` | `account` | `GetWallPapersRequest` | `account.GetWallPapersRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `GetWebBrowserSettingsRequest` | `account.GetWebBrowserSettingsRequest` | `(self, hash: int)` |
| `3` | `True` | `account` | `InitPasskeyRegistrationRequest` | `account.InitPasskeyRegistrationRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `InitTakeoutSessionRequest` | `account.InitTakeoutSessionRequest` | `(self, contacts: Optional[bool] = None, message_users: Optional[bool] = None, message_chats: Optional[bool] = None, message_megagroups: Optional[bool] = None, message_channels: Optional[bool] = None, files: Optional[bool] = None, file_max_size: Optional[int] = None)` |
| `3` | `True` | `account` | `InstallThemeRequest` | `account.InstallThemeRequest` | `(self, dark: Optional[bool] = None, theme: Optional[ForwardRef('TypeInputTheme')] = None, format: Optional[str] = None, base_theme: Optional[ForwardRef('TypeBaseTheme')] = None)` |
| `3` | `True` | `account` | `InstallWallPaperRequest` | `account.InstallWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper', settings: 'TypeWallPaperSettings')` |
| `3` | `True` | `account` | `InvalidateSignInCodesRequest` | `account.InvalidateSignInCodesRequest` | `(self, codes: List[str])` |
| `3` | `True` | `account` | `RegisterDeviceRequest` | `account.RegisterDeviceRequest` | `(self, token_type: int, token: str, app_sandbox: bool, secret: bytes, other_uids: List[int], no_muted: Optional[bool] = None)` |
| `3` | `True` | `account` | `RegisterPasskeyRequest` | `account.RegisterPasskeyRequest` | `(self, credential: 'TypeInputPasskeyCredential')` |
| `3` | `True` | `account` | `ResendPasswordEmailRequest` | `account.ResendPasswordEmailRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `ResetNotifySettingsRequest` | `account.ResetNotifySettingsRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `ResetPasswordRequest` | `account.ResetPasswordRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `ResetWallPapersRequest` | `account.ResetWallPapersRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `account` | `SaveAutoDownloadSettingsRequest` | `account.SaveAutoDownloadSettingsRequest` | `(self, settings: 'TypeAutoDownloadSettings', low: Optional[bool] = None, high: Optional[bool] = None)` |
| `3` | `True` | `account` | `SaveAutoSaveSettingsRequest` | `account.SaveAutoSaveSettingsRequest` | `(self, settings: 'TypeAutoSaveSettings', users: Optional[bool] = None, chats: Optional[bool] = None, broadcasts: Optional[bool] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `3` | `True` | `account` | `SaveMusicRequest` | `account.SaveMusicRequest` | `(self, id: 'TypeInputDocument', unsave: Optional[bool] = None, after_id: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `3` | `True` | `account` | `SaveRingtoneRequest` | `account.SaveRingtoneRequest` | `(self, id: 'TypeInputDocument', unsave: bool)` |
| `3` | `True` | `account` | `SaveSecureValueRequest` | `account.SaveSecureValueRequest` | `(self, value: 'TypeInputSecureValue', secure_secret_id: int)` |
| `3` | `True` | `account` | `SaveThemeRequest` | `account.SaveThemeRequest` | `(self, theme: 'TypeInputTheme', unsave: bool)` |
| `3` | `True` | `account` | `SaveWallPaperRequest` | `account.SaveWallPaperRequest` | `(self, wallpaper: 'TypeInputWallPaper', unsave: bool, settings: 'TypeWallPaperSettings')` |
| `3` | `True` | `account` | `SendChangePhoneCodeRequest` | `account.SendChangePhoneCodeRequest` | `(self, phone_number: str, settings: 'TypeCodeSettings')` |
| `3` | `True` | `account` | `SendConfirmPhoneCodeRequest` | `account.SendConfirmPhoneCodeRequest` | `(self, hash: str, settings: 'TypeCodeSettings')` |
| `3` | `True` | `account` | `SendVerifyEmailCodeRequest` | `account.SendVerifyEmailCodeRequest` | `(self, purpose: 'TypeEmailVerifyPurpose', email: str)` |
| `3` | `True` | `account` | `SendVerifyPhoneCodeRequest` | `account.SendVerifyPhoneCodeRequest` | `(self, phone_number: str, settings: 'TypeCodeSettings')` |
| `3` | `True` | `account` | `SetAccountTTLRequest` | `account.SetAccountTTLRequest` | `(self, ttl: 'TypeAccountDaysTTL')` |
| `3` | `True` | `account` | `SetContactSignUpNotificationRequest` | `account.SetContactSignUpNotificationRequest` | `(self, silent: bool)` |
| `3` | `True` | `account` | `SetContentSettingsRequest` | `account.SetContentSettingsRequest` | `(self, sensitive_enabled: Optional[bool] = None)` |
| `3` | `True` | `account` | `SetGlobalPrivacySettingsRequest` | `account.SetGlobalPrivacySettingsRequest` | `(self, settings: 'TypeGlobalPrivacySettings')` |
| `3` | `True` | `account` | `SetMainProfileTabRequest` | `account.SetMainProfileTabRequest` | `(self, tab: 'TypeProfileTab')` |
| `3` | `True` | `account` | `SetPrivacyRequest` | `account.SetPrivacyRequest` | `(self, key: 'TypeInputPrivacyKey', rules: List[ForwardRef('TypeInputPrivacyRule')])` |
| `3` | `True` | `account` | `SetReactionsNotifySettingsRequest` | `account.SetReactionsNotifySettingsRequest` | `(self, settings: 'TypeReactionsNotifySettings')` |
| `3` | `True` | `account` | `ToggleConnectedBotPausedRequest` | `account.ToggleConnectedBotPausedRequest` | `(self, peer: 'TypeInputPeer', paused: bool)` |
| `3` | `True` | `account` | `ToggleWebBrowserSettingsExceptionRequest` | `account.ToggleWebBrowserSettingsExceptionRequest` | `(self, url: str, delete: Optional[bool] = None, open_external_browser: Optional[bool] = None)` |
| `3` | `True` | `account` | `UnregisterDeviceRequest` | `account.UnregisterDeviceRequest` | `(self, token_type: int, token: str, other_uids: List[int])` |
| `3` | `True` | `account` | `UploadRingtoneRequest` | `account.UploadRingtoneRequest` | `(self, file: 'TypeInputFile', file_name: str, mime_type: str)` |
| `3` | `True` | `account` | `UploadThemeRequest` | `account.UploadThemeRequest` | `(self, file: 'TypeInputFile', file_name: str, mime_type: str, thumb: Optional[ForwardRef('TypeInputFile')] = None)` |
| `3` | `True` | `account` | `UploadWallPaperRequest` | `account.UploadWallPaperRequest` | `(self, file: 'TypeInputFile', mime_type: str, settings: 'TypeWallPaperSettings', for_chat: Optional[bool] = None)` |
| `3` | `True` | `account` | `VerifyEmailRequest` | `account.VerifyEmailRequest` | `(self, purpose: 'TypeEmailVerifyPurpose', verification: 'TypeEmailVerification')` |
| `3` | `True` | `account` | `VerifyPhoneRequest` | `account.VerifyPhoneRequest` | `(self, phone_number: str, phone_code_hash: str, phone_code: str)` |
| `3` | `True` | `contacts` | `AcceptContactRequest` | `contacts.AcceptContactRequest` | `(self, id: 'TypeInputUser')` |
| `3` | `True` | `contacts` | `AddContactRequest` | `contacts.AddContactRequest` | `(self, id: 'TypeInputUser', first_name: str, last_name: str, phone: str, add_phone_privacy_exception: Optional[bool] = None, note: Optional[ForwardRef('TypeTextWithEntities')] = None)` |
| `3` | `True` | `contacts` | `BlockFromRepliesRequest` | `contacts.BlockFromRepliesRequest` | `(self, msg_id: int, delete_message: Optional[bool] = None, delete_history: Optional[bool] = None, report_spam: Optional[bool] = None)` |
| `3` | `True` | `contacts` | `BlockRequest` | `contacts.BlockRequest` | `(self, id: 'TypeInputPeer', my_stories_from: Optional[bool] = None)` |
| `3` | `True` | `contacts` | `DeleteByPhonesRequest` | `contacts.DeleteByPhonesRequest` | `(self, phones: List[str])` |
| `3` | `True` | `contacts` | `DeleteContactsRequest` | `contacts.DeleteContactsRequest` | `(self, id: List[ForwardRef('TypeInputUser')])` |
| `3` | `True` | `contacts` | `EditCloseFriendsRequest` | `contacts.EditCloseFriendsRequest` | `(self, id: List[int])` |
| `3` | `True` | `contacts` | `ExportContactTokenRequest` | `contacts.ExportContactTokenRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `contacts` | `GetBirthdaysRequest` | `contacts.GetBirthdaysRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `contacts` | `GetBlockedRequest` | `contacts.GetBlockedRequest` | `(self, offset: int, limit: int, my_stories_from: Optional[bool] = None)` |
| `3` | `True` | `contacts` | `GetContactIDsRequest` | `contacts.GetContactIDsRequest` | `(self, hash: int)` |
| `3` | `True` | `contacts` | `GetContactsRequest` | `contacts.GetContactsRequest` | `(self, hash: int)` |
| `3` | `True` | `contacts` | `GetLocatedRequest` | `contacts.GetLocatedRequest` | `(self, geo_point: 'TypeInputGeoPoint', background: Optional[bool] = None, self_expires: Optional[int] = None)` |
| `3` | `True` | `contacts` | `GetSavedRequest` | `contacts.GetSavedRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `contacts` | `GetStatusesRequest` | `contacts.GetStatusesRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `contacts` | `ImportContactTokenRequest` | `contacts.ImportContactTokenRequest` | `(self, token: str)` |
| `3` | `True` | `contacts` | `ImportContactsRequest` | `contacts.ImportContactsRequest` | `(self, contacts: List[ForwardRef('TypeInputContact')])` |
| `3` | `True` | `contacts` | `ResetSavedRequest` | `contacts.ResetSavedRequest` | `(self, /, *args, **kwargs)` |
| `3` | `True` | `contacts` | `ResolvePhoneRequest` | `contacts.ResolvePhoneRequest` | `(self, phone: str)` |
| `3` | `True` | `contacts` | `SearchRequest` | `contacts.SearchRequest` | `(self, q: str, limit: int, broadcasts: Optional[bool] = None, bots: Optional[bool] = None)` |
| `3` | `True` | `contacts` | `SetBlockedRequest` | `contacts.SetBlockedRequest` | `(self, id: List[ForwardRef('TypeInputPeer')], limit: int, my_stories_from: Optional[bool] = None)` |
| `3` | `True` | `contacts` | `UnblockRequest` | `contacts.UnblockRequest` | `(self, id: 'TypeInputPeer', my_stories_from: Optional[bool] = None)` |
| `3` | `True` | `payments` | `GetStarsRevenueAdsAccountUrlRequest` | `payments.GetStarsRevenueAdsAccountUrlRequest` | `(self, peer: 'TypeInputPeer')` |
| `4` | `True` | `bots` | `GetAdminedBotsRequest` | `bots.GetAdminedBotsRequest` | `(self, /, *args, **kwargs)` |
| `4` | `True` | `bots` | `SetBotBroadcastDefaultAdminRightsRequest` | `bots.SetBotBroadcastDefaultAdminRightsRequest` | `(self, admin_rights: 'TypeChatAdminRights')` |
| `4` | `True` | `bots` | `SetBotGroupDefaultAdminRightsRequest` | `bots.SetBotGroupDefaultAdminRightsRequest` | `(self, admin_rights: 'TypeChatAdminRights')` |
| `4` | `True` | `channels` | `CheckSearchPostsFloodRequest` | `channels.CheckSearchPostsFloodRequest` | `(self, query: Optional[str] = None)` |
| `4` | `True` | `channels` | `ConvertToGigagroupRequest` | `channels.ConvertToGigagroupRequest` | `(self, channel: 'TypeInputChannel')` |
| `4` | `True` | `channels` | `DeleteHistoryRequest` | `channels.DeleteHistoryRequest` | `(self, channel: 'TypeInputChannel', max_id: int, for_everyone: Optional[bool] = None)` |
| `4` | `True` | `channels` | `DeleteParticipantHistoryRequest` | `channels.DeleteParticipantHistoryRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer')` |
| `4` | `True` | `channels` | `EditAdminRequest` | `channels.EditAdminRequest` | `(self, channel: 'TypeInputChannel', user_id: 'TypeInputUser', admin_rights: 'TypeChatAdminRights', rank: Optional[str] = None)` |
| `4` | `True` | `channels` | `EditBannedRequest` | `channels.EditBannedRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer', banned_rights: 'TypeChatBannedRights')` |
| `4` | `True` | `channels` | `EditLocationRequest` | `channels.EditLocationRequest` | `(self, channel: 'TypeInputChannel', geo_point: 'TypeInputGeoPoint', address: str)` |
| `4` | `True` | `channels` | `EditTitleRequest` | `channels.EditTitleRequest` | `(self, channel: 'TypeInputChannel', title: str)` |
| `4` | `True` | `channels` | `GetAdminLogRequest` | `channels.GetAdminLogRequest` | `(self, channel: 'TypeInputChannel', q: str, max_id: int, min_id: int, limit: int, events_filter: Optional[ForwardRef('TypeChannelAdminLogEventsFilter')] = None, admins: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `4` | `True` | `channels` | `GetGroupsForDiscussionRequest` | `channels.GetGroupsForDiscussionRequest` | `(self, /, *args, **kwargs)` |
| `4` | `True` | `channels` | `GetParticipantRequest` | `channels.GetParticipantRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer')` |
| `4` | `True` | `channels` | `GetParticipantsRequest` | `channels.GetParticipantsRequest` | `(self, channel: 'TypeInputChannel', filter: 'TypeChannelParticipantsFilter', offset: int, limit: int, hash: int)` |
| `4` | `True` | `channels` | `GetSendAsRequest` | `channels.GetSendAsRequest` | `(self, peer: 'TypeInputPeer', for_paid_reactions: Optional[bool] = None, for_live_stories: Optional[bool] = None)` |
| `4` | `True` | `channels` | `ReadHistoryRequest` | `channels.ReadHistoryRequest` | `(self, channel: 'TypeInputChannel', max_id: int)` |
| `4` | `True` | `channels` | `ReportAntiSpamFalsePositiveRequest` | `channels.ReportAntiSpamFalsePositiveRequest` | `(self, channel: 'TypeInputChannel', msg_id: int)` |
| `4` | `True` | `channels` | `ReportSpamRequest` | `channels.ReportSpamRequest` | `(self, channel: 'TypeInputChannel', participant: 'TypeInputPeer', id: List[int])` |
| `4` | `True` | `channels` | `SearchPostsRequest` | `channels.SearchPostsRequest` | `(self, offset_rate: int, offset_peer: 'TypeInputPeer', offset_id: int, limit: int, hashtag: Optional[str] = None, query: Optional[str] = None, allow_paid_stars: Optional[int] = None)` |
| `4` | `True` | `channels` | `SetBoostsToUnblockRestrictionsRequest` | `channels.SetBoostsToUnblockRestrictionsRequest` | `(self, channel: 'TypeInputChannel', boosts: int)` |
| `4` | `True` | `channels` | `SetDiscussionGroupRequest` | `channels.SetDiscussionGroupRequest` | `(self, broadcast: 'TypeInputChannel', group: 'TypeInputChannel')` |
| `4` | `True` | `channels` | `SetEmojiStickersRequest` | `channels.SetEmojiStickersRequest` | `(self, channel: 'TypeInputChannel', stickerset: 'TypeInputStickerSet')` |
| `4` | `True` | `channels` | `SetMainProfileTabRequest` | `channels.SetMainProfileTabRequest` | `(self, channel: 'TypeInputChannel', tab: 'TypeProfileTab')` |
| `4` | `True` | `channels` | `SetStickersRequest` | `channels.SetStickersRequest` | `(self, channel: 'TypeInputChannel', stickerset: 'TypeInputStickerSet')` |
| `4` | `True` | `channels` | `ToggleAntiSpamRequest` | `channels.ToggleAntiSpamRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `4` | `True` | `channels` | `ToggleAutotranslationRequest` | `channels.ToggleAutotranslationRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `4` | `True` | `channels` | `ToggleForumRequest` | `channels.ToggleForumRequest` | `(self, channel: 'TypeInputChannel', enabled: bool, tabs: bool)` |
| `4` | `True` | `channels` | `ToggleJoinRequestRequest` | `channels.ToggleJoinRequestRequest` | `(self, channel: 'TypeInputChannel', enabled: bool, apply_to_invites: Optional[bool] = None, guard_bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `4` | `True` | `channels` | `ToggleJoinToSendRequest` | `channels.ToggleJoinToSendRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `4` | `True` | `channels` | `ToggleParticipantsHiddenRequest` | `channels.ToggleParticipantsHiddenRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `4` | `True` | `channels` | `TogglePreHistoryHiddenRequest` | `channels.TogglePreHistoryHiddenRequest` | `(self, channel: 'TypeInputChannel', enabled: bool)` |
| `4` | `True` | `channels` | `ToggleSignaturesRequest` | `channels.ToggleSignaturesRequest` | `(self, channel: 'TypeInputChannel', signatures_enabled: Optional[bool] = None, profiles_enabled: Optional[bool] = None)` |
| `4` | `True` | `channels` | `ToggleSlowModeRequest` | `channels.ToggleSlowModeRequest` | `(self, channel: 'TypeInputChannel', seconds: int)` |
| `4` | `True` | `chatlists` | `DeleteExportedInviteRequest` | `chatlists.DeleteExportedInviteRequest` | `(self, chatlist: 'TypeInputChatlist', slug: str)` |
| `4` | `True` | `chatlists` | `EditExportedInviteRequest` | `chatlists.EditExportedInviteRequest` | `(self, chatlist: 'TypeInputChatlist', slug: str, title: Optional[str] = None, peers: Optional[List[ForwardRef('TypeInputPeer')]] = None)` |
| `4` | `True` | `chatlists` | `GetExportedInvitesRequest` | `chatlists.GetExportedInvitesRequest` | `(self, chatlist: 'TypeInputChatlist')` |
| `4` | `True` | `help` | `GetInviteTextRequest` | `help.GetInviteTextRequest` | `(self, /, *args, **kwargs)` |
| `4` | `True` | `phone` | `DeclineConferenceCallInviteRequest` | `phone.DeclineConferenceCallInviteRequest` | `(self, msg_id: int)` |
| `4` | `True` | `phone` | `DeleteConferenceCallParticipantsRequest` | `phone.DeleteConferenceCallParticipantsRequest` | `(self, call: 'TypeInputGroupCall', ids: List[int], block: bytes, only_left: Optional[bool] = None, kick: Optional[bool] = None)` |
| `4` | `True` | `phone` | `EditGroupCallParticipantRequest` | `phone.EditGroupCallParticipantRequest` | `(self, call: 'TypeInputGroupCall', participant: 'TypeInputPeer', muted: Optional[bool] = None, volume: Optional[int] = None, raise_hand: Optional[bool] = None, video_stopped: Optional[bool] = None, video_paused: Optional[bool] = None, presentation_paused: Optional[bool] = None)` |
| `4` | `True` | `phone` | `ExportGroupCallInviteRequest` | `phone.ExportGroupCallInviteRequest` | `(self, call: 'TypeInputGroupCall', can_self_unmute: Optional[bool] = None)` |
| `4` | `True` | `phone` | `GetGroupParticipantsRequest` | `phone.GetGroupParticipantsRequest` | `(self, call: 'TypeInputGroupCall', ids: List[ForwardRef('TypeInputPeer')], sources: List[int], offset: str, limit: int)` |
| `4` | `True` | `phone` | `InviteConferenceCallParticipantRequest` | `phone.InviteConferenceCallParticipantRequest` | `(self, call: 'TypeInputGroupCall', user_id: 'TypeInputUser', video: Optional[bool] = None)` |
| `4` | `True` | `phone` | `InviteToGroupCallRequest` | `phone.InviteToGroupCallRequest` | `(self, call: 'TypeInputGroupCall', users: List[ForwardRef('TypeInputUser')])` |
| `4` | `True` | `premium` | `ApplyBoostRequest` | `premium.ApplyBoostRequest` | `(self, peer: 'TypeInputPeer', slots: Optional[List[int]] = None)` |
| `4` | `True` | `premium` | `GetBoostsListRequest` | `premium.GetBoostsListRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, gifts: Optional[bool] = None)` |
| `4` | `True` | `premium` | `GetBoostsStatusRequest` | `premium.GetBoostsStatusRequest` | `(self, peer: 'TypeInputPeer')` |
| `4` | `True` | `premium` | `GetMyBoostsRequest` | `premium.GetMyBoostsRequest` | `(self, /, *args, **kwargs)` |
| `5` | `True` | `bots` | `AnswerWebhookJSONQueryRequest` | `bots.AnswerWebhookJSONQueryRequest` | `(self, query_id: int, data: 'TypeDataJSON')` |
| `5` | `True` | `bots` | `CreateBotRequest` | `bots.CreateBotRequest` | `(self, name: str, username: str, manager_id: 'TypeInputUser', via_deeplink: Optional[bool] = None)` |
| `5` | `True` | `bots` | `EditAccessSettingsRequest` | `bots.EditAccessSettingsRequest` | `(self, bot: 'TypeInputUser', restricted: Optional[bool] = None, add_users: Optional[List[ForwardRef('TypeInputUser')]] = None)` |
| `5` | `True` | `bots` | `ExportBotTokenRequest` | `bots.ExportBotTokenRequest` | `(self, bot: 'TypeInputUser', revoke: bool)` |
| `5` | `True` | `bots` | `GetAccessSettingsRequest` | `bots.GetAccessSettingsRequest` | `(self, bot: 'TypeInputUser')` |
| `5` | `True` | `bots` | `GetBotCommandsRequest` | `bots.GetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str)` |
| `5` | `True` | `bots` | `GetBotInfoRequest` | `bots.GetBotInfoRequest` | `(self, lang_code: str, bot: Optional[ForwardRef('TypeInputUser')] = None)` |
| `5` | `True` | `bots` | `GetBotMenuButtonRequest` | `bots.GetBotMenuButtonRequest` | `(self, user_id: 'TypeInputUser')` |
| `5` | `True` | `bots` | `GetBotRecommendationsRequest` | `bots.GetBotRecommendationsRequest` | `(self, bot: 'TypeInputUser')` |
| `5` | `True` | `bots` | `GetPopularAppBotsRequest` | `bots.GetPopularAppBotsRequest` | `(self, offset: str, limit: int)` |
| `5` | `True` | `bots` | `GetPreviewInfoRequest` | `bots.GetPreviewInfoRequest` | `(self, bot: 'TypeInputUser', lang_code: str)` |
| `5` | `True` | `bots` | `GetRequestedWebViewButtonRequest` | `bots.GetRequestedWebViewButtonRequest` | `(self, bot: 'TypeInputUser', webapp_req_id: str)` |
| `5` | `True` | `bots` | `InvokeWebViewCustomMethodRequest` | `bots.InvokeWebViewCustomMethodRequest` | `(self, bot: 'TypeInputUser', custom_method: str, params: 'TypeDataJSON')` |
| `5` | `True` | `bots` | `RequestWebViewButtonRequest` | `bots.RequestWebViewButtonRequest` | `(self, user_id: 'TypeInputUser', button: 'TypeKeyboardButton')` |
| `5` | `True` | `bots` | `ResetBotCommandsRequest` | `bots.ResetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str)` |
| `5` | `True` | `bots` | `SendCustomRequestRequest` | `bots.SendCustomRequestRequest` | `(self, custom_method: str, params: 'TypeDataJSON')` |
| `5` | `True` | `bots` | `SetBotCommandsRequest` | `bots.SetBotCommandsRequest` | `(self, scope: 'TypeBotCommandScope', lang_code: str, commands: List[ForwardRef('TypeBotCommand')])` |
| `5` | `True` | `bots` | `SetBotInfoRequest` | `bots.SetBotInfoRequest` | `(self, lang_code: str, bot: Optional[ForwardRef('TypeInputUser')] = None, name: Optional[str] = None, about: Optional[str] = None, description: Optional[str] = None)` |
| `5` | `True` | `bots` | `SetBotMenuButtonRequest` | `bots.SetBotMenuButtonRequest` | `(self, user_id: 'TypeInputUser', button: 'TypeBotMenuButton')` |
| `5` | `True` | `bots` | `SetCustomVerificationRequest` | `bots.SetCustomVerificationRequest` | `(self, peer: 'TypeInputPeer', enabled: Optional[bool] = None, bot: Optional[ForwardRef('TypeInputUser')] = None, custom_description: Optional[str] = None)` |
| `5` | `True` | `payments` | `BotCancelStarsSubscriptionRequest` | `payments.BotCancelStarsSubscriptionRequest` | `(self, user_id: 'TypeInputUser', charge_id: str, restore: Optional[bool] = None)` |
| `5` | `True` | `payments` | `ConnectStarRefBotRequest` | `payments.ConnectStarRefBotRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser')` |
| `5` | `True` | `payments` | `EditConnectedStarRefBotRequest` | `payments.EditConnectedStarRefBotRequest` | `(self, peer: 'TypeInputPeer', link: str, revoked: Optional[bool] = None)` |
| `5` | `True` | `payments` | `GetConnectedStarRefBotRequest` | `payments.GetConnectedStarRefBotRequest` | `(self, peer: 'TypeInputPeer', bot: 'TypeInputUser')` |
| `5` | `True` | `payments` | `GetConnectedStarRefBotsRequest` | `payments.GetConnectedStarRefBotsRequest` | `(self, peer: 'TypeInputPeer', limit: int, offset_date: Optional[datetime.datetime] = None, offset_link: Optional[str] = None)` |
| `5` | `True` | `payments` | `GetSuggestedStarRefBotsRequest` | `payments.GetSuggestedStarRefBotsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, order_by_revenue: Optional[bool] = None, order_by_date: Optional[bool] = None)` |
| `6` | `True` | `help` | `GetPremiumPromoRequest` | `help.GetPremiumPromoRequest` | `(self, /, *args, **kwargs)` |
| `6` | `True` | `payments` | `GetPremiumGiftCodeOptionsRequest` | `payments.GetPremiumGiftCodeOptionsRequest` | `(self, boost_peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `6` | `True` | `phone` | `AcceptCallRequest` | `phone.AcceptCallRequest` | `(self, peer: 'TypeInputPhoneCall', g_b: bytes, protocol: 'TypePhoneCallProtocol')` |
| `6` | `True` | `phone` | `CheckGroupCallRequest` | `phone.CheckGroupCallRequest` | `(self, call: 'TypeInputGroupCall', sources: List[int])` |
| `6` | `True` | `phone` | `ConfirmCallRequest` | `phone.ConfirmCallRequest` | `(self, peer: 'TypeInputPhoneCall', g_a: bytes, key_fingerprint: int, protocol: 'TypePhoneCallProtocol')` |
| `6` | `True` | `phone` | `CreateConferenceCallRequest` | `phone.CreateConferenceCallRequest` | `(self, muted: Optional[bool] = None, video_stopped: Optional[bool] = None, join: Optional[bool] = None, random_id: int = None, public_key: Optional[int] = None, block: Optional[bytes] = None, params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `6` | `True` | `phone` | `CreateGroupCallRequest` | `phone.CreateGroupCallRequest` | `(self, peer: 'TypeInputPeer', rtmp_stream: Optional[bool] = None, random_id: int = None, title: Optional[str] = None, schedule_date: Optional[datetime.datetime] = None)` |
| `6` | `True` | `phone` | `DiscardCallRequest` | `phone.DiscardCallRequest` | `(self, peer: 'TypeInputPhoneCall', duration: int, reason: 'TypePhoneCallDiscardReason', connection_id: int, video: Optional[bool] = None)` |
| `6` | `True` | `phone` | `DiscardGroupCallRequest` | `phone.DiscardGroupCallRequest` | `(self, call: 'TypeInputGroupCall')` |
| `6` | `True` | `phone` | `EditGroupCallTitleRequest` | `phone.EditGroupCallTitleRequest` | `(self, call: 'TypeInputGroupCall', title: str)` |
| `6` | `True` | `phone` | `GetCallConfigRequest` | `phone.GetCallConfigRequest` | `(self, /, *args, **kwargs)` |
| `6` | `True` | `phone` | `GetGroupCallChainBlocksRequest` | `phone.GetGroupCallChainBlocksRequest` | `(self, call: 'TypeInputGroupCall', sub_chain_id: int, offset: int, limit: int)` |
| `6` | `True` | `phone` | `GetGroupCallJoinAsRequest` | `phone.GetGroupCallJoinAsRequest` | `(self, peer: 'TypeInputPeer')` |
| `6` | `True` | `phone` | `GetGroupCallRequest` | `phone.GetGroupCallRequest` | `(self, call: 'TypeInputGroupCall', limit: int)` |
| `6` | `True` | `phone` | `GetGroupCallStarsRequest` | `phone.GetGroupCallStarsRequest` | `(self, call: 'TypeInputGroupCall')` |
| `6` | `True` | `phone` | `GetGroupCallStreamRtmpUrlRequest` | `phone.GetGroupCallStreamRtmpUrlRequest` | `(self, peer: 'TypeInputPeer', revoke: bool, live_story: Optional[bool] = None)` |
| `6` | `True` | `phone` | `JoinGroupCallPresentationRequest` | `phone.JoinGroupCallPresentationRequest` | `(self, call: 'TypeInputGroupCall', params: 'TypeDataJSON')` |
| `6` | `True` | `phone` | `JoinGroupCallRequest` | `phone.JoinGroupCallRequest` | `(self, call: 'TypeInputGroupCall', join_as: 'TypeInputPeer', params: 'TypeDataJSON', muted: Optional[bool] = None, video_stopped: Optional[bool] = None, invite_hash: Optional[str] = None, public_key: Optional[int] = None, block: Optional[bytes] = None)` |
| `6` | `True` | `phone` | `LeaveGroupCallPresentationRequest` | `phone.LeaveGroupCallPresentationRequest` | `(self, call: 'TypeInputGroupCall')` |
| `6` | `True` | `phone` | `LeaveGroupCallRequest` | `phone.LeaveGroupCallRequest` | `(self, call: 'TypeInputGroupCall', source: int)` |
| `6` | `True` | `phone` | `ReceivedCallRequest` | `phone.ReceivedCallRequest` | `(self, peer: 'TypeInputPhoneCall')` |
| `6` | `True` | `phone` | `RequestCallRequest` | `phone.RequestCallRequest` | `(self, user_id: 'TypeInputUser', g_a_hash: bytes, protocol: 'TypePhoneCallProtocol', video: Optional[bool] = None, random_id: int = None)` |
| `6` | `True` | `phone` | `SaveCallDebugRequest` | `phone.SaveCallDebugRequest` | `(self, peer: 'TypeInputPhoneCall', debug: 'TypeDataJSON')` |
| `6` | `True` | `phone` | `SaveCallLogRequest` | `phone.SaveCallLogRequest` | `(self, peer: 'TypeInputPhoneCall', file: 'TypeInputFile')` |
| `6` | `True` | `phone` | `SaveDefaultGroupCallJoinAsRequest` | `phone.SaveDefaultGroupCallJoinAsRequest` | `(self, peer: 'TypeInputPeer', join_as: 'TypeInputPeer')` |
| `6` | `True` | `phone` | `SaveDefaultSendAsRequest` | `phone.SaveDefaultSendAsRequest` | `(self, call: 'TypeInputGroupCall', send_as: 'TypeInputPeer')` |
| `6` | `True` | `phone` | `SendConferenceCallBroadcastRequest` | `phone.SendConferenceCallBroadcastRequest` | `(self, call: 'TypeInputGroupCall', block: bytes)` |
| `6` | `True` | `phone` | `SendSignalingDataRequest` | `phone.SendSignalingDataRequest` | `(self, peer: 'TypeInputPhoneCall', data: bytes)` |
| `6` | `True` | `phone` | `SetCallRatingRequest` | `phone.SetCallRatingRequest` | `(self, peer: 'TypeInputPhoneCall', rating: int, comment: str, user_initiative: Optional[bool] = None)` |
| `6` | `True` | `phone` | `StartScheduledGroupCallRequest` | `phone.StartScheduledGroupCallRequest` | `(self, call: 'TypeInputGroupCall')` |
| `6` | `True` | `phone` | `ToggleGroupCallRecordRequest` | `phone.ToggleGroupCallRecordRequest` | `(self, call: 'TypeInputGroupCall', start: Optional[bool] = None, video: Optional[bool] = None, title: Optional[str] = None, video_portrait: Optional[bool] = None)` |
| `6` | `True` | `phone` | `ToggleGroupCallSettingsRequest` | `phone.ToggleGroupCallSettingsRequest` | `(self, call: 'TypeInputGroupCall', reset_invite_hash: Optional[bool] = None, join_muted: Optional[bool] = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None)` |
| `6` | `True` | `phone` | `ToggleGroupCallStartSubscriptionRequest` | `phone.ToggleGroupCallStartSubscriptionRequest` | `(self, call: 'TypeInputGroupCall', subscribed: bool)` |
| `6` | `True` | `stats` | `GetStoryStatsRequest` | `stats.GetStoryStatsRequest` | `(self, peer: 'TypeInputPeer', id: int, dark: Optional[bool] = None)` |
| `6` | `True` | `stickers` | `AddStickerToSetRequest` | `stickers.AddStickerToSetRequest` | `(self, stickerset: 'TypeInputStickerSet', sticker: 'TypeInputStickerSetItem')` |
| `6` | `True` | `stickers` | `ChangeStickerPositionRequest` | `stickers.ChangeStickerPositionRequest` | `(self, sticker: 'TypeInputDocument', position: int)` |
| `6` | `True` | `stickers` | `ChangeStickerRequest` | `stickers.ChangeStickerRequest` | `(self, sticker: 'TypeInputDocument', emoji: Optional[str] = None, mask_coords: Optional[ForwardRef('TypeMaskCoords')] = None, keywords: Optional[str] = None)` |
| `6` | `True` | `stickers` | `CheckShortNameRequest` | `stickers.CheckShortNameRequest` | `(self, short_name: str)` |
| `6` | `True` | `stickers` | `CreateStickerSetRequest` | `stickers.CreateStickerSetRequest` | `(self, user_id: 'TypeInputUser', title: str, short_name: str, stickers: List[ForwardRef('TypeInputStickerSetItem')], masks: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, thumb: Optional[ForwardRef('TypeInputDocument')] = None, software: Optional[str] = None)` |
| `6` | `True` | `stickers` | `DeleteStickerSetRequest` | `stickers.DeleteStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet')` |
| `6` | `True` | `stickers` | `RemoveStickerFromSetRequest` | `stickers.RemoveStickerFromSetRequest` | `(self, sticker: 'TypeInputDocument')` |
| `6` | `True` | `stickers` | `RenameStickerSetRequest` | `stickers.RenameStickerSetRequest` | `(self, stickerset: 'TypeInputStickerSet', title: str)` |
| `6` | `True` | `stickers` | `ReplaceStickerRequest` | `stickers.ReplaceStickerRequest` | `(self, sticker: 'TypeInputDocument', new_sticker: 'TypeInputStickerSetItem')` |
| `6` | `True` | `stickers` | `SetStickerSetThumbRequest` | `stickers.SetStickerSetThumbRequest` | `(self, stickerset: 'TypeInputStickerSet', thumb: Optional[ForwardRef('TypeInputDocument')] = None, thumb_document_id: Optional[int] = None)` |
| `6` | `True` | `stickers` | `SuggestShortNameRequest` | `stickers.SuggestShortNameRequest` | `(self, title: str)` |
| `6` | `True` | `stories` | `ActivateStealthModeRequest` | `stories.ActivateStealthModeRequest` | `(self, past: Optional[bool] = None, future: Optional[bool] = None)` |
| `6` | `True` | `stories` | `CanSendStoryRequest` | `stories.CanSendStoryRequest` | `(self, peer: 'TypeInputPeer')` |
| `6` | `True` | `stories` | `CreateAlbumRequest` | `stories.CreateAlbumRequest` | `(self, peer: 'TypeInputPeer', title: str, stories: List[int])` |
| `6` | `True` | `stories` | `DeleteAlbumRequest` | `stories.DeleteAlbumRequest` | `(self, peer: 'TypeInputPeer', album_id: int)` |
| `6` | `True` | `stories` | `DeleteStoriesRequest` | `stories.DeleteStoriesRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `6` | `True` | `stories` | `EditStoryRequest` | `stories.EditStoryRequest` | `(self, peer: 'TypeInputPeer', id: int, media: Optional[ForwardRef('TypeInputMedia')] = None, media_areas: Optional[List[ForwardRef('TypeMediaArea')]] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, privacy_rules: Optional[List[ForwardRef('TypeInputPrivacyRule')]] = None, music: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `6` | `True` | `stories` | `ExportStoryLinkRequest` | `stories.ExportStoryLinkRequest` | `(self, peer: 'TypeInputPeer', id: int)` |
| `6` | `True` | `stories` | `GetAlbumStoriesRequest` | `stories.GetAlbumStoriesRequest` | `(self, peer: 'TypeInputPeer', album_id: int, offset: int, limit: int)` |
| `6` | `True` | `stories` | `GetAlbumsRequest` | `stories.GetAlbumsRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `6` | `True` | `stories` | `GetAllStoriesRequest` | `stories.GetAllStoriesRequest` | `(self, next: Optional[bool] = None, hidden: Optional[bool] = None, state: Optional[str] = None)` |
| `6` | `True` | `stories` | `GetPinnedStoriesRequest` | `stories.GetPinnedStoriesRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, limit: int)` |
| `6` | `True` | `stories` | `GetStoriesArchiveRequest` | `stories.GetStoriesArchiveRequest` | `(self, peer: 'TypeInputPeer', offset_id: int, limit: int)` |
| `6` | `True` | `stories` | `GetStoriesByIDRequest` | `stories.GetStoriesByIDRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `6` | `True` | `stories` | `GetStoriesViewsRequest` | `stories.GetStoriesViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `6` | `True` | `stories` | `GetStoryReactionsListRequest` | `stories.GetStoryReactionsListRequest` | `(self, peer: 'TypeInputPeer', id: int, limit: int, forwards_first: Optional[bool] = None, reaction: Optional[ForwardRef('TypeReaction')] = None, offset: Optional[str] = None)` |
| `6` | `True` | `stories` | `GetStoryViewsListRequest` | `stories.GetStoryViewsListRequest` | `(self, peer: 'TypeInputPeer', id: int, offset: str, limit: int, just_contacts: Optional[bool] = None, reactions_first: Optional[bool] = None, forwards_first: Optional[bool] = None, q: Optional[str] = None)` |
| `6` | `True` | `stories` | `IncrementStoryViewsRequest` | `stories.IncrementStoryViewsRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `6` | `True` | `stories` | `ReadStoriesRequest` | `stories.ReadStoriesRequest` | `(self, peer: 'TypeInputPeer', max_id: int)` |
| `6` | `True` | `stories` | `ReorderAlbumsRequest` | `stories.ReorderAlbumsRequest` | `(self, peer: 'TypeInputPeer', order: List[int])` |
| `6` | `True` | `stories` | `ReportRequest` | `stories.ReportRequest` | `(self, peer: 'TypeInputPeer', id: List[int], option: bytes, message: str)` |
| `6` | `True` | `stories` | `SearchPostsRequest` | `stories.SearchPostsRequest` | `(self, offset: str, limit: int, hashtag: Optional[str] = None, area: Optional[ForwardRef('TypeMediaArea')] = None, peer: Optional[ForwardRef('TypeInputPeer')] = None)` |
| `6` | `True` | `stories` | `SendReactionRequest` | `stories.SendReactionRequest` | `(self, peer: 'TypeInputPeer', story_id: int, reaction: 'TypeReaction', add_to_recent: Optional[bool] = None)` |
| `6` | `True` | `stories` | `SendStoryRequest` | `stories.SendStoryRequest` | `(self, peer: 'TypeInputPeer', media: 'TypeInputMedia', privacy_rules: List[ForwardRef('TypeInputPrivacyRule')], pinned: Optional[bool] = None, noforwards: Optional[bool] = None, fwd_modified: Optional[bool] = None, media_areas: Optional[List[ForwardRef('TypeMediaArea')]] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, random_id: int = None, period: Optional[int] = None, fwd_from_id: Optional[ForwardRef('TypeInputPeer')] = None, fwd_from_story: Optional[int] = None, albums: Optional[List[int]] = None, music: Optional[ForwardRef('TypeInputDocument')] = None)` |
| `6` | `True` | `stories` | `StartLiveRequest` | `stories.StartLiveRequest` | `(self, peer: 'TypeInputPeer', privacy_rules: List[ForwardRef('TypeInputPrivacyRule')], pinned: Optional[bool] = None, noforwards: Optional[bool] = None, rtmp_stream: Optional[bool] = None, caption: Optional[str] = None, entities: Optional[List[ForwardRef('TypeMessageEntity')]] = None, random_id: int = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None)` |
| `6` | `True` | `stories` | `ToggleAllStoriesHiddenRequest` | `stories.ToggleAllStoriesHiddenRequest` | `(self, hidden: bool)` |
| `6` | `True` | `stories` | `TogglePinnedRequest` | `stories.TogglePinnedRequest` | `(self, peer: 'TypeInputPeer', id: List[int], pinned: bool)` |
| `6` | `True` | `stories` | `TogglePinnedToTopRequest` | `stories.TogglePinnedToTopRequest` | `(self, peer: 'TypeInputPeer', id: List[int])` |
| `7` | `True` | `payments` | `ApplyGiftCodeRequest` | `payments.ApplyGiftCodeRequest` | `(self, slug: str)` |
| `7` | `True` | `payments` | `AssignAppStoreTransactionRequest` | `payments.AssignAppStoreTransactionRequest` | `(self, receipt: bytes, purpose: 'TypeInputStorePaymentPurpose')` |
| `7` | `True` | `payments` | `AssignPlayMarketTransactionRequest` | `payments.AssignPlayMarketTransactionRequest` | `(self, receipt: 'TypeDataJSON', purpose: 'TypeInputStorePaymentPurpose')` |
| `7` | `True` | `payments` | `CanPurchaseStoreRequest` | `payments.CanPurchaseStoreRequest` | `(self, purpose: 'TypeInputStorePaymentPurpose')` |
| `7` | `True` | `payments` | `ChangeStarsSubscriptionRequest` | `payments.ChangeStarsSubscriptionRequest` | `(self, peer: 'TypeInputPeer', subscription_id: str, canceled: Optional[bool] = None)` |
| `7` | `True` | `payments` | `CheckCanSendGiftRequest` | `payments.CheckCanSendGiftRequest` | `(self, gift_id: int)` |
| `7` | `True` | `payments` | `CheckGiftCodeRequest` | `payments.CheckGiftCodeRequest` | `(self, slug: str)` |
| `7` | `True` | `payments` | `ClearSavedInfoRequest` | `payments.ClearSavedInfoRequest` | `(self, credentials: Optional[bool] = None, info: Optional[bool] = None)` |
| `7` | `True` | `payments` | `ConvertStarGiftRequest` | `payments.ConvertStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift')` |
| `7` | `True` | `payments` | `CraftStarGiftRequest` | `payments.CraftStarGiftRequest` | `(self, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `7` | `True` | `payments` | `CreateStarGiftCollectionRequest` | `payments.CreateStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', title: str, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `7` | `True` | `payments` | `DeleteStarGiftCollectionRequest` | `payments.DeleteStarGiftCollectionRequest` | `(self, peer: 'TypeInputPeer', collection_id: int)` |
| `7` | `True` | `payments` | `ExportInvoiceRequest` | `payments.ExportInvoiceRequest` | `(self, invoice_media: 'TypeInputMedia')` |
| `7` | `True` | `payments` | `FulfillStarsSubscriptionRequest` | `payments.FulfillStarsSubscriptionRequest` | `(self, peer: 'TypeInputPeer', subscription_id: str)` |
| `7` | `True` | `payments` | `GetBankCardDataRequest` | `payments.GetBankCardDataRequest` | `(self, number: str)` |
| `7` | `True` | `payments` | `GetCraftStarGiftsRequest` | `payments.GetCraftStarGiftsRequest` | `(self, gift_id: int, offset: str, limit: int)` |
| `7` | `True` | `payments` | `GetGiveawayInfoRequest` | `payments.GetGiveawayInfoRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `7` | `True` | `payments` | `GetPaymentFormRequest` | `payments.GetPaymentFormRequest` | `(self, invoice: 'TypeInputInvoice', theme_params: Optional[ForwardRef('TypeDataJSON')] = None)` |
| `7` | `True` | `payments` | `GetPaymentReceiptRequest` | `payments.GetPaymentReceiptRequest` | `(self, peer: 'TypeInputPeer', msg_id: int)` |
| `7` | `True` | `payments` | `GetResaleStarGiftsRequest` | `payments.GetResaleStarGiftsRequest` | `(self, gift_id: int, offset: str, limit: int, sort_by_price: Optional[bool] = None, sort_by_num: Optional[bool] = None, for_craft: Optional[bool] = None, stars_only: Optional[bool] = None, attributes_hash: Optional[int] = None, attributes: Optional[List[ForwardRef('TypeStarGiftAttributeId')]] = None)` |
| `7` | `True` | `payments` | `GetSavedInfoRequest` | `payments.GetSavedInfoRequest` | `(self, /, *args, **kwargs)` |
| `7` | `True` | `payments` | `GetSavedStarGiftRequest` | `payments.GetSavedStarGiftRequest` | `(self, stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `7` | `True` | `payments` | `GetSavedStarGiftsRequest` | `payments.GetSavedStarGiftsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, exclude_unsaved: Optional[bool] = None, exclude_saved: Optional[bool] = None, exclude_unlimited: Optional[bool] = None, exclude_unique: Optional[bool] = None, sort_by_value: Optional[bool] = None, exclude_upgradable: Optional[bool] = None, exclude_unupgradable: Optional[bool] = None, peer_color_available: Optional[bool] = None, exclude_hosted: Optional[bool] = None, collection_id: Optional[int] = None)` |
| `7` | `True` | `payments` | `GetStarGiftActiveAuctionsRequest` | `payments.GetStarGiftActiveAuctionsRequest` | `(self, hash: int)` |
| `7` | `True` | `payments` | `GetStarGiftAuctionAcquiredGiftsRequest` | `payments.GetStarGiftAuctionAcquiredGiftsRequest` | `(self, gift_id: int)` |
| `7` | `True` | `payments` | `GetStarGiftAuctionStateRequest` | `payments.GetStarGiftAuctionStateRequest` | `(self, auction: 'TypeInputStarGiftAuction', version: int)` |
| `7` | `True` | `payments` | `GetStarGiftCollectionsRequest` | `payments.GetStarGiftCollectionsRequest` | `(self, peer: 'TypeInputPeer', hash: int)` |
| `7` | `True` | `payments` | `GetStarGiftUpgradeAttributesRequest` | `payments.GetStarGiftUpgradeAttributesRequest` | `(self, gift_id: int)` |
| `7` | `True` | `payments` | `GetStarGiftUpgradePreviewRequest` | `payments.GetStarGiftUpgradePreviewRequest` | `(self, gift_id: int)` |
| `7` | `True` | `payments` | `GetStarGiftWithdrawalUrlRequest` | `payments.GetStarGiftWithdrawalUrlRequest` | `(self, stargift: 'TypeInputSavedStarGift', password: 'TypeInputCheckPasswordSRP')` |
| `7` | `True` | `payments` | `GetStarGiftsRequest` | `payments.GetStarGiftsRequest` | `(self, hash: int)` |
| `7` | `True` | `payments` | `GetStarsGiftOptionsRequest` | `payments.GetStarsGiftOptionsRequest` | `(self, user_id: Optional[ForwardRef('TypeInputUser')] = None)` |
| `7` | `True` | `payments` | `GetStarsGiveawayOptionsRequest` | `payments.GetStarsGiveawayOptionsRequest` | `(self, /, *args, **kwargs)` |
| `7` | `True` | `payments` | `GetStarsRevenueStatsRequest` | `payments.GetStarsRevenueStatsRequest` | `(self, peer: 'TypeInputPeer', dark: Optional[bool] = None, ton: Optional[bool] = None)` |
| `7` | `True` | `payments` | `GetStarsRevenueWithdrawalUrlRequest` | `payments.GetStarsRevenueWithdrawalUrlRequest` | `(self, peer: 'TypeInputPeer', password: 'TypeInputCheckPasswordSRP', ton: Optional[bool] = None, amount: Optional[int] = None)` |
| `7` | `True` | `payments` | `GetStarsStatusRequest` | `payments.GetStarsStatusRequest` | `(self, peer: 'TypeInputPeer', ton: Optional[bool] = None)` |
| `7` | `True` | `payments` | `GetStarsSubscriptionsRequest` | `payments.GetStarsSubscriptionsRequest` | `(self, peer: 'TypeInputPeer', offset: str, missing_balance: Optional[bool] = None)` |
| `7` | `True` | `payments` | `GetStarsTopupOptionsRequest` | `payments.GetStarsTopupOptionsRequest` | `(self, /, *args, **kwargs)` |
| `7` | `True` | `payments` | `GetStarsTransactionsByIDRequest` | `payments.GetStarsTransactionsByIDRequest` | `(self, peer: 'TypeInputPeer', id: List[ForwardRef('TypeInputStarsTransaction')], ton: Optional[bool] = None)` |
| `7` | `True` | `payments` | `GetStarsTransactionsRequest` | `payments.GetStarsTransactionsRequest` | `(self, peer: 'TypeInputPeer', offset: str, limit: int, inbound: Optional[bool] = None, outbound: Optional[bool] = None, ascending: Optional[bool] = None, ton: Optional[bool] = None, subscription_id: Optional[str] = None)` |
| `7` | `True` | `payments` | `GetUniqueStarGiftRequest` | `payments.GetUniqueStarGiftRequest` | `(self, slug: str)` |
| `7` | `True` | `payments` | `GetUniqueStarGiftValueInfoRequest` | `payments.GetUniqueStarGiftValueInfoRequest` | `(self, slug: str)` |
| `7` | `True` | `payments` | `LaunchPrepaidGiveawayRequest` | `payments.LaunchPrepaidGiveawayRequest` | `(self, peer: 'TypeInputPeer', giveaway_id: int, purpose: 'TypeInputStorePaymentPurpose')` |
| `7` | `True` | `payments` | `RefundStarsChargeRequest` | `payments.RefundStarsChargeRequest` | `(self, user_id: 'TypeInputUser', charge_id: str)` |
| `7` | `True` | `payments` | `ReorderStarGiftCollectionsRequest` | `payments.ReorderStarGiftCollectionsRequest` | `(self, peer: 'TypeInputPeer', order: List[int])` |
| `7` | `True` | `payments` | `ResolveStarGiftOfferRequest` | `payments.ResolveStarGiftOfferRequest` | `(self, offer_msg_id: int, decline: Optional[bool] = None)` |
| `7` | `True` | `payments` | `SaveStarGiftRequest` | `payments.SaveStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', unsave: Optional[bool] = None)` |
| `7` | `True` | `payments` | `SendPaymentFormRequest` | `payments.SendPaymentFormRequest` | `(self, form_id: int, invoice: 'TypeInputInvoice', credentials: 'TypeInputPaymentCredentials', requested_info_id: Optional[str] = None, shipping_option_id: Optional[str] = None, tip_amount: Optional[int] = None)` |
| `7` | `True` | `payments` | `SendStarGiftOfferRequest` | `payments.SendStarGiftOfferRequest` | `(self, peer: 'TypeInputPeer', slug: str, price: 'TypeStarsAmount', duration: int, random_id: int = None, allow_paid_stars: Optional[int] = None)` |
| `7` | `True` | `payments` | `SendStarsFormRequest` | `payments.SendStarsFormRequest` | `(self, form_id: int, invoice: 'TypeInputInvoice')` |
| `7` | `True` | `payments` | `ToggleStarGiftsPinnedToTopRequest` | `payments.ToggleStarGiftsPinnedToTopRequest` | `(self, peer: 'TypeInputPeer', stargift: List[ForwardRef('TypeInputSavedStarGift')])` |
| `7` | `True` | `payments` | `TransferStarGiftRequest` | `payments.TransferStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', to_id: 'TypeInputPeer')` |
| `7` | `True` | `payments` | `UpgradeStarGiftRequest` | `payments.UpgradeStarGiftRequest` | `(self, stargift: 'TypeInputSavedStarGift', keep_original_details: Optional[bool] = None)` |
| `7` | `True` | `payments` | `ValidateRequestedInfoRequest` | `payments.ValidateRequestedInfoRequest` | `(self, invoice: 'TypeInputInvoice', info: 'TypePaymentRequestedInfo', save: Optional[bool] = None)` |
| `8` | `True` | `help` | `AcceptTermsOfServiceRequest` | `help.AcceptTermsOfServiceRequest` | `(self, id: 'TypeDataJSON')` |
| `8` | `True` | `help` | `DismissSuggestionRequest` | `help.DismissSuggestionRequest` | `(self, peer: 'TypeInputPeer', suggestion: str)` |
| `8` | `True` | `help` | `GetAppConfigRequest` | `help.GetAppConfigRequest` | `(self, hash: int)` |
| `8` | `True` | `help` | `GetCdnConfigRequest` | `help.GetCdnConfigRequest` | `(self, /, *args, **kwargs)` |
| `8` | `True` | `help` | `GetConfigRequest` | `help.GetConfigRequest` | `(self, /, *args, **kwargs)` |
| `8` | `True` | `help` | `GetCountriesListRequest` | `help.GetCountriesListRequest` | `(self, lang_code: str, hash: int)` |
| `8` | `True` | `help` | `GetDeepLinkInfoRequest` | `help.GetDeepLinkInfoRequest` | `(self, path: str)` |
| `8` | `True` | `help` | `GetNearestDcRequest` | `help.GetNearestDcRequest` | `(self, /, *args, **kwargs)` |
| `8` | `True` | `help` | `GetPassportConfigRequest` | `help.GetPassportConfigRequest` | `(self, hash: int)` |
| `8` | `True` | `help` | `GetPromoDataRequest` | `help.GetPromoDataRequest` | `(self, /, *args, **kwargs)` |
| `8` | `True` | `help` | `GetRecentMeUrlsRequest` | `help.GetRecentMeUrlsRequest` | `(self, referer: str)` |
| `8` | `True` | `help` | `GetSupportNameRequest` | `help.GetSupportNameRequest` | `(self, /, *args, **kwargs)` |
| `8` | `True` | `help` | `GetSupportRequest` | `help.GetSupportRequest` | `(self, /, *args, **kwargs)` |
| `8` | `True` | `help` | `GetTimezonesListRequest` | `help.GetTimezonesListRequest` | `(self, hash: int)` |
| `8` | `True` | `help` | `HidePromoDataRequest` | `help.HidePromoDataRequest` | `(self, peer: 'TypeInputPeer')` |
| `8` | `True` | `help` | `SaveAppLogRequest` | `help.SaveAppLogRequest` | `(self, events: List[ForwardRef('TypeInputAppEvent')])` |
| `8` | `True` | `langpack` | `GetDifferenceRequest` | `langpack.GetDifferenceRequest` | `(self, lang_pack: str, lang_code: str, from_version: int)` |
| `8` | `True` | `langpack` | `GetLangPackRequest` | `langpack.GetLangPackRequest` | `(self, lang_pack: str, lang_code: str)` |
| `8` | `True` | `langpack` | `GetLanguageRequest` | `langpack.GetLanguageRequest` | `(self, lang_pack: str, lang_code: str)` |
| `8` | `True` | `langpack` | `GetLanguagesRequest` | `langpack.GetLanguagesRequest` | `(self, lang_pack: str)` |
| `8` | `True` | `langpack` | `GetStringsRequest` | `langpack.GetStringsRequest` | `(self, lang_pack: str, lang_code: str, keys: List[str])` |
| `8` | `True` | `stats` | `GetBroadcastStatsRequest` | `stats.GetBroadcastStatsRequest` | `(self, channel: 'TypeInputChannel', dark: Optional[bool] = None)` |
| `8` | `True` | `stats` | `GetMegagroupStatsRequest` | `stats.GetMegagroupStatsRequest` | `(self, channel: 'TypeInputChannel', dark: Optional[bool] = None)` |
| `8` | `True` | `stats` | `LoadAsyncGraphRequest` | `stats.LoadAsyncGraphRequest` | `(self, token: str, x: Optional[int] = None)` |
| `10` | `True` | `aicompose` | `CreateToneRequest` | `aicompose.CreateToneRequest` | `(self, emoji_id: int, title: str, prompt: str, display_author: Optional[bool] = None)` |
| `10` | `True` | `aicompose` | `DeleteToneRequest` | `aicompose.DeleteToneRequest` | `(self, tone: 'TypeInputAiComposeTone')` |
| `10` | `True` | `aicompose` | `GetToneExampleRequest` | `aicompose.GetToneExampleRequest` | `(self, tone: 'TypeInputAiComposeTone', num: int)` |
| `10` | `True` | `aicompose` | `GetToneRequest` | `aicompose.GetToneRequest` | `(self, tone: 'TypeInputAiComposeTone')` |
| `10` | `True` | `aicompose` | `GetTonesRequest` | `aicompose.GetTonesRequest` | `(self, hash: int)` |
| `10` | `True` | `aicompose` | `SaveToneRequest` | `aicompose.SaveToneRequest` | `(self, tone: 'TypeInputAiComposeTone', unsave: bool)` |
| `10` | `True` | `fragment` | `GetCollectibleInfoRequest` | `fragment.GetCollectibleInfoRequest` | `(self, collectible: 'TypeInputCollectible')` |
| `10` | `True` | `smsjobs` | `FinishJobRequest` | `smsjobs.FinishJobRequest` | `(self, job_id: str, error: Optional[str] = None)` |
| `10` | `True` | `smsjobs` | `GetSmsJobRequest` | `smsjobs.GetSmsJobRequest` | `(self, job_id: str)` |
| `10` | `True` | `smsjobs` | `GetStatusRequest` | `smsjobs.GetStatusRequest` | `(self, /, *args, **kwargs)` |
| `10` | `True` | `smsjobs` | `IsEligibleToJoinRequest` | `smsjobs.IsEligibleToJoinRequest` | `(self, /, *args, **kwargs)` |
| `10` | `True` | `smsjobs` | `JoinRequest` | `smsjobs.JoinRequest` | `(self, /, *args, **kwargs)` |
| `10` | `True` | `smsjobs` | `LeaveRequest` | `smsjobs.LeaveRequest` | `(self, /, *args, **kwargs)` |
