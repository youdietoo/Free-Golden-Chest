from mods_base import build_mod, hook
from unrealsdk.hooks import Type, Block

GOLDEN_KEY_CURRENCY = 3

@hook("WillowGame.WillowInteractiveObject:Behavior_ChangeUsabilityCost", Type.PRE)
def change_cost(obj, args, ret, func):
    if int(args.CostType) == GOLDEN_KEY_CURRENCY:
        args.CostAmount = 0
        args.CostType = 0
        args.ChangeType = 0

        return Block

mod = build_mod()