# Dockerfile for Next.js Frontend

# Step 1: Build the Next.js app
FROM node:23 AS build

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the Next.js app files and build the app
COPY . ./
RUN npm run build

# Step 2: Serve the Next.js app using a production server (Next.js built-in)
FROM node:23

WORKDIR /app

# Copy the build from the build stage
COPY --from=build /app /app

# Expose the port (default Next.js port)
EXPOSE 3000

# Run the Next.js production server
CMD ["npm", "start"]
