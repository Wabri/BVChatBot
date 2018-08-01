# coding=utf-8
import requests
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.featurizers import (
    MaxHistoryTrackerFeaturizer,
    BinarySingleStateFeaturizer)
import json

from actions.ActionGreetings import ActionGreetings

from actions.ActionPaymentTracker import ActionPaymentTracker

from actions.ActionRequestListAccount import ActionRequestListAccount

from actions.ActionRequestTotalAccountValue import ActionRequestTotalAccountValue

from actions.ActionGoodbye import ActionGoodbye