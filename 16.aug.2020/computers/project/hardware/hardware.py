from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if software.memory_consumption > self.memory \
                or software.capacity_consumption > self.capacity:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def memory_used(self):
        result = 0
        for software in self.software_components:
            result += software.memory_consumption
        return result

    def capacity_usage(self):
        result = 0
        for software in self.software_components:
            result += software.capacity_consumption
        return result

    def details(self):
        express_software_count = len([soft for soft in self.software_components if soft.software_type == 'Express'])
        light_software_count = len([soft for soft in self.software_components if soft.software_type == 'Light'])

        all_software_components = 'None'
        if len(self.software_components) > 0:
            all_software_components = ', '.join([soft.name for soft in self.software_components])

        output = [f"Hardware Component - {self.name}",
                  f'Express Software Components: {express_software_count}',
                  f'Light Software Components: {light_software_count}',
                  f'Memory Usage: {self.memory_used()}/{self.memory}',
                  f'Capacity Usage: {self.capacity_usage()}/{self.capacity}',
                  f'Type: {self.hardware_type}',
                  f'Software Components: {all_software_components}']
        return '\n'.join(output)
