'use client'

import { Menu, Group, Center, Burger } from '@mantine/core'
import { useDisclosure } from '@mantine/hooks'
import classes from './Header.module.css'
import Link from 'next/link'
import { IconChevronDown } from '@tabler/icons-react'

const links = [
  { link: '/dashboard', label: 'Dashboard' },
  {
    link: '#1',
    label: 'Teams',
    links: [
      { link: '/teams', label: 'List teams' },
      { link: '/teams/create', label: 'Create a new team' },
    ],
  },
  {
    link: '#2',
    label: 'Games',
    links: [
      { link: '/games', label: 'List Games' },
      { link: '/games/create', label: 'Create new game' },
    ],
  },
]

export function Header() {
  const [opened, { toggle }] = useDisclosure(false)

  const items = links.map((link) => {
    const menuItems = link.links?.map((item) => (
      <Link key={item.link} href={item.link}>
        <Menu.Item key={item.link}>{item.label}</Menu.Item>
      </Link>
    ))

    if (menuItems) {
      return (
        <Menu
          key={link.label}
          trigger="hover"
          transitionProps={{ exitDuration: 0 }}
          withinPortal
        >
          <Menu.Target>
            <Link href={link.link} className={classes.link}>
              <Center>
                <span className={classes.linkLabel}>{link.label}</span>
                <IconChevronDown size="0.9rem" stroke={1.5} />
              </Center>
            </Link>
          </Menu.Target>
          <Menu.Dropdown>{menuItems}</Menu.Dropdown>
        </Menu>
      )
    }

    return (
      <Link href={link.link} key={link.label} className={classes.link}>
        {link.label}
      </Link>
    )
  })

  return (
    <header className={classes.header}>
      <div className={classes.inner}>
        <div>Challenge</div>
        <Group gap={10} visibleFrom="sm">
          {items}
        </Group>
        <Burger opened={opened} onClick={toggle} size="sm" hiddenFrom="sm" />
      </div>
    </header>
  )
}
