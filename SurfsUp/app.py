# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(bind=engine)

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
    date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    query_date = date - dt.timedelta(days=365)
    
    results = session.query(Measurement.prcp, 
                        Measurement.date).\
                  filter(Measurement.date > query_date).all()

    session.close()

    recent_measurements = []
    for prcp, date in results:
        measurement_dict = {}
        measurement_dict["name"] = name
        measurement_dict["age"] = age
        
        measurements.append(recent_measurements)

    return jsonify(measurements)

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)

#@app.route("/api/v1.0/stations")
session.query(func.count(Station.station)).all()

session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).all()

#@app.route("/api/v1.0/tobs")

temperatures = session.query(Measurement.tobs, func.count(Measurement.tobs)).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date > query_date).\
    group_by(Measurement.tobs).all()

#@app.route("/api/v1.0/<start>") and @app.route(/api/v1.0/<start>/<end>)

#TMIN, TAVG, and TMAX

if __name__ == '__name__':
    app.run(debug=True)