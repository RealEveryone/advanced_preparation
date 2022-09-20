from project.space_station import SpaceStation

space_station = SpaceStation()
biologist = space_station.add_astronaut('Biologist', 'Georgi')
astrologist = space_station.add_astronaut('Meteorologist', 'Mario')
shibaniq_gei = space_station.add_astronaut('Biologist', 'Toshko')
space_station.add_planet('MulhoLandiq', ['Kartofi', 'Domati', 'Chushki', 'MalkoDjigubile'])
space_station.send_on_mission('MulhoLandiq')
space_station.report()
