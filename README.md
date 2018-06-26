# st2_test_unicode

```
root@3e837b4b137b:/# st2 run test.pass_unicode_output1
.
id: 5b323aec88bcb100e9f8e7c1
action.ref: test.pass_unicode_output1
parameters: None
status: succeeded
result_task: task1
result:
  exit_code: 0
  result: Rue de la Défense
  stderr: ''
  stdout: ''
start_timestamp: Tue, 26 Jun 2018 13:09:00 UTC
end_timestamp: Tue, 26 Jun 2018 13:09:01 UTC
+--------------------------+------------------------+-------+------------------+------------------------+
| id                       | status                 | task  | action           | start_timestamp        |
+--------------------------+------------------------+-------+------------------+------------------------+
| 5b323aed88bcb100e9f8e7c4 | succeeded (0s elapsed) | task1 | test.echo_action | Tue, 26 Jun 2018       |
|                          |                        |       |                  | 13:09:01 UTC           |
+--------------------------+------------------------+-------+------------------+------------------------+
root@3e837b4b137b:/# st2 run test.pass_unicode_output2
..
id: 5b323b0b88bcb100e9f8e7c6
action.ref: test.pass_unicode_output2
parameters: None
status: succeeded
result_task: task2
result:
  exit_code: 0
  result: Rue de la D\xe9fense
  stderr: ''
  stdout: ''
start_timestamp: Tue, 26 Jun 2018 13:09:31 UTC
end_timestamp: Tue, 26 Jun 2018 13:09:34 UTC
+--------------------------+------------------------+-------+------------------+------------------------+
| id                       | status                 | task  | action           | start_timestamp        |
+--------------------------+------------------------+-------+------------------+------------------------+
| 5b323b0c88bcb100e9f8e7c9 | succeeded (0s elapsed) | task1 | test.echo_action | Tue, 26 Jun 2018       |
|                          |                        |       |                  | 13:09:32 UTC           |
| 5b323b0c88bcb100e9f8e7cb | succeeded (1s elapsed) | task2 | test.echo_action | Tue, 26 Jun 2018       |
|                          |                        |       |                  | 13:09:32 UTC           |
+--------------------------+------------------------+-------+------------------+------------------------+
```
