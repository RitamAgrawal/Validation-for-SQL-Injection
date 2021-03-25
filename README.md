# Flask API for sanitized inputs

## Routes

#### Home (/)

The API returns a character set containing all ascii characters.

### API

#### Check for sanitized payload (/api/v1/sanitized/input/)

Path - `/api/v1/sanitized/input/`
Type - `POST`

**Valid Input**

Sample Input

```
curl -X POST https://iu8utrspej.execute-api.us-west-2.amazonaws.com/production/api/v1/sanitized/input/ \
  --header "Content-Type: application/json" \
  --data '{"payload": "Foo"}'
```

Sample Output

```
{"result":"unsanitized"}
```

**InValid Input**

1.  Sample Input

```
curl -X POST https://iu8utrspej.execute-api.us-west-2.amazonaws.com/production/api/v1/sanitized/input/ \
  --header "Content-Type: application/json" \
  --data '{"payload": "Foo_"}'
```

Sample Output

```
{"result":"sanitized"}
```

2. Sample Input

```
curl -X POST https://iu8utrspej.execute-api.us-west-2.amazonaws.com/production/api/v1/sanitized/input/ \
  --header "Content-Type: application/json" \
  --data '{}'
```

Sample Output

```
Invalid Input. Request is missing "payload".
```

3. Sample Input

```
curl -X POST https://iu8utrspej.execute-api.us-west-2.amazonaws.com/production/api/v1/sanitized/input/ \
  --header "Content-Type: application/json" \
  --data '{"payload": "Foo",}'
```

Sample Output

```
Bad Request. Please verify your Input
```

## Unit Test

To run all unit tests recursively, execute the following command.

```
find . -name '*test.py' | sed "s|^\./||" | xargs python3 -m unittest
```
