#!/usr/bin/ruby -rubygems
# subscribe to climate topics and write text file to be read by py3status module
# 2014-07-20 alarmschaben

require 'mqtt'

topicTempOutside = '/nest/balcony/temperature'
topicHumOutside = '/nest/balcony/humidity'
topicTempLivingroom = '/nest/aquarium/temp/ambient'

filename = '/tmp/mqtemps.txt'
m = MQTT::Client.connect('lallapi')
m.subscribe('/nest/balcony/+')
m.subscribe(topicTempLivingroom)


keepgoing = true
outsideTemperature = "-"
outsideHumidity = "-"
livingroomTemperature = "-"

f = File.open(filename, 'w')
f.write('--.-°C/--%/--.-°C')
f.close


while keepgoing
  Signal.trap("TERM") do
    keepgoing = false
  end

  Signal.trap("INT") do
    keepgoing = false
  end
  if ! m.queue_empty?
    topic, message = m.get
    if (topic == topicTempOutside)
      outsideTemperature = message
    elsif (topic == topicHumOutside)
      outsideHumidity = message
    elsif (topic == topicTempLivingroom)
      livingroomTemperature = message
    end
    f = File.open(filename, 'w') 
    filestring = outsideTemperature + '°C/' + outsideHumidity + '%/' + livingroomTemperature + '°C'
    f.write(filestring)
    f.close
  else
    sleep 3
  end
end

m.close
