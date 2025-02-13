# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...environment import MergeEnvironment
from .resources.account_details.client import AccountDetailsClient, AsyncAccountDetailsClient
from .resources.account_token.client import AccountTokenClient, AsyncAccountTokenClient
from .resources.available_actions.client import AsyncAvailableActionsClient, AvailableActionsClient
from .resources.delete_account.client import AsyncDeleteAccountClient, DeleteAccountClient
from .resources.drives.client import AsyncDrivesClient, DrivesClient
from .resources.files.client import AsyncFilesClient, FilesClient
from .resources.folders.client import AsyncFoldersClient, FoldersClient
from .resources.force_resync.client import AsyncForceResyncClient, ForceResyncClient
from .resources.generate_key.client import AsyncGenerateKeyClient, GenerateKeyClient
from .resources.groups.client import AsyncGroupsClient, GroupsClient
from .resources.issues.client import AsyncIssuesClient, IssuesClient
from .resources.link_token.client import AsyncLinkTokenClient, LinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient, LinkedAccountsClient
from .resources.passthrough.client import AsyncPassthroughClient, PassthroughClient
from .resources.regenerate_key.client import AsyncRegenerateKeyClient, RegenerateKeyClient
from .resources.selective_sync.client import AsyncSelectiveSyncClient, SelectiveSyncClient
from .resources.sync_status.client import AsyncSyncStatusClient, SyncStatusClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient, WebhookReceiversClient


class FilestorageClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.account_details = AccountDetailsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.account_token = AccountTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.available_actions = AvailableActionsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.delete_account = DeleteAccountClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.drives = DrivesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.files = FilesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.folders = FoldersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.generate_key = GenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.groups = GroupsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.issues = IssuesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.link_token = LinkTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.linked_accounts = LinkedAccountsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.passthrough = PassthroughClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.regenerate_key = RegenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.selective_sync = SelectiveSyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.sync_status = SyncStatusClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.force_resync = ForceResyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.users = UsersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.webhook_receivers = WebhookReceiversClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )


class AsyncFilestorageClient:
    def __init__(
        self, *, environment: MergeEnvironment = MergeEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper
        self.account_details = AsyncAccountDetailsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.account_token = AsyncAccountTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.available_actions = AsyncAvailableActionsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.delete_account = AsyncDeleteAccountClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.drives = AsyncDrivesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.files = AsyncFilesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.folders = AsyncFoldersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.generate_key = AsyncGenerateKeyClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.groups = AsyncGroupsClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.issues = AsyncIssuesClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.link_token = AsyncLinkTokenClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.linked_accounts = AsyncLinkedAccountsClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.passthrough = AsyncPassthroughClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.regenerate_key = AsyncRegenerateKeyClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.selective_sync = AsyncSelectiveSyncClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
        self.sync_status = AsyncSyncStatusClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.force_resync = AsyncForceResyncClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(environment=self._environment, client_wrapper=self._client_wrapper)
        self.webhook_receivers = AsyncWebhookReceiversClient(
            environment=self._environment, client_wrapper=self._client_wrapper
        )
