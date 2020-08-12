from typing import List, Any
import yaml
from importlib import import_module as imp
CONFIG_FILE = "zkit.yml"
CONFIG_FILE_EX = "zkit.yaml"


class Interact:
    "Base class for zkit user-payload and zkit-action"

    def __init_subclass__(cls, required_vars: list, optional_vars: dict, **kwargs):
        cls.requireds = required_vars
        cls.optionals = optional_vars
        cls.all = [*cls.requireds, *list(cls.optionals.keys())]
        return cls

    def load_info(self, file: str) -> dict:
        if file.split('.')[-1] == "py":
            # python file to check for info
            return self._load_pyconfig(file)
        else:
            # yaml
            return self._load_yaml(file)

    def _load_yaml(self, file) -> dict:
        try:
            f = open(self.CONFIG_FILE)
        except FileNotFoundError:
            f = open(self.CONFIG_FILE_EX)
        info = yaml.full_load(f)
        f.close()
        return info

    def _load_pyconfig(self, file) -> dict:
        config = imp(file)
        return config.vars()

    def _check_for_odds(self, tocheck) -> bool:
        for m in tocheck:
            if not (m in self.all):
                raise PayloadConfigError(
                    "{} Is not reconized by ZKit".format(m))
        return True

    def _check_for_requireds(self, tocheck) -> bool:
        for r in self.requireds:
            if not (r in tocheck):
                raise PayloadConfigError(
                    "{} Is required but NOT found".format(r))
        return True

    def validate_vars(self, vars_: dict) -> dict:
        self._check_for_odds(vars_)
        self._check_for_requireds(vars_)
        base = self.optionals
        for var in vars_:
            base[var] = vars_[var]

        return base

    def table_validate(self, tovalidate: Any, typeof=None, key=None) -> bool:
        """validates data with given info

        Arguments:

            tovalidate (Any): any str, int, or anything you want to validate

            typeof (type): the key that we should get type from(Defaults = none)
            when default checks for any match in the whole key

            key (dict): the key to validate from (Defaults = self.validation_table)

            see example for more info

        Returns:
            bool : True if the 'to_validate' has the same type of the required else False
        """
        if key is None:
            key = self.validation_table
        if typeof is None:
            corr_type = tuple(key.keys())
        else:
            corr_type = table.get(typeof, str)

        return isinstance(tovalidate, corr_type)

    def interact(self):
        return NotImplemented
