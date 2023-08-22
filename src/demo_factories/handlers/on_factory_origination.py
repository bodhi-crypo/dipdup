from typing import cast

from dipdup.context import HandlerContext
from dipdup.models.tezos_tzkt import TzktOperationData


async def on_factory_origination(
    ctx: HandlerContext,
    origination_0: TzktOperationData,
) -> None:
    originated_contract = cast(str, origination_0.originated_contract_address)
    name = f'registry_dao_{originated_contract}'
    await ctx.add_contract(
        kind='tezos',
        name=originated_contract,
        address=originated_contract,
        typename='registry',
    )
    await ctx.add_index(
        name=name,
        template='registry_dao',
        values={'contract': originated_contract},
    )