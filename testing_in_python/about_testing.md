## Notes about testing software in general

#### Automated vs. Manual testing

###### Manual

- You've probably already performed tests without realizing it
  - opening up your application to see if things are functioning correctly
  - experimenting with features to see how they perform
- _Exploratory testing_ - a form of manual testing that is done without a plan, you're just exploring the application
  - Are components formatted correctly?
  - Are features functioning the way you designed?
- _Manual testing_ involves testing each individual feature by hand
  - providing input to to features and observing output
  - **very tedious**
    - have to insert test cases and edge cases by hand for each individual feature and visually check for expected results
    - every time you make changes to your code, you need to redo ^ to make sure nothing has broken and everything is still functioning as designed

###### Automated

- Automated testing - the execution of your test plan (the parts of code/features you want tested, the order to test them, and expected responses) by a script instead of manually (by a human).
- automated tests are designed to simply test if a specific function or series of functions is producing the expected outputs
- Python includes a built-in set of tools/libs to help you creat automated tests

#### Unit vs. Integration test

- Think about testing the audio on some speakers at home.
  - Turn stereo on (**test step**)
  - Press play on device (or drop needle on vinyle if you're really cool) (**test step**)
  - Is music coming out of speakers? (**test assertion**)
- Testing multiple components is called **integration testing**
  - problem with integration testing is that when a full integration test fails, it can be difficult to diagnose which component is failing
    - ex: if no music is playing, is it because the stereo is broken? cables/wires not connected? audio source not working properly (record/CD player, mobile device)?
- Checking if the song is actually playing on your phone (unplugging aux and playing from phone speakers), for instance, would be a form of **unit testing**
- **Unit test** - a smaller test that checks if a single component is operating in the right way.

Simply put:

- integration test checks that components in application operate with eachother correctly
- unit test checks a small component of application
