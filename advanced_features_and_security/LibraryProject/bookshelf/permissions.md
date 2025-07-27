# Django Permissions and Groups Setup

## Custom Permissions (in Book model)
- `can_view`: View list of books
- `can_create`: Add new books
- `can_edit`: Modify existing books
- `can_delete`: Remove books

## Groups Configuration (done via admin)
- **Viewers**: `can_view`
- **Editors**: `can_view`, `can_create`, `can_edit`
- **Admins**: All permissions

## Enforced in Views
- Decorators such as `@permission_required('bookshelf.can_edit')` are used in views to enforce access.

## Testing
- Create sample users and assign to each group to verify enforcement.
