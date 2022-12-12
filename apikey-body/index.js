/*
 * This is an HTTP based Thing implementation that implements the following assertions of the TD specification
 * sec-body-name-json-pointer : When used in the context of a body security information location, the value of name MUST be in the form of a JSON pointer [[!RFC6901]] relative to the root of the input DataSchema for each interaction it is used with.
 * sec-body-name-json-pointer-array : The JSON pointer used in the body locator MAY use the "-" character to indicate a non-existent array element when it is necessary to insert an element after the last element of an existing array.
 * sec-body-name-json-pointer-creatable : When an element of a data schema indicated by a JSON pointer indicated in a body locator does not already exist in the indicated schema, it MUST be possible to insert the indicated element at the location indicated by the pointer.
 * sec-body-name-json-pointer-type : The element referenced (or created) by a body security information location MUST be required and of type "string".
 * 
 * Basically, three actions use an apikey scheme in different ways. One expects it at a certain field in an object, 
 * one expects it appended to the object and the other expects it appended to the array
*/

import express from 'express';
import fs from 'fs';

const app = express()
app.use(express.json())
const port = 8080
const superSecretApiKey = "amazingKey"

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.split(search).join(replacement);
};

const currentLocation = {
    x: 0,
    y: 0,
    z: 0
}

app.get('/location', (req, res) => {
    res.status(200).send({ value: currentLocation })
})

app.post('/actions/moveTo1', (req, res) => {
    // console.log(req.body)
    const requestedLocation = {
        x: req.body.x,
        y: req.body.y,
        z: req.body.z
    }

    if(req.body.keyLocation){
        if (req.body.keyLocation===superSecretApiKey){
            setTimeout(() => {
                console.log("Moving to",requestedLocation)
                res.status(200).send()
            }, 1000)
        } else {
            console.log("Wrong API Key")
            res.status(401).send()
        }
    } else {
        console.log("Missing API Key")
        res.status(401).send()
    }
})

app.post('/actions/moveTo2', (req, res) => {
    console.log(req.body)
    const requestedLocation = {
        x: req.body.x,
        y: req.body.y,
        z: req.body.z
    }

    if(req.body.keyLocationInvisible){
        if (req.body.keyLocationInvisible===superSecretApiKey){
            setTimeout(() => {
                console.log("Moving to",requestedLocation)
                res.status(200).send()
            }, 1000)
        } else {
            console.log("Wrong API Key")
            res.status(401).send()
        }
    } else {
        console.log("Missing API Key")
        res.status(401).send()
    }
})

app.post('/actions/moveInSequence', (req, res) => {
    console.log(req.body)
    const requestedLocation1 = {
        x: req.body[0].x,
        y: req.body[0].y,
        z: req.body[0].z
    }
    const requestedLocation2 = {
        x: req.body[1].x,
        y: req.body[1].y,
        z: req.body[1].z
    }

    if(req.body[2]){
        if (req.body[2]===superSecretApiKey){
            setTimeout(() => {
                console.log("Moving to",requestedLocation1)
                setTimeout(() => {
                    console.log("Moving to",requestedLocation2)
                    res.status(200).send()
                }, 1000)
            }, req.body[0].pause)
        } else {
            console.log("Wrong API Key")
            res.status(401).send()
        }
    } else {
        console.log("Missing API Key")
        res.status(401).send()
    }
})

app.get('/td', (req, res) => {
    console.log("request for td")
    const bodyRaw = fs.readFileSync('./robot.td.jsonld', 'utf-8');
    const bodyTEXT = bodyRaw.replaceAll('${port}', port);
    const body = JSON.parse(bodyTEXT)
    res.status(200).send(body)
})

app.listen(port, async() => {
    console.log(`APIkey Secured Robot listening at http://localhost:${port}`)
})
