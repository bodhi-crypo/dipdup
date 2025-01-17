from demo_etherlink.types.controller.tezos_parameters.default import DefaultParameter as ControllerDefaultParameter
from demo_etherlink.types.controller.tezos_storage import ControllerStorage
from demo_etherlink.types.rollup.tezos_parameters.default import DefaultParameter as RollupDefaultParameter
from demo_etherlink.types.rollup.tezos_storage import RollupStorage
from dipdup.context import HandlerContext
from dipdup.models.tezos_tzkt import TzktTransaction


async def on_rollup_call(
    ctx: HandlerContext,
    controller_default: TzktTransaction[ControllerDefaultParameter, ControllerStorage],
    rollup_default: TzktTransaction[RollupDefaultParameter, RollupStorage],
) -> None:
    ctx.logger.info(
        'Smart rollup %s has been called by contract %s with parameter %s',
        rollup_default.data.target_address,
        controller_default.data.target_address,
        rollup_default.parameter.__root__,
    )