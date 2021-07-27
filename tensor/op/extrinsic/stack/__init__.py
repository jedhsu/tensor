class Stack(Join):
    Stack = jnp.stack  # [TODO] clarify

    HorizontalStack = jnp.hstack
    VerticalStack = jnp.vstack
    DiagonalStack = jnp.dstack

    # [TODO] clarify
    RowStack = jnp.row_stack
    ColumnStack = jnp.column_stack
