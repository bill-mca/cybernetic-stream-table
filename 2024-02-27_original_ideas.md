
## CPS

### Idea 1: Cybernetic Stream Table

 - The idea is to give people a direct experience of emergent phenomena.
 - The stream must meander.
 - choices that the user makes should determine the flow regime of the stream.
 - If the player makes bad choices, the flow rates get more variable.
 - Players might compete against each other in a settlers of Catan type of game. The more farm houses you build, the more money you have.
 - Farmhouses earn at a rate inversely proportional to their proximity to other farm houses.
 - It'd be cool if players were allowed to place new buildings out of turn. The competition wouldn't necessarily be obligatory.
 - Players could define their own objectives. Bankrupting the other player might be one objective. Earning as much money as possible might be another. The game wouldn't give people the objective but let them play with this mechanic themselves

#### Physical
 - water
 - Modelling media or sand
 - symbolic components for players to add as part of the game
 - pump and valves
 - flow meters
 - (opt) projector

#### Digital
 - data on the rate of flow at the inlet
 - data on the rate of flow at the outlet
 - (opt) A digital twin of the sandbox
 - game state

#### Calculaion
 - The stream calculates the balance of impelling and resisting forces
 - (opt) calculation of a DEM to map where erosion or deposition has happened
 - (opt)comparison of instantaneous flow rates at the inlet and outlet
 - Computer vision to recognise which moves the players have made
 - scores for the players

#### Concerns:
 - WILL MORE VARIABLE FLOWS RESULT IN GREATER GEOMORPHIC INSTABILITY?
 - Will the game just result in hostility to nature?
 - Will there be ways to hack through the meandering?
 - Will the link between the state of play and the variability of the flow rate make sense to players?
 - How wold you prevent players from drastically modifying the landforms?
    - I reckon making the medium quite sensitive to manipulation so that players naturally realise that they can't manage this.  
 - Would players just dig channels to redirect the river towards each other's houses?
 - Would players just build offline storages?
 - How will you make it clear that a
 - Will some parts of the board just naturally be wetter than others?
 - Will all the medium just slide to the bottom of the tank?

#### Timeline:
*Steps:*
 1. Co-design the concept with partners.
 2. Start experimenting with media. If you can't get good meandering to happen then you should just give up on the idea.
 3. Prototype the design of the trough and the media. Initially, flow from the bottom to the top will just be done manually with a bucket.
 4. Write OpenCV code to count the number of coloured shapes in an image.
 5. Write OpenCV code to detect the proximity of a coloured shape to the blue stream.
 6. Write an interactive python script to automatically keep score based on the OpenCV part.
 7. Make a rig to point the camera at the board.
 8. Success! this is the minimum adequate to get the message across.
 9. Finalise the design of the trough and the media.
 10. Implement flow gauges and electronically controlled valves and pumps on the stream table.
 11. Write python code to monitor and stochastically control the discharge of the simulated river. 
 12. Success! This is an advanced version of the game that emphasises the power of nature instead of the agency of humans.
 13. Present to partners.

Deadlines:
 - Step 1: 27th of March
        (one week - 2)
 - Step 2: 7th of April
        (two weeks - 3, 4, 5)
 - Step 5: 21st of April
        (3 weeks - 6, 7)
 - Step 8: 12th of May
        (two weeks - 9, 10, 11)
 - Step 12: 30th of May



### Idea 2: Computer vision stream gauges
The basic concept is to explore decentralisation of hydrological monitoring. I believe that technology has the potential to give community organisations greater agency in environmental management. automated stream gauges, and hence substantial stream gauging datasets, are currently restricted to the outlets of large catchments. This means that data on the impact of changes to land management on the behaviour of natural streams is non-existant.

Other ideas:
1. A sandbox stream table with depth perception cameras and a projector. The projector shows the biological response to human intervention. The computer also controls the rate of inflow. It analyses the hydrograph of your catchment after each flood and assumes that the upstream catchment is functioning the same way that your section does. 
2. Using precision GPS with drones to create weed maps. Making the models public.
3. Using drones to create automated photo-monitoring routines
4. Splicing historic aerial images together to make a historical map. Then adding any historical accounts or photos This isn't really a physical system and it isn't sensing the real world. I put it here as a starting point for thinking about a project about environmental histories.
5. A cheap water quality gauge.

#### Physical
 - The streams that I will be monitoring.
 - The camera.
 - A waterproof and solar-powered raspberry pi.

#### Digital
 - A photo monitoring dataset.
 - A timeseries of stream stage.
 - (optional) A timeseries of stream velocity.

#### Computational
 - Computer vision algorithms that translate one form of data into another. 
 - An easy way of visualising the data and downloading it.
 - (opt) support for analysing the data against other hydrological or meterological datasets for decision making. This might be a collaborative dataset where citizen-science data from all the stream gauges that we deploy is pulled together in a comparable form and analysed.
