# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
#session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

    
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query
    #date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    date = dt.date(2017, 8, 23)
    query_date = date - dt.timedelta(days=365)
    
    results = session.query(Measurement.prcp,\
                        Measurement.date).\
                  filter(Measurement.date > query_date).all()

    # Close session
    session.close()

    # converting results to list using for loop
    recent_measurements = []
    for prcp, date in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        
        #append list w/ dictionaries
        recent_measurements.append(measurement_dict)

    # return jsonified results to page
    return jsonify(recent_measurements)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query
    results = session.query(Station.station, Station.name).all()

    # Close session
    session.close()

    # converting results to list using for loop
    stations = []
    for station, name in results:
        station_dict = {}
        station_dict["station"] = station
        station_dict["name"] = name
        
        #append list w/ dictionaries
        stations.append(station_dict)
    
    # return jsonified results to page
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query
    #date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    date = dt.date(2017, 8, 23)
    query_date = date - dt.timedelta(days=365)

    temperatures = session.query(Measurement.tobs, Measurement.date).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date > query_date).all()

    # Close session
    session.close()

    # converting temperatures to list using for loop
    temps = []
    for temp, date in temperatures:
        temps_dict = {}
        temps_dict['date'] = date
        temps_dict['temp'] = temp

        #append list w/ dictionaries
        temps.append(temps_dict)

    # return jsonified results to page
    return jsonify(temps)   



#@app.route("/api/v1.0/<start>") and @app.route(/api/v1.0/<start>/<end>)

#TMIN, TAVG, and TMAX



if __name__ == '__main__':
    app.run(debug=True)