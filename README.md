# OrderOwl

OrderOwl is a food delivery system chatbot designed to simplify the process of ordering food and tracking orders seamlessly through a conversational interface.

## Scope of Work - SOW

### New Order
- Allow users to place new orders directly within the chatbot.
- Support payment through the chatbot for added convenience.

### Track Order
- Enable users to track the status of their orders using either the order ID or their customer name.

### Offers/Store House
- Provide information about ongoing and upcoming offers to users.
- Showcase available items in the storehouse.

## Backlog

### New Order
1. Implement the functionality to place a new order.
2. Integrate support for payment processing through the chatbot.

### Track Order
1. Develop the capability to track orders by order ID.
2. Implement order tracking by customer name.

### Offers/Store House
1. Display ongoing offers to users.
2. Notify users about upcoming offers.
3. Showcase available items in the storehouse.

## MVP

The Minimum Viable Product (MVP) includes:
1. Ability to place a new order.
2. Capability to track orders by order ID.

## Phase 2

Phase 2 of development will focus on enhancing the chatbot's functionality:
- Support payment through the chatbot.
- Enable tracking orders by customer name.
- Display ongoing and upcoming offers.
- Showcase available items in the storehouse.

## Chatbot Platform

OrderOwl is built using Dialogflow, a powerful natural language understanding platform provided by Google.

## Dialogflow Setup

### Define Intents, Context & Fulfillment

#### Intents
- **neworder**: Intent to initiate a new order.
- **order add**: Intent to add items to an existing order.
- **order remove**: Intent to remove items from an existing order.

#### Fulfillment
- Implement a webhook that connects to a backend to create new orders and track existing orders.

## Build Backend

The backend of OrderOwl is developed using FastAPI, Flask, Django, or Node.js, depending on the project requirements. It is responsible for managing the business logic and communication with the database.

## Website Integration

OrderOwl is seamlessly integrated into our self-designed food website, providing users with a unified experience for browsing menu items, placing orders, and tracking deliveries.

With OrderOwl, we aim to revolutionize the food delivery experience, making it more accessible and convenient for users while streamlining operations for businesses.
