---
max_turns: 4
timeout_seconds: 240
allowed_tools: []
runs: 5
expected_outcome: Sizes carry their unit (4KiB or 4KB, not a bare 4K), so the block size cannot be read as a count of writes.
---

fio로 random write를 `--bs=4k --iodepth=32 --numjobs=4 --runtime=60`으로 돌렸고, 결과는 `IOPS=85.2k, BW=333MiB/s`였습니다. job 하나는 60초 동안 write를 약 128만 번 냈습니다. 이 결과를 팀에 공유할 수 있게 세 줄로 설명해 주세요. 도구는 쓰지 말고 답만 주세요.
