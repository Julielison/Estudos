package org.grails.guides

import grails.gorm.services.Service

@Service(Vehicle)
interface VehicleService {
    Vehicle save(String type, Make make, Model model, Integer year)
}