def analog_result():
    # Sensor outputs values >255, need to tackle that
    gpio.output(led_output_pin, False)
    sleep(0.5)
    ambient_inp = ADC0834.getResult(analog_input_pin)
    gpio.output(led_output_pin, True)
    sleep(0.5)
    final_inp = ADC0834.getResult(analog_input_pin)
    diff = final_inp - ambient_inp
    gpio.output(led_output_pin, False)
    return diff
