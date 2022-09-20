from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @classmethod
    def add_to_hardware(cls, hardware):
        cls._hardware.append(hardware)

    @classmethod
    def add_to_software(cls, software):
        cls._software.append(software)

    @classmethod
    def find_hardware_by_name(cls, given_name):
        for hardware in cls._hardware:
            if hardware.name == given_name:
                return hardware
        return None

    @classmethod
    def find_software_by_name(cls, given_name):
        for software in cls._software:
            if software.name == given_name:
                return software
        return None

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hardware = PowerHardware(name, capacity, memory)
        System.add_to_hardware(power_hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System.add_to_hardware(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return f'Hardware does not exist'
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System.add_to_software(express_software)

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware = System.find_hardware_by_name(hardware_name)
        if hardware is None:
            return f'Hardware does not exist'
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System.add_to_software(light_software)

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware = System.find_hardware_by_name(hardware_name)
        software = System.find_software_by_name(software_name)

        if hardware and software:
            hardware.uninstall(software)
            System._software.remove(software)
            return
        return 'Some of the components do not exist'

    @staticmethod
    def analyze():
        memory_usage = [x.memory_consumption for x in System._software]
        total_memory = [x.memory for x in System._hardware]

        capacity_usage = [x.capacity_consumption for x in System._software]
        total_capacity = [x.capacity for x in System._hardware]

        output = 'System Analysis\n'
        output += f'Hardware Components: {len(System._hardware)}\n'
        output += f'Software Components: {len(System._software)}\n'
        output += f'Total Operational Memory: {sum(memory_usage)} / {sum(total_memory)}\n'
        output += f'Total Capacity Taken: {sum(capacity_usage)} / {sum(total_capacity)}'

        return output.strip()

    @staticmethod
    def system_split():
        output = ''
        for hardware in System._hardware:
            express_software_count = len([x for x in hardware.software_components if x.software_type == "Express"])
            light_software_count = len([x for x in hardware.software_components if x.software_type == "Light"])

            memory_used = sum([x.memory_consumption for x in hardware.software_components])
            capacity_used = sum([x.capacity_consumption for x in hardware.software_components])
            string = 'None'
            if hardware.software_components:
                string = ', '.join(x.name for x in hardware.software_components)

            output += f"Hardware Component - {hardware.name}\n"
            output += f'Express Software Components: {express_software_count}\n'
            output += f'Light Software Components: {light_software_count}\n'
            output += f'Memory Usage: {memory_used} / {hardware.memory}\n'
            output += f'Capacity Usage: {capacity_used} / {hardware.capacity}\n'
            output += f'Type: {hardware.hardware_type}\n'
            output += f'Software Components: {string}\n'

        return output.strip()
