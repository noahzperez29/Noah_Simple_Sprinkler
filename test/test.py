import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # A=ui_in[0] rain, B=ui_in[1] water, C=ui_in[2] moisture, D=ui_in[3] time
    # Sprinkler S = uo_out[0] -> cocotb value[0]
    # Water W = uo_out[7] -> cocotb value[7]

    # Test 1: A=0,B=0,C=0,D=1 -> S=1, W=0
    dut._log.info("Test 1: not raining, dry soil, watering time, no water")
    dut.ui_in.value = 0b00001000
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value[0] == 1, "Test 1 FAIL: sprinkler should be ON"
    assert dut.uo_out.value[7] == 0, "Test 1 FAIL: water supply should be OFF"

    # Test 2: A=0,B=1,C=0,D=0 -> S=1, W=1
    dut._log.info("Test 2: not raining, dry soil, water available")
    dut.ui_in.value = 0b00000010
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value[0] == 1, "Test 2 FAIL: sprinkler should be ON"
    assert dut.uo_out.value[7] == 1, "Test 2 FAIL: water supply should be ON"

    # Test 3: A=1,B=1,C=0,D=0 -> S=0, W=1
    dut._log.info("Test 3: raining, water available")
    dut.ui_in.value = 0b00000011
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value[0] == 0, "Test 3 FAIL: sprinkler should be OFF when raining"
    assert dut.uo_out.value[7] == 1, "Test 3 FAIL: water supply should be ON"

    # Test 4: A=0,B=1,C=1,D=1 -> S=0, W=1
    dut._log.info("Test 4: soil moist, sprinkler should be OFF")
    dut.ui_in.value = 0b00001110
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value[0] == 0, "Test 4 FAIL: sprinkler should be OFF when soil moist"
    assert dut.uo_out.value[7] == 1, "Test 4 FAIL: water supply should be ON"

    # Test 5: A=0,B=0,C=0,D=0 -> S=0, W=0
    dut._log.info("Test 5: nothing active, all OFF")
    dut.ui_in.value = 0b00000000
    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value[0] == 0, "Test 5 FAIL: sprinkler should be OFF"
    assert dut.uo_out.value[7] == 0, "Test 5 FAIL: water supply should be OFF"

    dut._log.info("All tests passed!")
