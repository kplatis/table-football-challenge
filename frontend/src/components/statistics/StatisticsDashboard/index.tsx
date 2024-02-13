'use client'

import { StatisticsCategory } from '@/types/statistics'
import { Tabs, rem } from '@mantine/core'
import { IconUser, IconUsers, IconUsersGroup } from '@tabler/icons-react'
import StatisticsTable from '../StatisticsTable'

export default function StatisticsDashboard() {
  const iconStyle = { width: rem(12), height: rem(12) }

  return (
    <Tabs
      color="violet"
      defaultValue={StatisticsCategory.All}
      keepMounted={false}
    >
      <Tabs.List>
        <Tabs.Tab
          value={StatisticsCategory.All}
          leftSection={<IconUsersGroup style={iconStyle} />}
        >
          All
        </Tabs.Tab>
        <Tabs.Tab
          value={StatisticsCategory.Players}
          leftSection={<IconUser style={iconStyle} />}
        >
          Players
        </Tabs.Tab>
        <Tabs.Tab
          value={StatisticsCategory.Teams}
          leftSection={<IconUsers style={iconStyle} />}
        >
          Teams
        </Tabs.Tab>
      </Tabs.List>

      <Tabs.Panel value={StatisticsCategory.All}>
        <StatisticsTable category={StatisticsCategory.All} />
      </Tabs.Panel>

      <Tabs.Panel value={StatisticsCategory.Players}>
        <StatisticsTable category={StatisticsCategory.Players} />
      </Tabs.Panel>

      <Tabs.Panel value={StatisticsCategory.Teams}>
        <StatisticsTable category={StatisticsCategory.Teams} />
      </Tabs.Panel>
    </Tabs>
  )
}
