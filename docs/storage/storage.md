### Storage

Objects are stored in [`StorageItem`](../api/App.Storage.StorageItem.md). The [`Storage`](../api/App.Storage.Storage.md) contains list of them. Files are stored in [`StorageUnit`](../api/App.Storage.StorageUnit.md) format. DB connection is implemented via [`Adapters`](../api/App.DB.Adapters.md), every adapter must implement object flushing, queries and linking.
