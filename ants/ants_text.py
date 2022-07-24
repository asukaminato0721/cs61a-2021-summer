from ants_strategies import start_with_strategy
from utils import *

import ants
from ants import *


@main
def run(*args):
    Insect.reduce_health = class_method_wrapper(
        Insect.reduce_health, pre=print_expired_insects
    )
    start_with_strategy(args, interactive_strategy, ants)
