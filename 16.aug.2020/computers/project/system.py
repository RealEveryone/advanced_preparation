from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def return_hardware_if_exists(given_name):
        for hardware in System._hardware:
            if hardware.name == given_name:
                return hardware
        return None

    @staticmethod
    def return_software_if_exists(given_name):
        for software in System._software:
            if software.name == given_name:
                return software
        return None

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.return_hardware_if_exists(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        result = hardware.install(software)
        System._software.append(software)
        return result

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.return_hardware_if_exists(hardware_name)
        if hardware is None:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        result = hardware.install(software)
        System._software.append(software)
        return result

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.return_hardware_if_exists(hardware_name)
        software = System.return_software_if_exists(software_name)
        if hardware is None or software is None:
            return "Some of the components do not exist"
        System._software.remove(software)
        hardware.uninstall(software)

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
            details = hardware.details()
            output += details + '\n'

        return output.strip()
