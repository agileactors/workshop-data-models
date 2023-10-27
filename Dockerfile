# Use the official PostgreSQL image
FROM postgres:latest

# Set environment variables, similar to .env.variables file
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB mydatabase

# Expose the PostgreSQL port
EXPOSE 5432
