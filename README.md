<img align="right" src="/icons/logo.png" width="110">
<h1>MasterPlan</h1>
An automatic event scheduling desktop application.

-----------------

<br>

### Run Instructions:
*Python 3.7 (or higher, but not tested) is required*
1. Run `pip install PySide2` (make sure it is installed on the python installation that will be used to build the project).
2. Clone the project from the Github repository.
3. On the command line (Windows) or terminal (Mac, Linux) navigate to the project's folder.
4. Execute the command `python -u main.py`

*In case there is a problem with installing the required libraries we included a demonstrative video of all the implemented functions in the main repos folder.*

<br>

### Log In Instructions:
<img align="left" src="/screenshots/login.png" width="450">
1. Enter organization using example organization "upatras".
<br>
2. There are two possible actions:
<br>
   a) Enter as __admin__ using username "upatras" and password "1".
<br>
   b) Enter as organizer using username "makris" and password "1" OR username "alexiou" and password "1".
<br>
3. Switch between Grid and Calendar View using the respective buttons.
<br>
4. Select the edit button (pencil) after you log in to enter Edit Mode.
<br>
5. Clicking the search button on the right opens a search window that can be used to search for an event from the event list.

<br><br>

### Grid View Instructions:
<img align="left" src="/screenshots/grid_view.png" width="450">
1. In Grid View select the building to enter from the grid.
<br>
2. After the rooms load in the grid, select a blue room to see its current event information. If the room is grey, there is currently no event being held.
<br>
3. Change floor using arrows in the floor spin box at the bottom of the grid.
<br>
4. Change building by selecting the "Go Back to Buildings" button at the bottom or the "Selected Building" drop down menu at the top.
<br>
5. Select a filter using the filter drop down menu.

<br><br>

### Calendar View Instructions:
<img align="left" src="/screenshots/calendar_view.png" width="450">
1. In Calendar View select a blue date from the calendar to see the events scheduled for that day. If the date is gray, there is no event scheduled for that day yet. Default date selected is today's date.
<br>
2. After selecting a date, double click an event from the list in the right to see its information.
<br>
3. Change building using the "Selected Building" Menu.
<br>
4. Select a filter using the filter drop down menu.
<br>
5. Download the calendar by selecting the download button at the bottom left.
<br>
6. Select a range for the calendar to be downloaded and click "ok" and then "yes". *(Currently no downloading happens)*

<br><br>

### Edit Mode Instructions (Admin):
<img align="left" src="/screenshots/admin.png" width="450">
1. On the Event List choose to Create Organizer.
<br>
2. On the pop-up Window type the name and email address for the new Organizer and finalize your action by clicking OK.
<br>
3. At this point, the new organizer's credentials will be printed on the python console. You can use these later to log in as the organizer you created.
<br>
4. On Event List choose Create Event and enter the Name, Duration, Room Group and select all Tags that correspond to the new event and click save.
<br>
5. On the list of events, by selecting an event, you can view details on the scheduled time and place as well as the event's assigned organizer and the lists of constraints - if any exist.
<br>
6. Click on your previously created event and select Assign in order to assign an organizer to the event.
<br>
7. Choose one from the list appearing on the pop-up window and assign them to the event. You can choose the organizer you created on the previous steps.
<br>
8. You can also choose to add a Tag to the selected event. This can be a tag that is completely new and was not offered before during the event's creation.
<br>
9. At this point you can click Execute Scheduling to run the scheduling algorithm and create a new schedule for all events. *This step exposes a known bug that removes the organizers' association with all events and should be skipped for the following instructions to run smoothly!*

<br><br>

### Edit Mode Instructions (Organizer):
*If you are following these instructions after following the previous ones as admin, you could login as the new organizer you created previously.*
<br>

<img align="left" src="/screenshots/organizer.png" width="450">
1. Select an event on the Event List. The constraints corresponding to the chosen event appear on the Event Details section.  
<br>
2. In the Time Constraint field select the add button.
<br>
3. On the pop-up window select the start/end dates and the repetition.
<br>
4. Set weight to ‘low’, ‘medium’ or ‘high’ on the slider and then choose Add to save the new constraint.
<br>
5. In the Tag Constraint field, select one of the tags appearing on the pop-up window, along with its weight and save your   
actions.
<br>
6. In the Space Constraint field, fill the expected capacity of the event and update the constraint.
