To run the GUI of this project the "main.py" file should be run
This will allow the user to interact with the GUI

each of the buttons allow for the specification for what data to display, 
for example choosing the "Proposed FGG", "Energy", "Grid", and "Low" options will
display the correct selected data selected data set

The user can select between the excel data source or the SQL Server for data fetching

The scripts to create the correct SQL Tables are below:

CREATE TABLE dbo.FGGEnergySQLLowPrecisionGrid (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.FGGEnergySQLMediumPrecisionGrid (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.FGGEnergySQLHighPrecisionGrid (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.FGGEnergySQLLowPrecisionFFT (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.FGGEnergySQLMediumPrecisionFFT (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.FGGEnergySQLHighPrecisionFFT (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.LagrangeEnergySQLLowPrecisionGrid (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.LagrangeEnergySQLMediumPrecisionGrid (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.LagrangeEnergySQLHighPrecisionGrid (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.LagrangeEnergySQLLowPrecisionFFT (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.LagrangeEnergySQLMediumPrecisionFFT (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.LagrangeEnergySQLMediumPrecisionFFT (
    N, int
    Energy (V)x10^6, decimal(10, 2)
)

CREATE TABLE dbo.FGGTimeSQLLowPrecisionGrid (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.FGGTimeSQLMediumPrecisionGrid (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.FGGTimeSQLHighPrecisionGrid (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.FGGTimeSQLLowPrecisionFFT (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.FGGTimeSQLMediumPrecisionFFT (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.FGGTimeSQLHighPrecisionFFT (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.LagrangeTimeSQLLowPrecisionGrid (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.LagrangeTimeSQLMediumPrecisionGrid (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.LagrangeTimeSQLHighPrecisionGrid (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.LagrangeTimeSQLLowPrecisionFFT (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.LagrangeTimeSQLMediumPrecisionFFT (
    N, int
    Time (ms), decimal(10, 2)
)

CREATE TABLE dbo.LagrangeTimeSQLHighPrecisionFFT (
    N, int
    Time (ms), decimal(10, 2)
)