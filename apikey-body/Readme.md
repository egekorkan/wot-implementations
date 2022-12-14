# Robot using API Key Authentication

Some requests you can send

- Location Property

`curl "http://localhost:8080/location"` -> No API Key

`curl "http://localhost:8080/amazingKey12/location"` -> Wrong API Key

`curl "http://localhost:8080/amazingKey/location"` -> Correct

- MoveTo1 Action

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveTo1" --data-binary "@moveTo1.valid.json"`

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveTo1" --data-binary "@moveTo1.invalid1.json"`

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveTo1" --data-binary "@moveTo1.invalid2.json"`

- MoveTo2 Action

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveTo2" --data-binary "@moveTo2.valid.json"`

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveTo2" --data-binary "@moveTo2.invalid1.json"`

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveTo2" --data-binary "@moveTo2.invalid2.json"`

- MoveInSequence Action

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveInSequence" --data-binary "@moveInSequence.valid.json"`

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveInSequence" --data-binary "@moveInSequence.invalid1.json"`

`curl -X POST -H "Content-Type: application/json" "http://localhost:8080/actions/moveInSequence" --data-binary "@moveInSequence.invalid2.json"`