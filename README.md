# log-receiver

Simple server for displaying logs, made for NLog.

Send HTTP Post to localhost:1337, where data is formatted as `{time}|{name}|{level}|{message}`

To use with NLog, you can add this to nlog.config targets:
`<target xsi:type="Network" name="ws" address="http://localhost:1337" encoding="UTF-8" layout="${time}|${iis-site-name}|${level}|${message}" />`
