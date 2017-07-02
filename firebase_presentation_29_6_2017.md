# Firebase Presentation
## June 28, 2017

What is Firebase?
- Realtime database, 
- And other things that make development easier for developers

The focus of this talk is primarily on database. 

Firebase DB authenticates uses rules. 

What does "serverless" mean?
- Firebase traditionally no backend server code
- Serverless--> Servers exist but you're just not managing them the *cloud* manages them. 

Cloud Functions for Firebase
- npm -environemtn runs in coloud
- Integrated with firebase
- rtdb, auth, storage, https
- decoupling of serverside and clientside logic
- remeber to handle errors, always assume server will fail

Functions part of console. 

Functions can be called on Demand. 
- https trigger

### Key Architectual Takeaways
1. Decoupling logic
   a. UI is indpendent of server
   b. database as API?-->Cutting out the middle man (no long trip between ) 
2. Server is secret. 
   - Server lives behind Google. 
   - You do not have to worry about users twisting or manipulating detail

 ### More Complicated Example:
 Stripe Integration--->Via functions we can access a third-party API. 

Memory cost per operation.

Billing not based on memory but based on number of calls. 

async pipe, token, serverless, real-time database

functions

