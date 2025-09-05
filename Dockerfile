# Stage 1: Builder Stage
# Use a slim Python image to minimize base attack surface
FROM python:3.9-slim AS builder

# Create a non-root user and group for security (principle of least privilege)
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR /app

# Copy only requirements.txt first for better caching
COPY requirements.txt .

# Install Python dependencies in a virtual environment
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2: Final Stage
# Use a fresh, clean Python slim image to exclude build tools and reduce attack surface
FROM python:3.9-slim AS final

# Copy the non-root user and group from builder stage
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

# Copy the installed Python dependencies from builder stage
COPY --from=builder /opt/venv /opt/venv

# Set environment to use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

COPY . .

# Run the database setup script
RUN python setup_db.py

# Change ownership of the application directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user to prevent running as root
USER appuser

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]