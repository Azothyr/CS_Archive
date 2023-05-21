class ClassCreator:
    def __init__(self):
        self.upper = None
        self.mid = None
        self.lower = None

    def _customize_upper(self, *arg):
        class_name, class_attributes, self_parameters, equal_parameters, \
            private_attributes, instance_name, instance_arg_list = \
            self.variable_creator(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self.upper = self.class_upper_text(class_name, class_attributes, self_parameters, equal_parameters)

    def _customize_mid(self, *arg):
        class_name, class_attributes, self_parameters, equal_parameters, \
            private_attributes, instance_name, instance_arg_list = \
            self.variable_creator(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self.mid = self.class_mid_text()

    def _customize_lower(self, *arg):
        class_name, class_attributes, self_parameters, equal_parameters, \
            private_attributes, instance_name, instance_arg_list = \
            self.variable_creator(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self.lower = self.class_lower_text(class_name, private_attributes, instance_name, instance_arg_list)

    @staticmethod
    def variable_creator(class_name, instance_name, class_attributes, define_attr_as_class_arg, instance_parameters,
                         underscore_amount):
        if instance_name is None:
            instance_name = "my_" + str(class_name).lower()
        else:
            instance_name = str(instance_name).lower()
        private_attributes = []
        self_attributes = []
        instance_arg_list = []
        equal_list = []
        underscores = ""
        if underscore_amount > 0:
            underscores = "_" * underscore_amount
        i = 1

        for argument in class_attributes:
            private_param = f"{underscores}{argument}"
            if underscore_amount == 2:
                private_param = f"_{class_name}" + private_param
            self_param = f"self.{underscores}{argument}"
            equal_param = f" = {argument}"
            private_attributes.append(private_param)
            self_attributes.append(self_param)
            equal_list.append(equal_param)
            if instance_parameters is None and define_attr_as_class_arg is True:
                instance_arg_list.append(str(i))
                i += 1

        if not define_attr_as_class_arg:
            class_attributes = None

        if instance_parameters:
            formatted_attributes = ", ".join(repr(param) for param in instance_parameters) \
                if instance_parameters else ""
            instance_arg_list = formatted_attributes
        else:
            instance_arg_list = ", ".join(instance_arg_list)
        return class_name, class_attributes, self_attributes, equal_list, private_attributes, instance_name, \
            instance_arg_list

    @staticmethod
    def class_upper_text(class_name, class_parameters, self_attributes, equal_attributes):
        attribute_list = []
        length = len(self_attributes)

        if class_parameters is not None:
            class_parameters = ", " + ", ".join(class_parameters)
            for i in range(length):
                new_value = self_attributes[i] + equal_attributes[i]
                attribute_list.append(new_value)

        else:
            class_parameters = ""
            for attr in self_attributes:
                new_value = attr + " = "
                attribute_list.append(new_value)

        text = ("class {class_name}:\n"
                "    def __init__(self{class_parameters}):\n"
                "        {self_attributes}\n").format(
            class_name=class_name,
            class_parameters=class_parameters,
            self_attributes="\n        ".join(attribute_list))
        return text

    @staticmethod
    def class_mid_text():
        text = "\n\n"
        return text

    @staticmethod
    def class_lower_text(class_name, private_attributes, instance_name, attributes):
        text = ("{instance_name}_attributes = {private_attributes}\n"
                "{instance_name} = {name}({attributes})\n"
                "for attribute in {instance_name}_attributes:\n"
                "    value = getattr({instance_name}, attribute)\n"
                "    print(value)").format(
            name=class_name,
            private_attributes=private_attributes,
            instance_name=instance_name,
            attributes=attributes)
        return text

    def run_creator(self, *arg):
        self._customize_upper(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self._customize_mid(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self._customize_lower(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])

        complete_text = "{upper}{mid}{lower}".format(
            upper=self.upper,
            mid=self.mid,
            lower=self.lower)
        return complete_text

    def create_class(self, class_name, instance_name, class_attributes, define_attr_as_class_arg,
                     instance_parameters, underscore_amount):

        return self.run_creator(class_name, instance_name, class_attributes, define_attr_as_class_arg,
                                instance_parameters, underscore_amount)


class GetSetFunction(ClassCreator):
    def __init__(self):
        super().__init__()

    def _customize_mid(self, *arg):
        class_name, class_attributes, self_parameters, equal_parameters, \
            private_attributes, instance_name, instance_arg_list = \
            self.variable_creator(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self.mid = self.class_mid_text(class_attributes, self_parameters)

    def _customize_lower(self, *arg):
        class_name, class_attributes, self_parameters, equal_parameters, \
            private_attributes, instance_name, instance_arg_list = \
            self.variable_creator(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self.lower = self.class_lower_text(class_name, class_attributes, instance_name, instance_arg_list)

    @staticmethod
    def class_mid_text(class_attributes, self_parameters):
        text_list = []
        i = 0

        for attr in class_attributes:
            part = ("    def get_{attribute}(self):\n"
                    "        return {self_attribute}\n"
                    "\n"
                    "    def set_{attribute}(self, new_value):\n"
                    "        {self_attribute} = new_value\n").format(attribute=attr,
                                                                     self_attribute=self_parameters[i])
            i += 1
            text_list.append(part)

        text = "{get_set}\n\n".format(get_set="\n".join(text_list))
        return text

    @staticmethod
    def class_lower_text(class_name, class_attributes, instance_name, instance_arg_list):
        return_value1 = []
        return_value2 = []
        for attribute in class_attributes:
            value = "{attribute} = property(get_{attribute}, set_{attribute})\n".format(attribute=attribute)
            return_value1.append(value)

        for attribute in class_attributes:
            value = "print({instance_name}.{attribute})\n".format(instance_name=instance_name, attribute=attribute)
            return_value2.append(value)

        text = "\n    {property}\n{instance_name} = {class_name}({instance_arg_list})\n{print}".format(
            class_name=class_name,
            instance_name=instance_name,
            property="    ".join(return_value1),
            print="".join(return_value2),
            instance_arg_list="".join(instance_arg_list))
        return text

    def create_class(self, *arg):
        return super().create_class(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])


class GetSetProperty(ClassCreator):
    def __init__(self):
        super().__init__()

    def _customize_mid(self, *arg):
        class_name, class_attributes, self_parameters, equal_parameters, \
            private_attributes, instance_name, instance_arg_list = \
            self.variable_creator(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self.mid = self.class_mid_text(class_attributes, self_parameters)

    def _customize_lower(self, *arg):
        class_name, class_attributes, self_parameters, equal_parameters, \
            private_attributes, instance_name, instance_arg_list = \
            self.variable_creator(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])
        self.lower = self.class_lower_text(class_name, class_attributes, instance_name, instance_arg_list)

    @staticmethod
    def class_mid_text(class_attributes, self_parameters):
        text_list = []
        i = 0

        for attr in class_attributes:
            part = ("    @property\n"
                    "    def {attribute}(self):\n"
                    "        return {self_attribute}\n"
                    "\n"
                    "    @{attribute}.setter\n"
                    "    def {attribute}(self, new_value):\n"
                    "        {self_attribute} = new_value\n").format(attribute=attr,
                                                                     self_attribute=self_parameters[i])
            i += 1
            text_list.append(part)

        text = "{property}".format(property="\n".join(text_list))
        return text

    @staticmethod
    def class_lower_text(class_name, class_attributes, instance_name, instance_arg_list):
        return_value = []

        for attribute in class_attributes:
            value = "{instance_name}.{attribute}(\"test\")\nprint({instance_name}.{attribute})\n" \
                .format(instance_name=instance_name, attribute=attribute)
            return_value.append(value)

        text = "\n{instance_name} = {class_name}({instance_arg_list})\n{print}".format(
            instance_name=instance_name,
            class_name=class_name,
            print="".join(return_value),
            instance_arg_list="".join(instance_arg_list))

        return text

    def create_class(self, *arg):
        return super().create_class(arg[0], arg[1], arg[2], arg[3], arg[4], arg[5])


def main(class_to_instance=ClassCreator(),
         class_name="Default",
         class_attributes=None,
         instance_name=None,
         instance_parameters=None,
         define_attr_as_class_arg=True,
         underscore_amount=0):
    my_class = class_to_instance
    if my_class == "GetSetFunction" or "GetSetProperty":
        if underscore_amount == 0:
            underscore_amount = 1

    print(my_class.create_class(class_name, instance_name,
                                class_attributes, define_attr_as_class_arg,
                                instance_parameters, underscore_amount))


if __name__ == "__main__":
    main(GetSetProperty(),
         "Dancer",
         ["name", "nationality", "style"],
         None,
         ["Savion Glover", "American", "tap"],
         True,
         0)
