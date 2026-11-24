from searescue.metrics import summarize
def test_discovery_rate(): assert summarize(2,4,10,[100,80])["discovery_rate"]==.5
