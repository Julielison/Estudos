package org.grails.guides

@SuppressWarnings('GrailsDomainReservedSqlKeywordName')
class Vehicle {
    String name
    Make make
    Model model
    Integer year

    static constraints = {
        name nullable: false, blank: false
        make nullable: false
        model nullable: false
        year nullable: false, min: 1886
    }
}