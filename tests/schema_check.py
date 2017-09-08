import os
import unittest

from snactor import loader
from pprint import pprint


class TestSchemaAvailability(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSchemaAvailability, self).__init__(*args, **kwargs)

        self.src_path = "../src"
        self.actors_path = os.path.join(self.src_path, "actors")
        self.schema_path = os.path.join(self.src_path, "schema")

    def test_actors_and_schemas(self):
        failed = False

        loader.load(self.actors_path)
        loader.load_schemas(self.schema_path)

        try:
            loader.validate_actor_types()
        except loader.ActorTypeValidationError as e:
            for (type_name, direction, actor_name) in e.data:
                print("Schema for type '{}' defined in actor '{}' section '{}' was not found"
                      .format(type_name, actor_name, direction))
            failed = True

        self.assertEqual(False, failed)

if __name__ == '__main__':
    unittest.main()
