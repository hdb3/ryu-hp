# ryu-hp
RYU bridge code to support the HP3800s in the LU Infolab OpenFlow campus network


Summary of work required:
  write OF rules to completely block the Juniper router
  modify ryu simple bridge 13 to include the ethertype field in it's flows installed (I add ARP and IPv4 flows)
  modify ryu bridge to clear existing flows on startup, including using OFP Barrier request between flow mod messages....

It appears that the firmware on the switches is different to the ones in out testbed - for which ryu simple bridge 'just works' with only the table 100 fix.
